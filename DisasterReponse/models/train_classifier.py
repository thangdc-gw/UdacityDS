import sys

# import libraries
import pandas as pd
from sqlalchemy import create_engine

from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_multilabel_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import pickle


def load_data(database_filepath):
    """Load data from disk
    
    Parameters
    ----------
    database_filepath : str
        The file location of the database
    
    Returns
    -------
    Nothing
    """
    
    #load punkt sentences tokenize
    nltk.download(['punkt', 'wordnet'])


    # load data from database
    engine = create_engine('sqlite:///DisasterResponse_t.db')
    df = pd.read_sql_table('DisasterResponseTable', engine)
    X = df['message']
    Y = df.iloc[:, 4:]

    return X, Y, Y.columns

def tokenize(text):
    """Remove punctuation chars

    Parameters
    ----------
    text : str
        The corpus need to be processed
    
    Returns
    -------
    Nothing
    """
    
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
        
    return clean_tokens   

def build_model():
    """Build pipeline

    Returns
    -------
    pipeline:
        Pipeline
    """

    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    
    return pipeline

def evaluate_model(model, X_test, Y_test, category_names):
    """Evaluate the model

    Parameters
    ----------
    model : estimator
        The model to evaluate
    X_test : matrix
        X elements for testing
    Y_test : matrix
        Y elements for testing
    category_names : Columns
        Columns
    
    Returns
    -------
    Nothing
    """
    y_pred = model.predict(X_test)

    for index, column in enumerate(category_names.values):
        print(column, classification_report(Y_test[column], y_pred[:, index]))

def save_model(model, model_filepath):
    """Save the model

    Parameters
    ----------
    model : estimator
        The model to save
    model_filepath : str
        The path to save the model
    
    Returns
    -------
    Nothing
    """
    parameters = {
        # 'tfidf__use_idf': (True, False),
        # 'tfidf__smooth_idf': [True, False],
        # 'vect__max_df': (0.5, 0.75, 1.0),
        # 'vect__max_features': (None, 5000, 10000),
        'clf__estimator__n_estimators': [50, 100],
        'clf__estimator__min_samples_split': [2, 4]
    }
    cv = GridSearchCV(model, param_grid=parameters)
    pickle.dump(cv.best_estimator_, open(model_filepath, "wb"))

def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse_t.db disater_model.pkl')

if __name__ == '__main__':
    main()