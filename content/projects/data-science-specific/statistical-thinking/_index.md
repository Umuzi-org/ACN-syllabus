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

The Millennium Development Goals were a set of 8 goals for 2015 that were defined by the United Nations to help improve living conditions and the conditions of our planet. Key indicators were defined for each of these goals, to see whether they were being met. We will have a look at some of the key indicators from _Goal 7: Ensure environmental sustainability_, namely carbon dioxide (CO2) emissions, protected land and sea areas, and forests. The full dataset can be found at http://mdgs.un.org/.

### Questions

1. Load the [MDG data](MDG_Export_20191227.csv) into a pandas DataFrame. You will need the packages `matplotlib`, `numpy`, `seaborn`, `pandas` and `scipy`.
2. How many different countries are represented? Save this number in a variable `number_of_countries`. 
3. How many missing values do we have by country, year and series? You need to create 3 DataFrames:

  - `missing_values_by_country_df` with column names `country` and `missing_values_count`
  - `missing_values_by_year_df` with column names `year` and `missing_values_count` 
  - `missing_values_by_series_df` with column names `series` and `missing_values_count`

4. Who are the top and bottom 5 countries in terms of CO2 emissions in 1990 and what are their emissions? Create DataFrames called `top_countries_co2_emmissions_df` and  `bottom_countries_co2_emmissions_df` with columns `Country` and `co2_emissions` and order the data from highest to lowest for `top_countries_co2_emmissions_df` and from lowest to highest for `bottom_countries_co2_emmissions_df`. How have these emissions changed by 2011?
5. Check and correct any problems with the data. At this stage ensure that your dataset is in a DataFrame named: `mdg_df`
6. Calculate the mean and median CO2 emissions for 1990. Save each answer in the variables `mean_co2_emmisions_1990` and `median_co2_emmisions_1990` respectively. Why do you think these values differ? 
7. Calculate the minimum, maximum and interquartile range of the CO2 emissions for 1990. Please store these as variables named: `minimum_co2_emmisions_1990`, `maximum_co2_emmisions_1990` and `iqr_co2_emissions_1990` respectively. Using this information, as well as the mean and median calculated previously for this year, explain what this tells us about the distribution of CO2 emissions?
8. Create a histogram of the CO2 emissions for 1990. Is this what you expected from your answers in questions 3 and 4? 
9. Calculate the standard deviation and standard error of the mean for CO2 emissions in 1990. Save each answer in the variables `std_co2_emmisions_1990` and `stderr_co2_emmisions_1990` respectively. How is the standard error different from the standard deviation? 
10. Create a line graph to show CO2 emissions in Brazil, Russia, China, India, the USA and South Africa over time. What does the graph tell you about the difference and change in C02 emissions in these countries?
11. What is the mean and standard deviation for land area covered by forest in 1990? Save each answer in the variables `mean_land_area_covered_forest_1990` and `std_land_area_covered_forest_1990` respectively. Why do you think the standard deviation is so large? 
12. Create histograms for land area covered by forest and percentage of area protected in 1990. Describe the distributions.
13. Create a scatterplot with a regression line using `seaborn.regplot` to show the relationship between the proportion of land area covered by forest and the percentage of area protected in 2000.

  - What is the relationship between these two variables?
  - Describe any patterns in the scatterplot.
  - Do you notice any unusual/extreme values that do not fit the general trend? If you see any unusual values, briefly describe them (Who are they? In what way are they different?).

14. Since neither forested land area nor protected area is normally distributed, we will need to log transform these variables in order to calculate a correlation coefficient. Log transform the variables and show the transformed distributions in a histogram.

15. Using the `pearsonr` function from the `scipy.stats` module, calculate the Pearson correlation coefficient (and its corresponding p value) to determine the nature of the relationship between proportion of land area covered by forest and the percentage of area protected (as measured in 1990 and log transformed). See `help(pearsonr)` for help on this function.

  - Interpret the size and direction of the correlation statistic.
  - Is the relationship statistically significant? Report the appropriate statistic(s) to support your answer.

16. Calculate the Spearman Rank-Order Correlation Coefficient. This test only looks at the _order_ of the categories, not the _values_. The Spearman Rank-Order Coefficient is therefore not influenced by non-normality of variables or outliers. How do the results of this test compare the results of the Pearson's correlation?

## Instructions for reviewer

1. A learner should be able to find any problems in the dataset without printing out the entire dataset like
   one would do in an Excel spreadsheet for example.  One thing to check for is changing the way pandas prints
   a dataset, things such as `pd.set_option()`.

2. Learners should understand the difference between a missing value and a NaN value.  It seems that students use
   the terminology interchangeably.

3. Learners need to be able to make the correct deductions following commands such as `.info()` and `.describe()`.
   Sometimes learners will use these commands since they know it is required of them, but they are not entirely
   comfortable with what is presented to them by these commands.

4. How do learners answer basic questions such as 'How many countries are represented'.  If it is a case of endless
   `for` loops and `if` statements then the learner is not comfortable with the basic functionality which pandas or
   numpy provides.

5. Does the learner clean the dataframe, impute missing values and set the dataframe in a neat order at the beginning
   of the project.  If not, the learner will continue to create sub-dataframes for each question to follow.  This is
   bad practice.

6. Learners should be comfortable in answering questions such as 'Who are the top and bottom five countries in terms of
   CO2 emissions in 1990, and what are their emissions' using standard pandas functionality such as `.nlargest()`,
   `.contains()`, `.groupby()`.  When learners don't understand how to use these functions as a collective they revert
   to things such as printing out an entire dataframe or finding the answer through a series of loops.

7. Any plots that are to be done, should be neat and easily readable.  The plot must have a heading, the labels should
   be in bold, the x and y axes should make sense (Multipliers should be added if necessary).

8. Most learners have no problem in calculating the standard error or the standard deviation in the mean, however,
   when they have to explain their findings they find it difficult to do so since they do not thoroughly grasp the
   underlying statistical concepts, or they have forgotten their true meaning since they last studied the topic.

9. Pearson coefficient, Spearman coefficient, correlation coefficient, p-value, Null hypothesis and Alternative hypothesis.
   This is where most learners have major difficulty.  They can find the answers to the questions through the code easy
   enough, but they cannot clearly and simply explain what these terms mean and how they all work together, when to accept
   or reject a Null hypothesis, if the p-value is small, but the Null hypothesis is stated not as a negative but as
   a positive, should I still reject the Null hypothesis?  These are the kind of questions learners should be
   comfortable to answer.
