---
_db_id: 236
content_type: project
flavours:
- python
learning_outcomes:
- data_sci_decision_trees
- data_sci_classification_metrics
- data_sci_sensitivity_specificity
- data_sci_confusion_matrix_classification_report
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - projects/data-science-specific/statistical-thinking
  - projects/data-science-specific/logistic-regression
  - topics/jupyter-notebooks-best-practices
  - topics/data-science-specific/data-science-methodology
ready: true
story_points: 8
submission_type: repo
tags:
- decision-trees
- sklearn
- statistics
- classification
title: Decision Trees
---

## Background material

- Walk through the [machine learning Kaggle tutorial](https://www.kaggle.com/learn/intro-to-machine-learning)
- Complete the DataCamp tutorial on [Tree-Based Models](https://www.datacamp.com/courses/machine-learning-with-tree-based-models-in-python)
  
## About the Dataset
This dataset includes descriptions of 23 species of gilled mushrooms in the Agaricus and
Lepiota Family. Each species is identified as either edible or poisonous.

## Metadata Information
The table below gives the variable names in the mushrooms data file.

| Variable                 | Description                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| classes                  | edible=e, poisonous=p                                                                                        |
| cap-shape                | bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s                                                     |
| cap-surface              | fibrous=f, grooves=g, scaly=y, smooth=s                                                                      |
| cap-color                | brown=n, buff=b, cinnamon=c, gray=g, green=r, pink=p, purple=u, red=e, white=w, yellow=y                     |
| bruises?                 | bruises=t, no=f                                                                                              |
| odor                     | almond=a, anise=l, creosote=c, fishy=y, foul=f, musty=m, none=n, pungent=p, spicy=s                          |
| gill-attachment          | attached=a, descending=d, free=f, notched=n                                                                  |
| gill-spacing             | close=c, crowded=w, distant=d                                                                                |
| gill-size                | broad=b, narrow=n                                                                                            |
| gill-color               | black=k, brown=n, buff=b, chocolate=h, gray=g, green=r, orange=o, pink=p, purple=u, red=e, white=w, yellow=y |
| stalk-shape              | enlarging=e, tapering=t                                                                                      |
| stalk-root               | bulbous=b, club=c, cup=u, equal=e, rhizomorphs=z, rooted=r, missing=?                                        |
| stalk-surface-above-ring | fibrous=f, scaly=y, silky=k, smooth=s                                                                        |
| stalk-surface-below-ring | fibrous=f, scaly=y, silky=k, smooth=s                                                                        |
| stalk-color-above-ring   | brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y                              |
| stalk-color-below-ring   | brown=n, buff=b, cinnamon=c, gray=g, orange=o, ink=p, red=e, white=w, yellow=y                               |
| veil-type                | partial=p, universal=u                                                                                       |
| veil-color               | brown=n, orange=o, white=w, yellow=y                                                                         |
| ring-number              | none=n, one=o, two=t                                                                                         |
| ring-type                | cobwebby=c, evanescent=e, flaring=f, large=l, none=n, pendant=p, sheathing=s, zone=z                         |
| spore-print-color        | black=k, brown=n, buff=b, chocolate=h, green=r, orange=o, purple=u, white=w, yellow=y                        |
| population               | abundant=a, clustered=c, numerous=n, scattered=s, several=v, solitary=y                                      |
| habitat                  | grasses=g, leaves=l, meadows=m, paths=p, urban=u, waste=w, woods=d                                           |
## Instructions:

Use a decision tree model to predict whether mushrooms are poisonous or edible.

1. Your repo should contain everything needed to replicate your work. It's good practice to structure your files well, so we'll expect you to have a separate directory for "data" and "notebook", so that your final file structure looks something like this: 

```
├──data
│  └── agaricus-lepiota.data
├──notebook
│  └── mushrooms_prediction.ipynb
├──README.md
├──requirements.txt
└──.gitignore 
```

2. Import the required libraries and load the dataset [here](agaricus-lepiota.data).
3. Split your data into train and test sets.
4. Get basic descriptive statistics for the training data and check for missing and incorrect or extreme values. Get scatterplots or heatmaps showing the relationship between the variables.
5. What are the factors(variables) that predict whether a mushroom is poisonous?
6. Build a decision tree model to predict whether mushrooms are poisonous or edible.
7. Report the accuracy of your model on the training set and on the test set. How successful is the model - what is its precision and recall?
8. What is the prevalence of poisonous mushrooms in the dataset? How might prevalence affect the positive and negative predictive values of a test/model?



## Supporting Material on decision trees

[Coursera: Decision Trees](https://www.coursera.org/lecture/python-machine-learning/decision-trees-Zj96A)