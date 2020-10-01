---
_db_id: 237
available_flavours:
- python
content_type: project
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - topics/data-science-specific/natural-language-processing
  soft:
  - topics/python-self-learning
  - topics/jupyter-notebooks-best-practices
ready: true
story_points: 21
submission_type: repo
tags:
- nlp
title: Natural language processing
---

The contents of the State of the Nation Address (SONA) for every year dating back to 1990 is available on the [South African Government website](https://www.gov.za/state-nation-address). This gives us a great opportunity to look at the priorities and challenges have faced over time, and the focus points for the various presidents over this time.

1. Create a corpus from the English-language text for the SONAs dating back to 2000. Save them with the speaker information and date for later analysis. Where there is more than one SONA per year, get both.

2. Use `NLTK` to create a document-term matrix from the text. To do this, the text should be:

- in lowercase with punctuation and numbers removed (tip: use regular expressions)
- tokenized and lemmatized
- without stop words
- in a matrix

3. Examine the most frequently removed terms in each speech. You may need to add additional stop words that are said very often, such as "South Africa" and "country". If a word occurs in the top 10 words in each SONA, add it to the stop words list.

4. How do the speeches compare in terms of complexity and length? How many speeches are there per president? On average, which presidents use the most unique words and which presidents use the most words?

5. Create word clouds to visualise the speeches for each president. What are the main issues that they talked about during their presidency?

6. Use TextBlob to do sentiment analysis of the SONAs. Get the polarity and subjectivity for each SONA and visualise the changes in polarity and subjectivity over time. Also create a graph of the average polarity and subjectivity by president. Do you notice any patterns?

7. How have focus areas and sentiment in the SONAs changed over the last twenty years in South Africa? Are there clear changes in focus areas between different presidents?