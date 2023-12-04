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

It's good practice to structure your files well, so we'll expect you to have a separate directory for "data" and "notebooks", so that your final file structure looks something like this: 

```
├──data
│  └── raw_data.csv
├──notebook
│  └── eda.ipynb
├──README.md
├──requirements.txt
└──.gitignore 
```

## Dealing with missing values in a dataset

Before we dive into the tasks of this project, let's talk a bit about missing values. For a variety of reasons, the data we work with could have missing or invalid data. Depending on the kind of data we are working with and the extent of the data missing, we typically deal with missing data either by dropping it (for example in the case of entirely/nearly entirely missing columns or rows) or by replacing them with a suitable values.

Later in this program you'll be learning how to train machine learning models using various kinds of data. When doing so, missing values cannot simply be ignored. Further, when it comes to datasets with many columns (also known as features), it is bad practice to drop an entire row for a few missing values. 

Here is a resource for dealing with missing values : https://www.analyticsvidhya.com/blog/2021/10/a-complete-guide-to-dealing-with-missing-values-in-python/


## Questions

The [data set](data.csv) consists of health and demographic data for the period 2014-2015, obtained from [Global Health Observatory Data Repository](http://apps.who.int/gho/data/node.main). Here is some [metadata](data-info.txt) that may be useful.

1. Load the dataset into a pandas DataFrame called `health_and_demographics_df`,  display the first 10 rows and determine how many missing values there are per feature. 

2. Address any missing values in the dataset. Given the kind of data we have in this dataset, as well as the *regional* analysis you will be tasked with performing below, it should not simply be replacing a missing value with the mean/median of the whole column. 

3. Are there any other problems with the data? If so, fix them. At this stage ensure that your dataset is in a DataFrame named: `health_and_demographics_df_cleaned`

4. Identify the country with the lowest % of their population under 15 and the one with the highest and save each country name as a string in the variables `country_with_lowest_population_percentage_under_15` and `country_with_highest_population_percentage_under_15` respectively.

5. Which region has the highest % of their population over 60? Save this region in the the variable `region_with_highest_population_percentage_over_60`

6. Does fertility decrease as income increases? Are there any countries that don't seem to follow this relation?

7. Which regions have the lowest literacy rates? Create a dataframe called `regional_literacy_df` with columns `region` and `literacy_rate` and order the data from lowest to highest. 

8. Which regions have the lowest child mortality rates? Create a dataframe called `regional_child_mortality_df` with columns `region` and `child_mortality_rate` and order the data from lowest to highest. 

9. What is the life expectancy across different regions? Create a box-and-whisker plot to investigate this. What can we conclude about life expectancy across different regions?

10. How is life expectancy related to wealth across different regions? How is wealth related to fertility across different regions? Do these relationships hold for African countries?

11. Create appropriate graphs to visually represent the relationship between literacy and life expectancy by region, and then for African countries. What can be concluded from the graphs? How confident can we be in the relationships represented here?


### Instructions for reviewers

- Ensure that correct methods were used to check for any missing values in the data, also check how they dealt with missing values and if they gave a valid reason(s) for choosing that method.
- Ensure that they checked if the data has any other problems and resolved them if so.
- Ensure that the notebook has an introduction at the beginning, insights for every answered question, and a conclusion at the end.
- Ensure that all plots have their titles and axes labelled in bold.