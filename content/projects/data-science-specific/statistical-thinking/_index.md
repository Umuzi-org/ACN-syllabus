---
_db_id: 248
content_type: project
flavours:
- python
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - projects/data-science-specific/data-visualisation/linux-evolution
  - topics/jupyter-notebooks-best-practices
  - projects/data-science-specific/assertive-programming-tricks-for-pandas
ready: true
story_points: 13
submission_type: repo
tags:
- stats
title: Statistical Thinking
---

## Objectives

At the end of this assignment you should be able to:

- do exploratory data analysis on a new dataset.
- know what the measures of central tendency and spread are used for.
- know when to use which measure of central tendency.
- describe different distributions and interpret a histogram.
- know what outliers are and how they affect measures of central tendency and spread.
- interpret correlations from a graph and from the correlation coefficient.

## Background material

- [Crash Course Statistics: Measures of Spread](https://youtu.be/R4yfNi_8Kqw)
- [Crash Course Statistics: Plots, Outliers and Justin Timberlake](https://youtu.be/HMkllhBI91Y)
- [Crash Course Statistics: Correlation Doesn’t Equal Causation](https://youtu.be/GtV-VYdNt_g)

## Tutorials

Complete the DataCamp courses [Statistical Thinking in Python Part 1](https://www.datacamp.com/courses/statistical-thinking-in-python-part-1) and [Statistical Thinking in Python Part 2](https://www.datacamp.com/courses/statistical-thinking-in-python-part-2).

## Assignment

### Instructions

The Millennium Development Goals were a set of 8 goals for 2015 that were defined by the United Nations to help improve living conditions and the conditions of our planet. Key indicators were defined for each of these goals, to see whether they were being met. We will have a look at some of the key indicators from _Goal 7: Ensure environmental sustainability_, namely carbon dioxide (CO2) emissions, protected land and sea areas, and forests. The full dataset can be found at http://mdgs.un.org/ . 

### Directory structure
It's good practice to structure your files well, so we'll expect you to have a separate directory for "data" and "notebook" so that your final file structure looks something like this: 

```
├──data
│   └──MDG_Export_20191227.csv
├──notebook
│  └──statistical_thinking.ipynb
├──README.md
├──requirements.txt
└──.gitignore 
```

### Questions

1. Load the [MDG data](MDG_Export_20191227.csv) into a pandas DataFrame. You will need the packages `matplotlib`, `numpy`, `seaborn`, `pandas` and `scipy`.
2. How many different countries are represented? Save this number in a variable `number_of_countries`. 
3. How many missing values do we have by country, year and series? You need to create 3 DataFrames:

  - `missing_values_by_country_df` with column names `Country` and `missing_values_count`
  - `missing_values_by_year_df` with column names `Year` and `missing_values_count` 
  - `missing_values_by_series_df` with column names `Series` and `missing_values_count`

4. Check and correct any problems with the data. Drop any empty columns and those starting with “Type” or “Footnote”. At this stage ensure that your dataset is in a DataFrame named: `mdg_df`. 
5. Who are the top and bottom 5 countries in terms of CO2 emissions in 1990 and what are their emissions? Create DataFrames called `top_countries_co2_emmissions_1990_df` and  `bottom_countries_co2_emmissions_1990_df` with columns `Country` and `co2_emissions` and order the data from highest to lowest for `top_countries_co2_emmissions_1990_df` and from lowest to highest for `bottom_countries_co2_emmissions_1990_df`. Create similarly named data frames for the emissions in 2011. How have these emissions changed compared with 1990?
6. Calculate the mean and median CO2 emissions for 1990. Save each answer in the variables `mean_co2_emmisions_1990` and `median_co2_emmisions_1990` respectively. Why do you think these values differ? 
7. Calculate the minimum, maximum and interquartile range of the CO2 emissions for 1990. Please store these as variables named: `minimum_co2_emmisions_1990`, `maximum_co2_emmisions_1990` and `iqr_co2_emissions_1990` respectively. Using this information, as well as the mean and median calculated previously for this year, explain what this tells us about the distribution of CO2 emissions?
8. Create a histogram of the CO2 emissions for 1990. Is this the distribution you expected based on your answers from questions 6 and 7? 
9. Calculate the standard deviation and standard error of the mean for CO2 emissions in 1990. Save each answer in the variables `std_co2_emmisions_1990` and `stderr_co2_emmisions_1990` respectively. How is the standard error different from the standard deviation? 
10. Create a line graph to show CO2 emissions in Brazil, Russia, China, India, the USA and South Africa over time. What does the graph tell you about the difference and change in C02 emissions in these countries?
11. What is the mean and standard deviation for land area covered by forest in 1990? Save each answer in the variables `mean_land_area_covered_forest_1990` and `std_land_area_covered_forest_1990` respectively. Why do you think the standard deviation is so large? 
12. Create histograms for land area covered by forest and percentage of area protected in 1990. Describe the distributions.
13. Create a scatterplot with a regression line using `seaborn.regplot` to show the relationship between the proportion of land area covered by forest and the percentage of area protected in 2000.

  - What is the relationship between these two variables?
  - Describe any patterns in the scatterplot.
  - Do you notice any unusual/extreme values that do not fit the general trend? If you see any unusual values, briefly describe them (Who are they? In what way are they different?).

14. Since neither forested land area nor protected area is normally distributed, we will need to log transform these variables in order to calculate a correlation coefficient. Log transform the variables and show the transformed distributions in a histogram. You need to create 2 DataFrames:
  - `log_transformed_land_area_covered_2000_df` with column names `Country` and `log_transformed_forested_land_area_value`
  - `log_transformed_protected_area_2000_df` with column names `Country` and `log_transformed_protected_area_value`.

15. We'd like to determine the nature of the relationship between proportion of land area covered by forest and the percentage of area protected (as measured in 1990 and log transformed). Start with stating the "null" and "alternative" hypothesis for this enquiry. Using the `pearsonr` function from the `scipy.stats` module, calculate the Pearson correlation coefficient and its corresponding p value. Save this answer in a variable called `pearson_correlation_coefficient_1990`. The p value here should be saved in a variable called `pearson_p_value_1990`. See `help(pearsonr)` for help on this function.

  - Interpret the size and direction of the correlation statistic.
  - Is the relationship statistically significant? Report the appropriate statistic(s) to support your answer.

16. Calculate the Spearman Rank-Order Correlation Coefficient. Save this answer in a variable called `spearman_correlation_coefficient_1990`. The p value here should be saved in a variable called `spearman_p_value_1990`. This test only looks at the _order_ of the categories, not the _values_. The Spearman Rank-Order Coefficient is therefore not influenced by non-normality of variables or outliers. How do the results of this test compare with the results of the Pearson's correlation?

## Instructions for reviewer

1. Learners should understand the difference between a missing value and a NaN value.  It seems that students use
   the terminology interchangeably.

2. Learners need to be able to make the correct deductions following commands such as `.info()` and `.describe()`.
   Sometimes learners will use these commands since they know it is required of them, but they are not entirely
   comfortable with what is presented to them by these commands.

3. How do learners answer basic questions such as 'How many different countries are represented?' or  'Who are the top and 
   bottom 5 countries in terms of CO2 emissions in 1990 and what are their emissions?'.  If it is a case of 
   endless `for` loops and `if` statements then the learner is not comfortable using standard pandas functionality such as 
   `.nlargest()`, `.contains()`, `.groupby()`. 

4. Any plots that are to be done, should be neat and easily readable.  The plot must have a heading, the labels should
   be in bold, the x and y axes should make sense (Multipliers should be added if necessary).

5. Pearson coefficient, Spearman coefficient, correlation coefficient, p-value, Null hypothesis and Alternative hypothesis.
   This is where most learners have major difficulty.  They can find the answers to the questions through the code easy
   enough, but they cannot clearly and simply explain what these terms mean and how they all work together, when to accept
   or reject a Null hypothesis, if the p-value is small, but the Null hypothesis is stated not as a negative but as
   a positive, should I still reject the Null hypothesis?  These are the kind of questions learners should be
   comfortable to answer.
