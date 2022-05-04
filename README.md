# Sentiment analysis of book summaries using NLP(natural language processing)
## Objective
To extract E-books of your choice and extract summary ,categorize summary as positive, negative or neutral. Build a NLP model for sentiment analysis

## Data extraction
I have taken Book summary data from https://www.goodreads.com/
web scraping tool -- Octoparse

## Steps followed for data extraction using octoparse:

1) Go to the web page
2) Create A pagination
3) Build a loop Item
4) Extract the data
5) Run the task and get the data

## EDA
Steps perform in EDA:

1) Data cleaning
2) Tokenization
3) Enrichment – POS tagging
4) Stop words removal
5) Obtaining the stem words

## Model building
Model -- Vader Model 
VADER (Valence Aware Dictionary and Sentiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts from other domains
The sum of pos, neg, neu intensities give 1. Compound ranges from -1 to 1 and is the metric used to draw the overall sentiment.
positive if compound >= 0.5
neutral if -0.5 < compound < 0.5
negative if -0.5 >= compound



## Model deployment
I have deployed the model on streamlit platform

### Screenshot of outputs:

![image](https://user-images.githubusercontent.com/91273990/166725130-d1173cbe-9120-4bab-9b08-289febfa20a0.png)

![image](https://user-images.githubusercontent.com/91273990/166725536-6f8fc11a-5689-485c-a228-36394c2d6697.png)

