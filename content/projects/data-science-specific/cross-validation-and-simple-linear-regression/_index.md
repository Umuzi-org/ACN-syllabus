---
_db_id: 234
available_flavours:
- python
content_type: project
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - projects/data-science-specific/statistical-thinking
  - projects/data-science-specific/data-visualisation/mobile-money-viz
  soft:
  - topics/python-self-learning
  - topics/jupyter-notebooks-best-practices
ready: true
story_points: 13
submission_type: repo
tags:
- simple-linear-regression
title: Cross-validation & Simple Linear Regression
---

## Key topics

- Simple linear regression
- Residuals
- Overfitting and underfitting
- Cross-validation
- Root Mean Square Error

## Background materials

### Regression

- [Introduction to Linear Regression](https://github.com/justmarkham/DAT4/blob/master/notebooks/08_linear_regression.ipynb)
- [Simple and Multiple Linear Regression in Python](https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9)
- [Crash Course Statistics: Regression](https://youtu.be/WWqE7YHR4Jc)
- [Khan Academy Engageny Algebra Topic D, Lessons 14 – 18 (Modelling relationships with a line & Residuals)](https://www.khanacademy.org/math/engageny-alg-1/alg1-2/alg1-2d-modeling-relationships-line/v/fitting-a-line-to-data)

### Overfitting and underfitting

- [Coursera Video](https://www.coursera.org/lecture/python-machine-learning/overfitting-and-underfitting-fVStr)

### Test/ training splits and cross-validation

- [Test/Train Splits and Crossvalidation in Python Tutorial](https://towardsdatascience.com/train-test-split-and-cross-validation-in-python-80b61beca4b6)
- [Google ML Training and Test Sets Video](https://developers.google.com/machine-learning/crash-course/training-and-test-sets/video-lecture)

## Assignment

We will predict employee salaries from different employee characteristics (or features).
We are going to use a simple supervised learning technique: linear regression. We want to build a simple model to determine how well Years Worked predicts an employee’s salary.
Import the data [salary.csv](salary.csv) to a Jupyter Notebook. A description of the variables is given in [Salary Metadata](Salary metadata.csv). You will need the packages matplotlib, pandas and statsmodels.

### Steps and questions

1. Split your data into a training and test set. Leave the test set for now. Examine the training data for missing and extreme values. Create histograms to show the distribution of the variables and a scatterplot showing the relationship between Years Worked and Salary. Are the data appropriate for linear regression? Is there anything that needs to be transformed or edited first?

2. Using the statsmodels package and the _training data_, run a simple linear regression for Salary with one predictor variable: Years Worked.
   - Does the model significantly predict the dependent variable? Report the amount of variance explained (R^2) and significance value (p) to support your answer.
   - What percentage of the variance in employees’ salaries is accounted for by the number of years they have worked?
3. What does the unstandardized coefficient (B or 'coef' in statsmodels) tell you about the relationship between Years Worked and Salary?
4. What do the 95% confidence intervals [0.025, 0.975] mean?
5. Calculate the expected salary for someone with 12 years’ work experience.
6. Calculate the expected salary for someone with 80 years’ work experience. Are there any problems with this prediction? If so, what are they?
7. We have only looked at the number of years an employee has worked. What other employee characteristics might influence their salary?

Now fit your model to your test set. DO NOT BUILD A NEW MODEL ON THE TEST SET! Simply use your existing, model, to predict salaries in the test set.

8. How does your model compare when running it on the test set - what is the difference in the Root Mean Square Error (RMSE) between the training and test sets? Is there any evidence of overfitting?

## References

Data is made up and inspired by Cohen, Cohen, West & Aiken. Applied Multiple Regression/Correlation Analysis for the Behavioral Sciences, 3rd Edition.