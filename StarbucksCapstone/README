# Starbucks-Capstone-Challenge

## Dataset overview
The data spread across three different files. It is a dummy data, on the Starbuck mobile app, to simulate how different promotional offers impact user interaction and decisions. There are three types of offers as per the data set: buy-one-get-one (BOGO), discount, and informational - all of which are delivered over multiple channels. The main task is to identify different segments of users based on their identifiable feature (like age, income, transaction patterns etc) to offer better targeted promotional offers. Also finding other patterns and trends like the impact of each offers on the different segments of users etc.

### Data Dictionary
 - profile.json - Rewards program users (17000 users x 5 fields)
   - gender: (categorical) M, F, O, or null
   - age: (numeric) missing value encoded as 118
   - id: (string/hash)
   - became_member_on: (date) format YYYYMMDD
   - income: (numeric)
  
 - portfolio.json - Offers sent during 30-day test period (10 offers x 6 fields)
   - reward: (numeric) money awarded for the amount spent
   - channels: (list) web, email, mobile, social
   - difficulty: (numeric) money required to be spent to receive reward
   - duration: (numeric) time for offer to be open, in days
   - offer_type: (string) bogo, discount, informational
   - id: (string/hash)

 - transcript.json - Event log (306648 events x 4 fields)
   - person: (string/hash)
   - event: (string) offer received, offer viewed, transaction, offer completed
   - value: (dictionary) different values depending on event type
   - offer id: (string/hash) not associated with any "transaction"
   - amount: (numeric) money spent in "transaction"
   - reward: (numeric) money gained from "offer completed"
   - time: (numeric) hours after start of test
   
## Project Motivation<a name="motivation"></a>

This is the Capstone project for the Udacity Data Science Nanodegree.  
The basis or this project is simulated data that mimics customer behavior on the Starbucks rewards mobile app. Once every few days, Starbucks sends out an offer to users of the mobile app. An offer can be merely an advertisement for a drink or an actual offer such as a discount or BOGO (buy one get one free).  
In particular, the data consists of information on the different offers, on customer demographics, and on offer and transaction events.  

Utilizing this data, **my goal** is:

Can we classify if an offer is going to be successful based on demographic and offer information?
- Build a machine learning model predicting offer success based on the demographic information and the offer details that are provided in the data

and Answer following questions:
- Which offer is the most successful?
- Who spends more money? male or female?
 
## Libraries used <a name="Libraries"></a>
Libraries
This project requires Python 3.x and the following Python libraries installed:
- python==3.6.3(recommended)
- seaborn==0.8.1
- pandas==0.23.3
- numpy==1.12.1
- matplotlib==2.1.0
- sklearn==0.19.1


## File Descriptions <a name="files"></a>

This github repo contains
- \data: contains 3 data files, profile.json, transcript.json, portfolio.json
- Starbucks_Capstone_notebook.ipynb: Jupyter notebook of project.
- Starbucks_Capstone_notebook.html: html version of jupyter notebook
- README.md : contains detail about the project.

## summary of the project <a name="summary"></a>

Blogspot's article for this [here](https://thangduong.substack.com/p/starbucks-customer-behaviors-with).

In short summary is 
- DecisionTreeClassifier gains with 92.77% accuracy
- The most used offer types are BOGO and Discount. The other, informational offer is least used.

- Customers of age group between 46–80 and whose income is in between 60000–80000 responded most to the offers type 'BOGO'and then offer type 'Discount'. So it’s better to send those offers to these customers

- Starbucks should give more offers to Females than Males since they have more completed offers.

## Licensing and Acknowledgements<a name="licensing"></a>

- Must give credit to Starbucks for the data.
- This project is part of Data scientist Nanodegree from udacity.
