---
_db_id: 112
content_type: project
flavours:
- python
prerequisites:
  hard:
  - content/data_science/3_introduction_to_statistics/measures_of_central_tendency_questions
  soft: []
protect_main_branch: false
ready: true
submission_type: repo
title: Measures of Central Tendency - Project
---


## Instructions

We will not only be assessing your code but also how you structure and present your analysis.This [notebook](notebook.ipynb) has a guide to the general structure we expect.

Your repo should contain everything needed to replicate your work. It's good practice to structure your files well, so we'll expect you to have a separate directory for "notebook", so that your final file structure looks something like this:

├──notebook
│  └── central_tendency_notebook.ipynb
├──README.md
├──requirements.txt
└──.gitignore 

## Instructions
Imagine you have a dataset representing the scores of students in a class. The assignment is to calculate and present key measures of central tendency. 

- Open the central_tendency_notebook notebook you created.
- Declare the dataset for scores using the below list.
```
scores = [80, 60, 78, 79, 48, 95, 90, 87, 100, 89]
```
- Compute and present the Mean, Mode, and Median of the provided scores.

## Instructions for reviewer
- The learner should organize their code into Jupyter notebook cells 
- The learner should include Markdown cells for explanations, analysis, and reflections.
- Ensure that the notebook has an introduction at the beginning, explanations for every answered question, and a conclusion at the end.
- The learner should not use external libraries like the statistics or numpy module for their calculations. Their calculations should be done using python

External Resources:
Please review below link to take deep dive inside it:

https://statisticsbyjim.com/basics/measures-central-tendency-mean-median-mode/
