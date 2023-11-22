---
_db_id: 247
content_type: project
flavours:
- python
learning_outcomes:
- data_sci_data_processing
- data_sci_data_validation
- data_sci_pandas
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - topics/data-validation-and-quality-control
  - topics/jupyter-notebooks-best-practices
  - topics/data-ethics-and-privacy
  - projects/data-science-specific/assertive-programming-tricks-for-pandas
ready: true
story_points: 5
submission_type: repo
tags:
- data-wrangling
- jupyter-notebooks
title: Data Wrangling
---

Please make use of Jupyter notebooks while doing this project.
## Key concepts

- merging data frames
- filtering data frames
- manipulating rows and columns

## Background materials

- Pandas content - https://www.youtube.com/watch?v=tRKeLrwfUgU&ab_channel=NicholasRenotte 
- Intro to pandas and data manipulation [here](https://www.kaggle.com/learn/pandas)
- https://towardsdatascience.com/data-wrangling-with-pandas-5b0be151df4e
- https://towardsdatascience.com/7-must-know-data-wrangling-operations-with-python-pandas-849438a90d15
- How to handle missing data - https://towardsdatascience.com/7-ways-to-handle-missing-values-in-machine-learning-1a6326adf79e
- If you'd like more, complete the DataCamp skills track [Data Manipulation with Python](https://www.datacamp.com/tracks/data-manipulation-with-python)

## About the dataset and assignment

This data contains [personality scores](personality_scores.csv) for learners, plus the [department](departments.csv) they applied for.

### Prerequisites

You should be able to write basic functions and for loops for this assignment. You should also be familiar with merging, filtering and creating new columns in pandas.

_Optional:_
As far as possible, use functional programming techniques (map, reduce, apply) instead of loops when writing the functions below.

For example, to modify every column in a data frame (to get a percentage in this case), instead of writing:

```
for column in df:
  column = column/10*100 #get percentage
```

use:

```
def get_percentage(score):
  score/10*100

df.apply(get_percentage, axis = 1) #axis=1 applies the function to all columns
```

### Instructions

1. Your repo should contain everything needed to replicate your work. It's good practice to structure your files well, so we'll expect you to have a separate directory for "data" and "notebook", so that your final file structure looks something like this: 

```
├──data
│   ├──departments.csv
│   └──personality_scores.csv 
├──notebook
│  └──data_wrangling.ipynb
├──README.md
├──requirements.txt
└──.gitignore 
```
2. Import the dataset [personality_scores.csv](personality_scores.csv) and load it into a DataFrame. Examine the DataFrame for duplicates (based on ID), and drop any duplicates that exist. Let's imagine that the data is ordered chronologically, and we'd like to keep the data related to the most recent time an applicant did the test. From your recent project on [assertive programing tricks](projects/data-science-specific/assertive-programming-tricks-for-pandas/_index.md) use the methods you practiced to check that the updated DataFrame has the dimensions you expect it to have. Perform some final cleaning steps by removing empty columns and cleaning up column names. Store this updated version of the DataFrame in a variable called: `personality_score_df`.


3. Creat a function (or functions) to support creating new columns containing the total score of each of the personality test subscales. The new columns should be named as per the **big five personality traits** laid out in [scoring](scoring.txt). In other words, for the **conscientiousness** total score, all items marked as belonging to 'conscientiousness' should be summed.

The new data frame will look something like this and it should be named `personality_score_totals_df`:

| I am always prepared | I am easily disturbed | I am exacting (demanding) in my work | ... | Conscientiousness | Neuroticism |
| -------------------- | --------------------- | ------------------------------------ | --- | ----------------- | ------------------- |
| (3, 5)               | (4, 5)                | (3, 5)                               | ... | 10                | 5                   |
| (3, 5)               | (4, 1)                | (3, 1)                               | ... | 6                 | 1                   |
| (3, 5)               | (4, 3)                | (3, 3)                               | ... | 8                 | 3                   |

4. Import the data in [departments.csv](departments.csv) and store it in a DataFrame. Merge this DataFrame with the personality score totals DataFrame. Again, use assertion techniques from [assertive programing tricks](projects/data-science-specific/assertive-programming-tricks-for-pandas/_index.md) to check that the newly created merged DataFrame has the expected number of rows and columns. The merged DataFrame should be named `merged_personality_department_df`

5. Filter the merged DataFrame so that you only see the applicants who scored less than 30 on emotional stability, conscientiousness AND agreeableness. Next, assign these applicants the tag "High risk" in a new column called `Risk Status`. All other applicants get the tag "Low risk". The DataFrame here should be named `risk_status_df`.

6. Wrangle a new DataFrame with a count of the number of low and high risk applicants within each department. Let each department be a separate column. This new DataFrame should be named `risk_status_summary_df`. If there are no learners in one of the categories, it should be represented by zero and not a null entry. The DataFrame should look something like this:

| Risk Status  | Copywriting | Data | Design | Strategy  |  Web Dev |
| ------------ | ----------  | ---- | ------ | -------   | -------- |
| Low risk     | 150         | 123  | 0      | 4         | 6        |
| High risk    | 40          | 0    | 22     | 67        | 9        |
