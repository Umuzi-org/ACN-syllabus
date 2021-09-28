---
_db_id: 710
content_type: topic
title: 'Assessment: Basic data analysis'
topic_needs_review: true
---

All students must understand all of the following concepts:

- Statistical concepts:  Mean, Median and Mode
- Statistical concept:  IQR (Interquartile range)
- Statistical concepts:  Standard deviation and Variance
- Statistical concepts:  Correlation and p-value (Probability value) and Null-hypothesis vs. Alternative-hypothesis
- Statistical concepts:  Standard deviation and Standard error

### Statistical concepts: Mean, Median and Mode

#### Mean (Average value):
```
Calculating the mean (average value):

list_of_speed_data = [87, 94, 78, 77, 85, 86]

mean = (87+94+78+77+85+86) = 507/6 = 84.5
```


#### Median (Middle value):
```
Calculating the median (middle value):

list_of_speed_data = [100, 200, 300, 400, 500, 600]

When we have an even amount of numbers we need to calculate the mean (average) of the two middle 
numbers, in this case 300 and 400.  So the mean (average) of 300 and 400 is (300+400)/2 = 350.
Therefore the mean (middle) value is:  median = 350


When we have an odd amount of numbers we need to divide the total amount of numbers by 2 and then
round up to the nearest integer.  For instance:

list_of_speed_data = [100, 200, 300, 400, 500, 600, 700]

There are seven numbers in the list, 7/2 = 3.5, if we round up to the nearest integer we get 4.  
Therefore, the 4th number in the list will be the median (middle) value:  median = 400
```


#### Mode (Most frequent value):
```
The mode is the value which occurs the most in a set.  So if you had a set [2, 2, 2, 3] then the
mode would be 2 since 2 is the value which occurs most frequently in the set.
```



### Statistical concepts: Interquartile range (IQR)
1st quartile:  Middle number between the smallest number and the median of the dataset

2nd quartile:  Equal to the median of the dataset

3rd quartile:  Middle number between the median and the largest value of the dataset



### Statistical concepts: Standard deviation and Variance
Standard deviation and variance are both determined by using the mean of the dataset.  Variance measures the average degree to which each number is different from the mean.  Standard deviation is a statistic that looks at how far from the mean a group of numbers is, by using the square root of the variance.  Standard deviation is similar to variance, which gives the measure of deviation whereas variance provides the value squared.

```
Formula for standard deviation:  square root of [(1/N)*Sigma i=1 to N of (x - u)^2 ]
sample_data = [9, 2, 5, 4, 12, 7, 8, 11]

Step 1: Calculate the Mean (average value) = (9+2+5+4+12+7+8+11)/8 = 7.25

Step 2:  For each number in sample_date, subtract the mean from the number and square the result

(9-7.25)^2 = 3.06
(2-7.25)^2 = 27.56
(5-7.25)^2 = 5.06
(4-7.25)^2 = 10.56
(12-7.25)^2 = 22.56
(7-7.25)^2 = 0.06
(8-7.25)^2 = 0.56
(11-7.25)^2 = 14.06

[3.06, 27.56, 5.06, 10.56, 22.56, 0.06, 0.56, 14.06]

Step 3:  Calculate the mean of all the numbers squared you calculated in step 2.  It is important to notice
         that once you have calculated step 3 you already have the Variance, the calculation done in step 4
         will simply give you the standard deviation.

(3.06+27.56+5.06+10.56+22.56+0.06+0.56+14.06)/8 = 10.435 (This is the variance)

Step 4:  Take the square root of step 3 and you are done

Square root of 10.435 = 3.23
```



### Statistical concepts: Correlation and p-value (Probability value)
A correlation coefficient is represented in Python by the variable R, the value ranges between -1 and 1.  A correlation coefficient of -1 (Negative slope) or +1 (Positive slope) illustrates a perfect linear relationship between dependant and independent variables, a correlation coefficient of 0 indicates NO linear relationship between dependant and independent variables.

P-values, a.k.a. probability values are exactly that, if you wanted to know what the probability is that you would throw a 2 on a 6-sided die then you could calculate it like this: 2/6 = 0,333. So in English we would say you have a two in six chance of landing on a 6 and this equates to a 33,33% probability.

Now suppose we have a hypothesis, we hypothesize that we have a fair coin, that is, no matter how much we flip this coin the probability of it landing on the one side is equal to it landing on the other side.  We shall call this hypothesis of ours the “null-hypothesis”.  If we were to reject our own hypothesis then we would have to have some evidence to do so and we would then also have to accept another hypothesis, this other hypothesis would be that the coin is not a fair coin, we shall call this other hypothesis the alternative hypothesis.  Lets summarize what we have below:
```
Null hypothesis:  We have a fair coin

Alternative hypothesis: We don’t have a fair coin, it is rigged
```


Ok, now we start flipping this coin and we record what we land on, here is what we’ve found:
```
1st flip:  Heads – Chances of this happening is ½ = 50%
2nd flip:  Heads – Chances of this happening is ¼ = 25%
3rd flip:  Heads – Chances of this happening is 1/8 = 12,5%
4th flip:  Heads – Chances of this happening is 1/16 = 6,25%
.
.
.
100th flip:  Heads – Chances of this happening is 1/2^n = 7,886 x 10^-31
```

By about the 4th flip you should begin to see that something strange is going on, how is it that we keep on landing on Heads?  Eventually, after the 100th throw we see that the probability of this happening is something stupendously small.  So in order for us not to always have to go through all this business of simulating something over and over again we came up with a threshold value and it is 0,05.  If you see that your probability value is less than or equal to 0,05 then you can reject your Null hypothesis and accept the alternative hypothesis.  In our case our p-value is clearly smaller than 0,05 so we reject our null hypothesis and accept our alternative hypothesis that this coin which we have been tossing is not a fair coin at all, it is rigged.



### Statistical concepts: Standard Deviation and Standard Error
Imagine we measure the weights of five people, their weights were as follows:
```
Person 1:  50kg
Person 2:  80kg
Person 3:  70kg
Person 4:  60kg
Person 5:  90kg

The average(mean) weight would be:  (50+80+70+60+90)/5 = 70kg

Standard deviation would refer to how far the individual mass of each person is from this mean amount.  For instance Person 1 weighs 50kg so he/she is 20kg away from the mean.  Person 4 weighs 60kg so Person 4 is a lot closer to the mean.  So in summary, standard deviation is a measure of how spread out data is, ergo, how far a specific data point is from the mean.
```

Now imagine we do this experiment five times over and each time with five new people.  So then in total you would have five individual means (averages) just like the one we calculated above.  In each experiment we would also have a standard deviation for that experiment.  Suppose now the means for the five experiments were as follows:
```
Experiment 1:  70kg
Experiment 2:  60kg
Experiment 3:  70kg
Experiment 4:  70kg
Experiment 5:  80kg


So then if we calculate a mean of the means it would be:  (70+60+70+70+80)/5 = 70kg
```
From here we can form an idea of the standard deviation each mean has from the ‘mean-of-the-means’.  So for instance, in experiment 1 the mean was 70kg so it’s mean is right on top of the ‘mean-of-the-means’.  Experiment 5 on the other hand is 10kg’s away from the ‘mean-of-the-means’.  This standard deviation from the ‘mean-of-the-means’ is actually referred to as the Standard Error.  If you had a single set of measurements, ergo, not five experiments but just one and you were asked to plot the standard error what would you plot?  Simply plot the standard deviation, seeing that the standard error refers to a kind of ‘standard deviation’ but it actually applies to the ‘standard deviation’ of means to the ‘mean-of-the-means’, within the context of a single experiment the standard error would then be the standard deviation of the mean.