---
title: Descriptive statistics
content_type: topic
---


## Measures of Central Tendency:

### Mean

The average of a set of values, calculated by summing all values and dividing by the number of observations. Or The mean, also known as the arithmetic average, is likely the measure of central tendency you are most acquainted with. Computing the mean is straightforward – you sum up all the values and then divide by the total number of observations in your dataset. Formula for calculating mean is: 

```
x1+x2+x3…+xn / n 
```

x1 to xn represent individual values, and n denotes the total number of values in your dataset.

![Mean](mean_symmetric.png)

The computation of the mean involves the consideration of all values within the dataset. Altering any value leads to a change in the mean. However, it's important to note that the mean may not consistently pinpoint the precise center of the data. The histograms below illustrate instances where we showcase the mean within the distributions, emphasizing its potential limitations in accurately representing the central tendency.

As shown above in the graph, In a distribution that is symmetric, the mean accurately identifies the central point.

![Distributions](distribution_central_tendency.png)

In a [skewed distribution](https://www.statisticshowto.com/probability-and-statistics/skewed-distribution/), the mean may deviate from accuracy. As evident in the provided histogram, it begins to shift outside the central region. This discrepancy arises due to the significant influence of outliers on the mean as a measure of central tendency. [Outliers](https://www.statisticshowto.com/statistics-basics/find-outliers/), particularly those in an elongated tail, exert a notable pull on the mean, causing it to shift away from the center. As the distribution exhibits more skewness, the mean becomes further displaced from the central position. Consequently, opting for the mean as a measure of central tendency is most advisable when dealing with a symmetric distribution. Further insights into this matter will be explored in the discussion comparing mean versus median. **When do we use mean,Use mean for symmetric and continuous data.**

### Median

The middle value in a dataset when it is ordered, separating the higher half from the lower half. This is not affected by the extreme or outliers in the dataset. 

To determine the median, arrange your data in ascending order, and identify the data point that possesses an equal count of values both above and below it. The approach for pinpointing the median differs slightly based on whether your dataset contains an even or odd number of values. I will guide you through finding the median for both scenarios. While I utilize whole numbers in the examples below for simplicity, it's important to note that your dataset may include decimal places.
In the dataset featuring an odd number of observations, observe how the number 11 stands in the middle, with six values left and right of it. Consequently, 11 serves as the median for this dataset.

1,10,13,5,8,7,**11**,9,10,12,13,8,3

In instances where there is an even number of values, you count inward to the two middlemost values and subsequently calculate their average. For example, in the dataset with values 11 and 13, their average (12) becomes the median for this particular dataset.

1,10,13,5,8,7,   **11, 13**,  9,10,12,13,8,3

**Note:** The impact of outliers and skewed data on the median is less pronounced compared to the mean as measures of central tendency.	

#### When to use median : Skewed distributions, Continuous data, Ordinal data

Read the below article if you want to take a deep dive when you should use means median.

[Use of mean vs median](https://www.statology.org/when-to-use-mean-vs-median/)

### Mode

The most frequently occurring value in a dataset. Or The mode, unlike the mean or median, is the value that appears most frequently in your dataset. To determine the mode, arrange your dataset in ascending order for numeric values or by categories, and then identify the value with the highest frequency.

## Which Central Tendency Measure — Mean, Median, or Mode — Is the Most Suitable?

In the presence of a symmetrical distribution in continuous data, the mean, median, and mode coincide. Analysts typically prefer using the mean in such scenarios as it considers all data points in its calculations. Conversely, in a skewed distribution, the median often emerges as the most suitable measure of central tendency.

For ordinal data, the median or mode is generally the preferable choice. In the case of categorical data, the mode is the mandatory selection.

Read the below article to take a deep dive when you should use mean vs median.

[Use of mean vs median](https://www.statology.org/when-to-use-mean-vs-median/)