---
_db_id: 235
content_type: project
flavours:
- python
learning_outcomes:
- data_sci_unsupervised_learning
- data_sci_k_means
- data_sci_cluster_optimisation
- data_sci_cluster_metrics
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - projects/data-science-specific/statistical-thinking
  - projects/data-science-specific/logistic-regression
  - topics/data-science-specific/clustering
  - topics/jupyter-notebooks-best-practices
  - topics/data-science-specific/data-science-methodology
ready: true
story_points: 8
submission_type: repo
tags:
- kmeans
- sklearn
- clustering
title: K-Means Clustering Assignment
---

## Pre-requisites

Read through the K-Means Tutorials at [content link](http://syllabus.africacode.net/topics/data-science-specific/clustering/) before starting this project.

## About the DataSet

Goal: Clustering whisky distilleries according to tasting Profiles

Download the dataset: [Whisky Tasting Profiles](whisky.csv)

## Instructions

1. Use K-Means clustering to cluster whisky distilleries by their tasting profile. Use the elbow or silhouette method to find the optimal number of clusters.

2. To see how successful clustering was, report relevant metrics (e.g. silhouette, adjusted rand index, etc.) and create a plot showing the different distilleries, their classes according to the k-Means clustering, and the distance between points. You can use `sklearn.manifold` to get Euclidean distances between points.

3. Describe the main differences between the cluster - what are the factors that differ between classes?

## Supporting Material
1. https://www.analyticsvidhya.com/blog/2016/11/an-introduction-to-clustering-and-different-methods-of-clustering/
2. https://adithsreeram.medium.com/the-best-beginners-guide-on-k-means-clustering-f3001cd27c8
