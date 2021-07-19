---
_db_id: 233
content_type: project
flavours:
- python
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - projects/data-science-specific/statistical-thinking
  - projects/data-science-specific/cross-validation-and-simple-linear-regression
  - topics/jupyter-notebooks-best-practices
ready: true
story_points: 3
submission_type: repo
tags:
- multiple-linear-regression
title: Multivariate Linear Regression
---

This week is all about one-hot encoding and multiple regression.

## Background materials

1. [Robust One-Hot Encoding in Python](https://blog.cambridgespark.com/robust-one-hot-encoding-in-python-3e29bfcec77e)
2. [Feature Engineering and Selection ebook](http://www.feat.engineering/)
3. [One-hot encoding multicollinearity and the dummy variable trap](https://towardsdatascience.com/one-hot-encoding-multicollinearity-and-the-dummy-variable-trap-b5840be3c41a)
4. [Emulating R Regression Plots in Python](https://medium.com/@emredjan/emulating-r-regression-plots-in-python-43741952c034)
5. [Statsmodels Regression Plot](https://www.statsmodels.org/dev/examples/notebooks/generated/regression_plots.html)
6. [Building and evaluating models](https://www.ritchieng.com/machine-learning-evaluate-linear-regression-model/).
7. [Test/Train Splits and Crossvalidation](https://towardsdatascience.com/train-test-split-and-cross-validation-in-python-80b61beca4b6)
8. Interpreting residuals plot [Stattrek](https://stattrek.com/statistics/dictionary.aspx?definition=residual%20plot) and [Statwing](http://docs.statwing.com/interpreting-residual-plots-to-improve-your-regression/)

## Assignment

We will predict employee salaries from different employee characteristics (or features).
Import the data [salary.csv](salary.csv) to a Jupyter Notebook. A description of the variables is given in [Salary metadata.csv](Salary metadata.csv). You will need the packages `matplotlib` / `seaborn`, `pandas` and `statsmodels`.

### Steps and questions

1. Perform some **exploratory data analysis (EDA)** by creating appropriate plots (e.g scatterplots and histograms) to visualise and investigate relationships between dependent variables and the target/independent variable (salary).

    - Create a descriptive statistics table to further characterise and describe the population under investigation.
    - Which variables seem like good predictors of salary?
    - Do any of the variables need to be transformed to be able to use them in a linear regression model?

2. Perform some basic **features engineering** by one-hot encoding the variable Field into three dummy variables, using HR as the reference category. You can use pandas' `get_dummies()` function for this (refer to "Background materials 1-3").

3. Perform **correlation and statistical significance analysis** to validate the relationship salary to each of the potential predictor variables:

    - Calculate Pearson correlation coefficient and plot the corresponding correlation matrix
    - Calculate p-values related to the Pearson correlation coefficients
    - Address any problems that may adversely affect the multiple regression (e.g multicollinearity)

4. Conduct some basic **feature selection** tasks by aggregating results from EDA, correlation matrix and p-values. Justify your feature selection decisions.

5. **Train model**:
    - Split your data into a training and test set.
    - Fit a multiple linear regression model using a training dataset with corresponding features selected above
    - Use the multiple linear regression model created from independent variables selected above and the training dataset to predict _salary_ using the training dataset.
    - Interpret the standardised coefficients given in the statsmodels output.
    - What are the most important features when predicting employee salary?

6. **Evaluate model**

    - Run your model on the _test set_.
    - Calculate and explain the significance of the Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Square Error (RMSE) and R-squared values for your model
    - Calculate the standardised residuals (`resid()`) and standardised predicted values (`fittedvalues()`).
    - Plot the residuals versus the predicted values using seaborn's `residplot` with predicted values as the x parameter, and the actual values as y, specify `lowess=True`.
    - Are there any problems with the regression?

7. **Benchmark with cross-validation model**

    - Perform cross-validation using the training dataset, test and evaluate the cross-validation model with test data
    - Compare performance of the cross-validation model (less prone to over-fitting) to determine whether the developed model has overfitted or not
    - Does it seem like you have a reasonably good model?

### References

Data is made up and inspired by Cohen, Cohen, West & Aiken. [Applied Multiple Regression/Correlation Analysis for the Behavioral Sciences, 3rd Edition](https://books.google.co.za/books?hl=en&lr=&id=gkalyqTMXNEC&oi=fnd&pg=PP1&dq=Applied+Multiple+Regression/Correlation+Analysis+for+the+Behavioral+Sciences+r+cran&ots=tRJUV4k7bi&sig=JlckiBj89w1rUBk1e71FKnr3Otg).

## Instructions for reviewer

1. All relevant instructions from the [simple-linear-regression](http://syllabus.africacode.net/projects/data-science-specific/cross-validation-and-simple-linear-regression/index.html) project also apply here.

2. EDA means actually analysing the data; it's not enough to create a graph, there needs to be commentary on what it reveals about the data.

3. For the one-hot encoding, make sure that HR is used as the reference category.

4. An understanding of multi-collinearity should be clearly demonstrated and checked with any of the standard techniques.

5. A common issue is incorrect interpretation of the residuals plot. Make sure interpretation demonstrates understanding for what the residual tell us about the appropriateness of the model.
