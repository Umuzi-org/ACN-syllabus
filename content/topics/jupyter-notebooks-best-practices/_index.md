---
_db_id: 51
content_type: topic
ready: true
title: Jupyter notebooks best practices
---

## Why use a notebook?

### Working alone

- Keep track of your thoughts.
- Make sketch notes.
- Add links to resources to review later.
- Example notebook: https://danielfrg.com/blog/2013/03/kaggle-bulldozers-basic-cleaning/.

### Working in a team

- For code review.
- For colleagues to contribute to your notebook.
- To write a report on your models.
- As a tutorial guide.
- To communicate with external clients/entities/blog.
- Notebook example:
  - https://www.kaggle.com/burhanykiyakoglu/predicting-house-prices

## Tips for effective and efficient use of (jupyter) notebooks for data science projects

### Follow standard coding practices:

- Provide comments and documentation to your code.
- Stick to a consistent naming scheme! Use meaningful names: answers_to_score is clearer than score_ans, which is clearer than score_1!
- Group code in a manner that allows anyone to follow the modelling process, for example: data exploration (summary statistics, distributions, bar graphs, scatter plots), data transformation (outlier detection, counting & dropping/replacing NaN, renaming columns/rows etc), modelling and model evaluations (model scores and error)
- Limit length of code lines.
- Refactor (restructuring) code whenever necessary to keep it simple.

## Make it easy for others to follow and improve your work

- Have an author name and contact details in case someone wants to ask for clarity.
- The notebook should be a standalone document that does not require someone to have to know about the problem being solved or in-depth knowledge of the algorithms. This will help others follow your thought processes and understand the data transformation/data analysis being done and why certain techniques are being used, since multiple techniques exist.
- Tell the story: describe the problem being solved and how the model will solve that problem.
- Summarise the data's statistical characteristics (to show that your data cleaning will not introduce artefacts or new features, and to show that the data is appropriate for the model(s) you use). This includes showing the variables' distribution and central tendency, as well as the amount of available data.
- Exploratory techniques for summarising data should be used before you start formal modelling and can help the development of more complex statistical models and to eliminate or sharpen potential hypotheses about the world that can be addressed by the data. You will almost always want to see graphs of variable distributions, relationships between variables and missing data patterns.
- Provide enough rationale for each coding task being carried out (you will find this information useful when you read your own notebooks later).
- Critique your own model, this will help pre-empt and address shortcomings of your model and avoid loss of confidence in your model by others.

### General tips

- Keep cells of your notebook simple: don't exceed the width of your cell.
- Make sure that you don't put too many unrelated functions in one cell.
- It's neater to import all packages in the first code cell of your notebook.
- Ensure graphics can display inline (use matplotlib inline magic commands & semicolons).