---
_db_id: 648
content_type: project
flavours:
- python
prerequisites:
  hard:
  - topics/data-science-specific/datacamp/intro-to-python
  soft:
  - topics/data-science-specific/intro-to-google-colab
ready: true
submission_type: repo
tags:
- statistics
- data-analysis
title: Bootcamp Exploratory Data Analysis
---

## Instructions

Your task is to use the given data to answer all the questions below. Any other additional analysis you think will help your submission is cool with us but NO external data may be used.

We will not only be assessing your code but also how you structure and present your analysis. This [notebook](notebook.ipynb) has a guide to the general structure we expect.

Your repo should contain everything needed to replicate your work:

- data
- notebook
- `requirements.txt`

## Questions

The [data set](data.csv) consists of health and demographic data for the period 2014-2015, obtained from [Global Health Observatory Data Repository](http://apps.who.int/gho/data/node.main). Here is some [metadata](data-info.txt) that may be useful.

1. Are there any missing values in the data set? You can deal with missing values by either dropping them or filling them with some value (in a variety of ways) or ignoring them. What do you think is best in this case? And why? Here is a resource for dealing with missing values : https://www.analyticsvidhya.com/blog/2021/10/a-complete-guide-to-dealing-with-missing-values-in-python/

2. Are there any other problems with the data? If so, fix them.

3. Identify the country with the lowest % of their population under 15 and the one with the highest.

4. Which region has the highest % of their population over 60?

5. Does fertility decrease as income increases? Are there any countries that don't seem to follow this relation?

6. Which regions have the lowest literacy rates?

7. Which regions have the lowest child mortality rates?

8. What is the life expectancy across different regions? Create a box-and-whisker plot to investigate this. What can we conclude about life expectancy across different regions?

9. How is life expectancy related to wealth across different regions? How is wealth related to fertility across different regions? Do these relationships hold for African countries?

10. Create appropriate graphs to visually represent the relationship between literacy and life expectancy by region, and then for African countries. What can be concluded from the graphs? How confident can we be in the relationships represented here?


### Instructions for reviewers

- Ensure that correct methods were used to check for any missing values in the data, also check how they dealt with missing values and if they gave a valid reason(s) for choosing that method.
- Ensure that they checked if the data has any other problems and resolved them if so.
- Ensure that the notebook has an introduction at the beginning, insights for every answered question, and a conclusion at the end.
- Ensure that all plots have their titles and axes labelled in bold.