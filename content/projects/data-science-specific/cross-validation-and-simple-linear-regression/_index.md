---
_db_id: 234
content_type: project
flavours:
- python
learning_outcomes:
- data_sci_eda
- data_sci_cross_validation
- data_sci_handle_categorical_variables
- data_sci_justify_feature_selection
- data_sci_linear_model_evaluation
- data_sci_linear_model_summary
- data_sci_linear_model_overfitting
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - projects/data-science-specific/statistical-thinking
  - projects/data-science-specific/data-visualisation/mobile-money-viz
  - topics/data-science-specific/data-science-methodology
  - topics/data-science-specific/regression
ready: true
story_points: 13
submission_type: repo
tags:
- linear-regression
- statistics
- data-analysis
title: Cross-validation & Simple Linear Regression
---

## Key topics

- Simple linear regression
- Residuals
- Overfitting and underfitting
- Cross-validation
- Root Mean Square Error

## About the dataset and assignment

Data is made up and inspired by Cohen, Cohen, West & Aiken. Applied Multiple Regression/Correlation Analysis for the Behavioral Sciences, 3rd Edition. We will predict employee salaries from different employee characteristics (or features).
We are going to use a simple supervised learning technique: linear regression. We want to build a simple model to determine how well Years Worked predicts an employee’s salary.

### Instructions

1. Your repo should contain everything needed to replicate your work. It's good practice to structure your files well, so we'll expect you to have a separate directory for "data" and "notebook", so that your final file structure looks something like this: 

```
├──data
│   ├──salary.csv
│   └──Salary metadata.csv 
├──notebook
│  └──salaries_predictions.ipynb
├──README.md
├──requirements.txt
└──.gitignore 
```
2. Import the data [salary.csv](salary.csv) to a Jupyter Notebook. A description of the variables is given in [Salary Metadata](Salary metadata.csv). You will need the packages `matplotlib`, `pandas` and `statsmodels`.
   
3. Split your data into a training and test set. Leave the test set for now. Examine the training data for missing and extreme values. Create different histograms to show the distribution of each variable in your dataset. Create a scatterplot showing the relationship between Years Worked and Salary. Are the data appropriate for linear regression? Is there anything that needs to be transformed or edited first?

4. Using the ``statsmodels`` package and the _training data_, run a simple linear regression for Salary with one predictor variable: Years Worked.
   - Does the model significantly predict the dependent variable? Report the amount of variance explained (R^2) and significance value (p) to support your answer.
   - What percentage of the variance in employees’ salaries is accounted for by the number of years they have worked?

5. What does the unstandardised coefficient (B or 'coef' in `statsmodels`) tell you about the relationship between Years Worked and Salary?

6. What do the 95% confidence intervals [0.025, 0.975] mean?

7. Calculate the expected salary for someone with 12 years’ work experience.

8. Calculate the expected salary for someone with 80 years’ work experience. Are there any problems with this prediction? If so, what are they?

9. Now fit your model to your test set. DO NOT BUILD A NEW MODEL ON THE TEST SET! Simply use your existing, model, to predict salaries in the test set.

10. How does your model compare when running it on the test set? - what is the difference in the Root Mean Square Error (RMSE) between the training and test sets? Is there any evidence of overfitting?

11. We have only looked at the number of years an employee has worked. What other employee characteristics might influence their salary? Please justify your answer using the data

## Instructions for reviewer

1. Make sure the amount of variance explained and its statistical significance are correctly interpreted. Simply computing these values is not sufficient, the student needs to demonstrate understanding.

2. Note that `statsmodel` suppresses the constant term unless it's added or (you use the formula notation). If the model is built without a constant term, this should be justified. If a constant term is added, it should also be explained why this is necessary.

3. When fitting the model to the test data, make sure that a new model isn't being built. There should only be one model in the notebook.

4. A common mistake is misinterpreting the condition for overfitting using the RMSE criterion. Pay attention to which is higher/lower and whether this has been interrupted correctly.
