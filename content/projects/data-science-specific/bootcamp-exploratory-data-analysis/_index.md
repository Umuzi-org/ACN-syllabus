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

It's good practice to structure your files well, so we'll expect you to have a separate directory for "data" and "notebook", so that your final file structure looks something like this: 

```
├──data
│  └── raw_data.csv
├──notebook
│  └── eda.ipynb
├──README.md
├──requirements.txt
└──.gitignore 
```


## Questions

The [dataset](data.csv) consists of health and demographic data for the period 2014-2015, obtained from [Global Health Observatory Data Repository](http://apps.who.int/gho/data/node.main). Here is some [metadata](data-info.txt) that may be useful.

1. Import the [dataset](data.csv). This data should be named `health_and_demographic_df`
2.  Are there any missing values in the dataset? You can deal with missing values by either dropping them or filling them with some value (in a variety of ways) or ignoring them. What do you think is best in this case? And why? Here is a resource for dealing with missing values: https://www.analyticsvidhya.com/blog/2021/10/a-complete-guide-to-dealing-with-missing-values-in-python/. Keep in mind that if you are filling the missing values with one of the three main measures of central tendency, Sometimes it makes sense to replace a missing value with a measure(like median) of the column (perhaps if we had a dataset of male heights around South Africa and we had a few missing values to deal with). In the case of GNI we are dealing with global data. And specifically, we are tasked with doing a fair amount of analysis of regional differences. The measure for GNI for Africa can be around 1620. The measure for GNI in general can be around 7870. That is a significant order of magnitude bigger! So if one of the missing countries was in Africa then it would skew the African data by making that replacement. 

3. Are there any other problems with the data? If so, fix them. After this, please the new DataFrame here should be called `cleaned_health_and_demographic_df`.

4. Identify the country with the lowest % of their population under 15 and the one with the highest. Your final table variable here should be called `lowest_under_15_df`.

5. Which region has the highest % of their population over 60? Your final table variable here should be called `highest_over_60_df`.

6. Does fertility decrease as income increases? Are there any countries that don't seem to follow this relation? The final table you create here should be called `fertility_and_income_df`. 

7. Which regions have the lowest literacy rates? The final table you create here should be called `lowest_literacy_rates_df`. 

8. Which regions have the lowest child mortality rates? The final table you create here should be called `lowest_child_mortality_df`. 

9. What is the life expectancy across different regions? Create a box-and-whisker plot to investigate this. What can we conclude about life expectancy across different regions? The DataFrame used to create the box-and-whisker plot should be called `life_expectancy_df`

10. How is life expectancy related to wealth across different regions? The DataFrame used to demonstrate this should be called `life_expectancy_and_wealth_df`. How is wealth related to fertility across different regions? The DataFrame used to demonstrate this should be called `fertility_and_wealth_df`. Do these relationships hold for African countries? 

11. Create appropriate graphs to visually represent the relationship between literacy and life expectancy by region,the DataFrame used to create this graph should be called `regional_life_expectancy_and_literacy_df` and then for African countries, the DataFrame used to create this graph should be called `africa_life_expectancy_and_literacy_df`. What can be concluded from the graphs? How confident can we be in the relationships represented here? 


### Instructions for reviewers

- Ensure that correct methods were used to check for any missing values in the data, also check how they dealt with missing values and if they gave a valid reason(s) for choosing that method.
- Ensure that they checked if the data has any other problems and resolved them if so.
- Ensure that the notebook has an introduction at the beginning, insights for every answered question, and a conclusion at the end.
- Ensure that all plots have their titles and axes labeled in bold.
