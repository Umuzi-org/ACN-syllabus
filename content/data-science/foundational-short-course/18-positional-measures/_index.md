---
title: Positional measures
content_type: topic
ready: true
---

Please read the following articles:

- https://www.w3schools.com/statistics/statistics_quartiles_and_percentiles.php
- https://www.simplilearn.com/tutorials/data-analytics-tutorial/percentile-in-statistics#:~:text=In%20statistics%2C%20a%20percentile%20is,fall%20below%20a%20given%20value.
- https://byjus.com/maths/quartiles/


**Percentiles**: Percentiles provide a means to characterize the relative position of a specific value within a dataset. The p’th percentile signifies the threshold below which p percent of the data points reside. For instance, the median corresponds to the 50th percentile as it partitions the dataset into two equal halves, with 50% of the observations falling below this central point.

**Quartiles**: Quartiles segment a dataset into four portions, each encompassing around 25% of the dataset. The trio of quartiles is designated as follows: the first quartile (Q1) aligns with the 25th percentile, the second quartile (Q2) corresponds to the 50th percentile (also recognized as the median), and the third quartile (Q3) is linked to the 75th percentile.

## Check your own understanding 

1. What does the 50th percentile represent in a dataset?
- The first quartile
- The median
- The third quartile
- The mean

2. If a data point is in the 75th percentile, what does this imply?
- It is above the median
- It is below the median
- It is in the third quartile
- It is in the first quartile

## Positional measures in Python

Open up a Python shell or notebook and play with this:

```
import numpy as np

# Example dataset
sample_data = np.array([10, 15, 18, 20, 20, 25, 28, 34, 35, 40])

# Calculating Percentiles
percentile_25 = np.percentile(sample_data, 25)
percentile_50 = np.percentile(sample_data, 50)  # Same as the median
percentile_75 = np.percentile(sample_data, 75)

print(f"25th Percentile (Q1): {percentile_25}")
print(f"50th Percentile (Median, Q2): {percentile_50}")
print(f"75th Percentile (Q3): {percentile_75}")

# Calculating Quartiles
quartiles = np.percentile(sample_data, [25, 50, 75])
Q1, Q2, Q3 = quartiles

print(f"First Quartile (Q1): {Q1}")
print(f"Second Quartile (Median, Q2): {Q2}")
print(f"Third Quartile (Q3): {Q3}")
```