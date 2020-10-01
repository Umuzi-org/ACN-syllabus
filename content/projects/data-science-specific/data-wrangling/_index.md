---
_db_id: 247
available_flavours:
- python
content_type: project
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - topics/data-validation-and-quality-control
  - topics/jupyter-notebooks-best-practices
  - topics/python-self-learning
  soft:
  - topics/data-ethics-and-privacy
  - projects/tdd/simple-calculator-part1
ready: true
story_points: 5
submission_type: repo
tags:
- data-wrangling
title: Data Wrangling
---

## Key concepts

- merging data frames
- filtering data frames
- manipulating rows and columns

## Tutorials

- Intro to pandas and data manipulation [here](https://www.kaggle.com/learn/pandas)
- If you'd like more, complete the DataCamp skills track [Data Manipulation with Python](https://www.datacamp.com/tracks/data-manipulation-with-python)

## Assignment

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

This data contains [personality scores](personality_scores.csv) for recruits, plus the [department](departments.csv) they applied for.

1. Import the dataset [personality_scores.csv](personality_scores.csv). Examine the data frame for duplicates (based on ID), and drop any duplicates that exist. Use an assert statement to check that the new data frame is the length of the unique entries of the original data frame.

Tip: An example assert statement is `assert 2*20=40` and it's a great way to check that your modification of the data was successful.

2. Create new columns containing the total score of each of the personality test subscales. To do this, write a function (or functions) that will calculate the total score for each of the subscales (conscientiousness, emotional stability, openness to new experience, agreeableness, extraversion), as set out in [scoring](scoring.txt). In other words, for the conscientiousness total score, all items marked as belonging to 'conscientiousness' should be summed.

The new data frame will look something like this:

| I am always prepared | I am easily disturbed | I am exacting (demanding) in my work | ... | Conscientiousness | Emotional Stability |
| -------------------- | --------------------- | ------------------------------------ | --- | ----------------- | ------------------- |
| (3, 5)               | (4, 5)                | (3, 5)                               | ... | 10                | 5                   |
| (3, 5)               | (4, 1)                | (3, 1)                               | ... | 6                 | 1                   |
| (3, 5)               | (4, 3)                | (3, 3)                               | ... | 8                 | 3                   |

3. Import the data in [departments.csv](departments.csv). Merge this data frame with the personality score data frame, keeping all applicants within the department data frame. Use an assert statement to check that the newly created merged data frame has the same amount of rows as the department data frame, and the expected number of columns.

4. Filter the merged data frame so that you get only the applicants who scored less than 30 on emotional stability, conscientiousness AND agreeableness. Print the ID numbers and departments of these applicants to the screen, and also assign these applicants the tag "high_risk" in a new column. All other applicants get the tag "low_risk"

5. Create a new data frame with a count of the number of low and high risk applicants within each department. Let each department be a separate column. In other words, the data frame should look something like this:

| Risk      | Multimedia | Coding | Data |
| --------- | ---------- | ------ | ---- |
| Low risk  | 150        | 123    | 239  |
| High risk | 40         | 15     | 22   |