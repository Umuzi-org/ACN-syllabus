---
title: Descriptive statistics in Python
content_type: topic 
ready: true
---

Python comes equipped with built-in capabilities that are useful for calculating various measures of central tendency.

To explore this yourself, open a Python shell or a Jupyter Notebook.

Start by importing the statistics library to access its features.


```
import statistics
```

Next, create a list of numbers.

```
data = [8, 15, 13, 20, 17, 15, 21, 23, 18, 20]
```

You can now calculate the mean, median and mode of the data:

```
mean_value = statistics.mean(data)
print(f"Mean: {mean_value}")

median_value = statistics.median(data)
print(f"Median: {median_value}")

try:
    mode_value = statistics.mode(data)
    print(f"Mode: {mode_value}")
except statistics.StatisticsError:
    print("Mode: No unique mode in the dataset.")
```

Experiment with this a bit:

- If you alter the numbers in `data` then does `mean_value` change? Or do you need to take additional steps to recalculate it?
- Can you determine if your dataset is skewed or not? What clues indicate skewness?
- Does your data have a mode? Try to create a dataset that has a mode and another that doesn't. How do you identify if a mode exists?


