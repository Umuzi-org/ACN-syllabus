---
_db_id: 236
available_flavours:
- python
content_type: project
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - projects/data-science-specific/statistical-thinking
  - projects/data-science-specific/data-visualisation
  - projects/data-science-specific/logistic-regression
  soft:
  - topics/python-self-learning
  - topics/jupyter-notebooks-best-practices
  - topics/data-science-specific/data-science-methodology
ready: true
story_points: 8
submission_type: repo
tags:
- decision-trees
title: Decision Trees
---

## Background material

- Walk through the [machine learning Kaggle tutorial](https://www.kaggle.com/learn/intro-to-machine-learning)
- Complete the DataCamp tutorial on [Tree-Based Models](https://www.datacamp.com/courses/machine-learning-with-tree-based-models-in-python)

## Assignment

Use a decision tree model to predict whether mushrooms are poisonous or edible.

1. Split your data into train and test sets.
2. Get basic descriptive statistics for the training data and check for missing and incorrect or extreme values. Get scatterplots or heatmaps showing the relationship between the variables.
3. What are the factors that predict whether a mushroom is poisonous?
4. Report the accuracy of your model on the training set and on the test set. How successful is the model - what is its precision and recall?
5. What is the prevalence of poisonous mushrooms in the dataset? How might prevalence affect the positive and negative predictive values of a test/model?

Find the data [here](agaricus-lepiota.data).

## More information on decision trees

[Coursera: Decision Trees](https://www.coursera.org/lecture/python-machine-learning/decision-trees-Zj96A)

## Description of the dataset

This dataset includes descriptions of 23 species of gilled mushrooms in the Agaricus and
Lepiota Family. Each species is identified as either edible or poisonous.

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