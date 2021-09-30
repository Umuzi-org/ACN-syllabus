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
- Questions:  Ten statistical type questions

### Statistical concepts: Mean, Median and Mode

#### Mean (Average value):
Calculating the mean (average value), simply add up all the values and divide the result by how many values there are:

list_of_speed_data = [87, 94, 78, 77, 85, 86]

mean = ?



#### Median (Middle value):
Calculating the median (middle value):

list_of_speed_data = [100, 200, 300, 400, 500, 600]

For an even amount of numbers the median is the average of the middle two numbers. In this case 300 and 400.  
Therefore median = (300+400)/2 = 350.


For an odd amount of numbers we need to divide the total amount of numbers by 2 and then
round up to the nearest integer.  For instance:

list_of_speed_data = [100, 200, 300, 400, 500, 600, 700]

Seven numbers in the list, 7/2 = 3.5, if we round up to the nearest integer we get 4.  
Therefore the median is the 4th number in the list = 400



#### Mode (Most frequent value):
The mode is the value which occurs the most in a set.  So if you had a set [2, 2, 2, 3] 
then the mode would be 2.



### Statistical concepts: Interquartile range (IQR)
1st quartile:  Middle number between the smallest number and the median of the dataset

2nd quartile:  Equal to the median of the dataset

3rd quartile:  Middle number between the median and the largest value of the dataset



### Statistical concepts: Standard deviation and Variance
Standard deviation and variance are both determined by using the mean of the dataset.  Variance measures the average degree to which each number is different from the mean.  Standard deviation is a statistic that looks at how far from the mean a group of numbers is, by using the square root of the variance.  Standard deviation is similar to variance, which gives the measure of deviation whereas variance provides the value squared.

sample_data = [9, 2, 5, 4, 12, 7, 8, 11]

Step 1: Calculate the Mean = 7.25

Step 2:  For each number in sample_date, subtract the mean from the number and square the result

(9 - 7.25)^2 = 3.06

(2 - 7.25)^2 = 27.56

etc.

result of step 2 = [3.06, 27.56, 5.06, 10.56, 22.56, 0.06, 0.56, 14.06]

Step 3:  Calculate the mean of all the numbers squared you calculated in step 2.  Notice that
         once you have calculated step 3 you already have the Variance, the calculation done in step 4
         will give you the standard deviation.

Mean of the result in step 2 = 10.435 (This is the variance)

Step 4:  Take the square root of step 3 and you are done

Square root of 10.435 = 3.23



### Statistical concepts: Correlation and p-value (Probability value)
A correlation coefficient is represented in Python by the variable R, the value ranges between -1 and 1.  A correlation coefficient of -1 (Negative slope) or +1 (Positive slope) illustrates a perfect linear relationship between dependant and independent variables, a correlation coefficient of 0 indicates NO linear relationship between dependant and independent variables.

P-values, a.k.a. probability values are exactly that, if you wanted to know what the probability is that you would throw a 2 on a 6-sided die then you could calculate it like this: 1/6 = 0,1667. So in English we would say you have a one in six chance of landing on a 6 and this equates to a 16.67% probability.

Now suppose we have a hypothesis, we hypothesize that we have a fair coin, that is, no matter how much we flip this coin the probability of it landing on the one side is equal to it landing on the other side.  We call this hypothesis the “Null-hypothesis”.  If we were to reject our own hypothesis then we would have to have some evidence to do so and we would then also have to accept another hypothesis, this other hypothesis would be that the coin is not a fair coin, we call this hypothesis the alternative hypothesis.


Ok, now we start flipping this coin and we record what we land on, here is what we’ve found:

1st flip:  Heads – Chances of this happening is ½ = 50%

2nd flip:  Heads – Chances of this happening is ¼ = 25%

3rd flip:  Heads – Chances of this happening is 1/8 = 12,5%

4th flip:  Heads – Chances of this happening is 1/16 = 6,25%

100th flip:  Heads – Chances of this happening is 1/2^n = 7,886 x 10^-31


By about the 4th flip you should begin to see that something strange is going on, how is it that we keep on landing on Heads?  Eventually, after the 100th throw we see that the probability of this happening is something stupendously small.  Remember this, unlikely = small p-value, probable = big p-value.


### Questions:  Ten statistical type questions

#### Question 1:
What is the probability of throwing a four on an 8-sided die?

#### Question 2:
What is the probability of throwing two fours in a row on an 8-sided die?

#### Question 3:
If you were told that during an experiment, the Null-hypothesis was that water can't flow downhill and the Alternative hypothesis was that it can, and after thousands of tests a p-value of 0.000001234 was found in favour of the Null hypothesis, would you reject or accept the Null hypothesis based on the p-value?

#### Question 4:
A man claims that his dog can run so fast that it can run on water.  Some people decide to put his theory to the test and make the dog run over water one hundred times.  A data scientist decides to calculate a p-value based on the outcome of the experiment, the p-value is calculated to be 0.15 in favour of the Null hypothesis.  What is the Null hypthesis?  What is the Alternative hypothesis?  Would you reject or accept the Null hypothesis?

#### Question 5:
Suppose you have eight friends of ages 21, 22, 23, 23, 24, 25, 26, 27.  What could be considered to be the mode of the ages?

#### Question 6:
Suppose you have eight friends of ages 21, 22, 23, 23, 24, 25, 26, 27.  What is the mean of the ages?

#### Question 7:
Suppose you have eight friends of ages 21, 22, 23, 23, 24, 25, 26, 27.  What is the median of the ages?

#### Question 8:
Suppose you have eight friends of ages 21, 22, 23, 23, 24, 25, 26, 27.  What is the variance of the ages?

#### Question 9:
Suppose you have eight friends of ages 21, 22, 23, 23, 24, 25, 26, 27.  What is the standard deviation of the ages?

#### Question 10:
Suppose we have a correlation coefficient of 0, what kind of a relationship exists between the dependant and independant variables?