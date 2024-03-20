---
title: Descriptive statistics in Python
content_type: topic 
ready: true
---

Python has a bit of functionality built in that you can use when calculating different measures of central tendency. 

Open up a Python shell or a Notebook and try this out for yourself:

First, import the statistics library so you can make use if it's functionality. 

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

Try to play around with this a little bit. 

- if you change the numbers in `data` then does `mean_value` change? Or do you need to do something to get it to calculate again?
- can you tell if the list of numbers is skew or not? How can you tell?
- does the data have a mode? Can you come up with a dataset that has a mode? And one that does not?


