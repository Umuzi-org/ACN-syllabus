---
_db_id: 148
content_type: topic
ready: true
title: K-Means Clustering
---

There are many different clustering algorithms to cluster, or group, objects based on how similar (or close in terms of distance) their attributes are.

We will look at just one type of clustering, K-Means clustering, but many other types exist.
You can read more about other methods of clustering [here](https://scikit-learn.org/stable/modules/clustering.html).

## Introduction
K-Means clustering is an unsupervised learning technique used in processes such as market segmentation,
document clustering, image segmentation and image compression.

Usually we do K-Means clustering to:

- Understand the structure of the data, and group similar observations.
- Cluster the data into subgroups and then do different predictions on the different subgroups.

If we think that subgroup behaviours differ substantially, then we will get more accurate models
by making separate models for each subgroup, than one model for all groups.


## Tutorials

### Guided tutorials

- [K-Means Clustering in Depth](https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html)
- [EDA and K-Means Example](https://www.kaggle.com/thebrownviking20/in-depth-eda-and-k-means-clustering)
- [K-Means Clustering: Algorithm, Applications, Evaluation Methods, and Drawbacks](https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a)


### Unguided tutorial: Flower features

This tutorial is not compulsory, but you can go through it on your own for a gentle introduction to clustering.
It is easier than the clustering assignment given in Projects.

Data: [Iris species](https://www.kaggle.com/shrutimechlearn/classification-with-iris-dataset/data)

1. Use K-Means cluster analysis to cluster different iris species.
Make an elbow plot and/or use silhouette analysis to find the optimal number of clusters.

2. What are the factors that differ between different iris species?

3. Create a plot of the clusters.