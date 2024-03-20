---
title: Skewness and Kurtosis
content_type: topic
ready: true
---

Please read through the following:

- https://www.analyticsvidhya.com/blog/2021/05/shape-of-data-skewness-and-kurtosis/
- https://www.w3schools.com/ai/ai_statistics_descriptive.asp
- https://www.analyticsvidhya.com/blog/2021/05/shape-of-data-skewness-and-kurtosis/

## Skewness and Kurtosis in Python

In order to make use of these concepts in Python, we need to make use of scipy:

- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skew.html
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kurtosis.html

Here they are in action:

```
from scipy.stats import skew, kurtosis

data = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

skewness = skew(data)
print("Skewness:", skewness)

kurtosis_value = kurtosis(data)
print("Kurtosis:", kurtosis_value)
```