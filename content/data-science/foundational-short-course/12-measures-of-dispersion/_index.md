---
title: Measures of Dispersion
content_type: topic
ready: true
---

Please read through the following article:

https://www.knowledgehut.com/blog/data-science/dispersion-in-statistics

Make sure you are able to understand what the following terms mean:

- Range
- Variance 
- Standard deviation

## Self Assess

Can you answer the following questions?

1. Which measure of dispersion provides information about the spread of data around the mean?
2. How is variance related to standard deviation?

## Python

Open up a python shell or notebook and play with these ideas a bit.

Try this out:

```
scores = [85, 90, 78, 92, 88, 95, 80, 87, 94, 89]

# Calculate measures of dispersion
range_score = max(scores) - min(scores)
variance_score = statistics.variance(scores)
std_dev_score = statistics.stdev(scores)

# Display measures of dispersion
print(f"Range of Scores: {range_score}")
print(f"Variance of Scores: {variance_score}")
print(f"Standard Deviation of Scores: {std_dev_score}")
```

For this code to function, you must import the statistics package. 
Can you recall how to do this?





