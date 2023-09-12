---
_db_id: 237
content_type: project
flavours:
- python
learning_outcomes:
- data_sci_nlp
- data_sci_nlp_data_preparation
- data_sci_nlp_frequency_analysis
- data_sci_sentiment_analysis
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - topics/data-science-specific/natural-language-processing
  - topics/data-science-specific/data-science-methodology
  - topics/jupyter-notebooks-best-practices
  - projects/data-science-specific/multivariate-linear-regression
  - projects/data-science-specific/logistic-regression
ready: true
story_points: 21
submission_type: repo
tags:
- nlp
- sentiment-analysis
- nltk
- textblob
title: Natural language processing.
---
In order to help you develop your NLP skills, we have prepared two datasets for you to work with.These datasets are designed to improve your understanding of text processing, sentiment analysis, and text classification. You have the option to work on either one dataset or both datasets. Please follow the instructions below to get started:

## Dataset 1: [Movie Reviews Sentiment Analysis](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

### Description: 
This dataset contains a collection of movie reviews, each labeled with its corresponding sentiment (positive or negative). This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. We provide a set of 25,000 highly polar movie reviews for training and 25,000 for testing. So, predict the number of positive and negative reviews using Logistic Regression or other classification algorithms.
For more dataset information, please go through the following [link](http://ai.stanford.edu/~amaas/data/sentiment/)

## Instructions:
1. Download the dataset file named "Movie Reviews Sentiment Analysis" from the provided link.
2. Perform data preprocessing tasks such as tokenization, stopword removal, and lowercasing.
3. Explore the dataset to gain insights into its distribution of sentiments.
4. Build and train a machine learning learning model to classify movie reviews as either positive or negative.
5. Evaluate the performance of your model using appropriate metrics (accuracy, precision, recall, F1-score).

## Dataset 2: The contents of the State of the Nation Address (SONA) for every year dating back to 1990 is available on the [South African Government website](https://www.gov.za/state-nation-address).

### Description:
This gives us a great opportunity to look at the priorities and challenges have faced over time, and the focus points for the various presidents over this time.

## Instructions:
1. Create a corpus from the English-language text for the SONAs dating back to 2000. Save them with the speaker information and date for later analysis. Where there is more than one SONA per year, get both.
2. Use `spaCy` to create a document-term matrix from the text. To do this, the text should be:  
  * in lowercase with punctuation and numbers removed (tip: use regular expressions)
  * tokenized and lemmatized
  * without stop words
  * in a matrix
3. Examine the most frequently used terms in each speech. You may need to add additional stop words that are said very often, such as "South Africa" and "country". If a word occurs in the top 10 words in each SONA, add it to the stop words list.
4. How do the speeches compare in terms of complexity and length? How many speeches are there per president? On average, which presidents use the most unique words and which presidents use the most words?
5. Create word clouds to visualise the speeches for each president. What are the main issues that they talked about during their presidency?
6. Use [spaCy-TextBlob](https://spacy.io/universe/project/spacy-textblob) to do sentiment analysis of the SONAs. Get the polarity and subjectivity for each SONA and visualise the changes in polarity and subjectivity over time. Also create a graph of the average polarity and subjectivity by president. Do you notice any patterns?
7. How have focus areas and sentiment in the SONAs changed over the last twenty years in South Africa? Are there clear changes in focus areas between different presidents?

## Supporting Material:
1. https://www.analyticsvidhya.com/blog/2022/09/complete-guide-to-analyzing-movie-reviews-using-nlp/
2. https://towardsdatascience.com/a-gentle-introduction-to-natural-language-processing-e716ed3c0863
