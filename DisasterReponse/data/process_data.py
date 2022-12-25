import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """Load message and categories data from disk
    
    Parameters
    ----------
    messages_filepath : str
        The file location of the messages
    categories_filepath : str
        The file location of the messages

    Returns
    -------
    Nothing
    """

    # load messages dataset
    messages = pd.read_csv("data/messages.csv")
    messages.head()

    # load categories dataset
    categories = pd.read_csv("data/categories.csv")
    categories.head()

    # merge datasets
    df = pd.merge(messages, categories, on="id")
    df.head()
    
    return df

def clean_data(df):
    """Clean the data
    
    Parameters
    ----------
    df : Dataframe
        Dataframe to process
    
    Returns
    -------
    Nothing
    """
    # create a dataframe of the 36 individual category columns
    categories = df["categories"].str.split(';', expand=True)
    categories.head()

    # select the first row of the categories dataframe
    row = categories.loc[0, :]

    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing
    category_colnames = row.apply(lambda x: x[:-2]).values
    print(category_colnames)

    # rename the columns of `categories`
    categories.columns = category_colnames
    categories.head()

    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1]
        
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
        if (categories[column] > 1):
            categories[column] = 1
            
    categories.head()


    # drop the original categories column from `df`
    df.drop("categories", axis=1, inplace=True)

    df.head()

    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1)
    df.head()

    # check number of duplicates
    df.duplicated().sum()
    print(df.duplicated().sum())

    # drop duplicates
    df.drop_duplicates(inplace=True)

    # check number of duplicates
    df.duplicated().sum()

    return df
    
def save_data(df, database_filename):
    """Save the dataframe to db file

    Parameters
    ----------
    df : Dataframe
        Dataframe to save
    database_filename : str
        The path to save the dataframe
    
    Returns
    -------
    Nothing
    """

    engine = create_engine('sqlite:///DisasterResponse_t.db')
    df.to_sql('DisasterResponseTable', engine, index=False, if_exists='replace')

def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()