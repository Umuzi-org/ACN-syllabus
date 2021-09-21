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
- Python concepts:  Thirteen questions and how you would answer them using Python and Pandas

### Statistical concepts: Mean, Median and Mode

#### Mean (Average value):
```
Calculating the mean (average value) by yourself:

list_of_speed_data = [87, 94, 78, 77, 85, 86]

mean = (87+94+78+77+85+86) = 507/6 = 84.5


Calculating the mean using numpy:

import numpy

list_of_speed_data = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.mean(list_of_speed_data)
```


#### Median (Middle value):
```
Calculating the median (middle value) by yourself:

list_of_speed_data = [100, 200, 300, 400, 500, 600]

When we have an even amount of numbers we need to calculate the mean (average) of the two middle 
numbers, in this case 300 and 400.  So the mean (average) of 300 and 400 is (300+400)/2 = 350.
Therefore the mean (middle) value is:  median = 350


When we have an odd amount of numbers we need to divide the total amount of numbers by 2 and then
round up to the nearest integer.  For instance:

list_of_speed_data = [100, 200, 300, 400, 500, 600, 700]

There are seven numbers in the list, 7/2 = 3.5, if we round up to the nearest integer we get 4.  
Therefore, the 4th number in the list will be the median (middle) value:  median = 400


Calculating the median using numpy:

import numpy

list_of_speed_data = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.median(list_of_speed_data)
```


#### Mode (Most frequent value):
```
The mode is the value which occurs the most in a set.  So if you had a set [2, 2, 2, 3] then the
mode would be 2 since 2 is the value which occurs most frequently in the set.

Calculating the mode with stats from the scipy module:

from scipy import stats

list_of_speed_data = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = stats.mode(list_of_speed_data)
```



### Statistical concepts: Interquartile range (IQR)
1st quartile:  Middle number between the smallest number and the median of the dataset

2nd quartile:  Equal to the median of the dataset

3rd quartile:  Middle number between the median and the largest value of the dataset

```
import numpy as np

data = [32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 89, 91, 92, 93, 96, 97, 101, 105, 112, 116]

# First quartile (Q1)
Q1 = np.percentile(data, 25, interpolation = 'midpoint')
  
# Third quartile (Q3)
Q3 = np.percentile(data, 75, interpolation = 'midpoint')
  
# Interquaritle range (IQR)
IQR = Q3 - Q1


OR YOU CAN DO THIS:


from scipy import stats

# Interquartile range (IQR)
IQR = stats.iqr(data, interpolation = 'midpoint')
```



### Statistical concepts: Standard deviation and Variance
Standard deviation and variance are both determined by using the mean of the dataset.  Variance measures the average degree to which each number is different from the mean.  Standard deviation is a statistic that looks at how far from the mean a group of numbers is, by using the square root of the variance.  Standard deviation is similar to variance, which gives the measure of deviation whereas variance provides the value squared.

```
from statistics import stdev, variance

sample_data = [1, 2, 3, 4, 5]
 
print(f"Standard Deviation is: {stdev(sample_data)}")
print(f"Variance is: {variance(sample_data)}")
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



### Python concepts: Thirteen questions and how you would answer them using Python and Pandas

#### Question 1:
If we wanted to make use of the pandas module and name it 'pd', how would we import it?
```
import pandas as pd
```

#### Question 2:
If we want to read data from a file named 'data.csv' and store the data in a dataframe object named 'df' what would we do?
```
df = pd.read_csv('data.csv')
```

#### Question 3:
How will you find the region with the highest population over 60 if you make use of the groupby functionality so that you see the ‘Region’ and too the right of it you see the maximum value for the column ‘Over60’ for the particular region.  You should make use of .groupby and .max() in a single line of code?
```
print(df.groupby('Region')['Over60'].max())
Or
print(df.groupby('Region').Over60.max())
```

Here is what it would look like:
```
Region
Africa                   13.23
Americas                 20.82
Eastern Mediterranean    12.03
Europe                   26.97
South-East Asia          13.96
Western Pacific          31.92
Name: Over60, dtype: float64
```

#### Question 4:
Continuing on from the previous question, suppose we wanted the values we get in sorted
order, how would you apply  the functionality of `.sort_values(ascending=True)` to the previous line of code in order to retrieve the desired result?
```
print(df.groupby('Region')['Over60'].max().sort_values(ascending=True))
```

Here is what it would look like:
```
Region
Eastern Mediterranean    12.03
Africa                   13.23
South-East Asia          13.96
Americas                 20.82
Europe                   26.97
Western Pacific          31.92
Name: Over60, dtype: float64
```

#### Question 5:
What will `pd.describe( )` look like and what is it for?

Here is what it will look like:
```
         Population     Under15      Over60  FertilityRate  LifeExpectancy  ChildMortality  CellularSubscribers
count  1.940000e+02  194.000000  194.000000     183.000000      194.000000      194.000000           184.000000
mean   3.635997e+04   28.732423   11.163660       2.940656       70.010309       36.148969            93.641522
std    1.379031e+05   10.534573    7.149331       1.480984        9.259075       37.992935            41.400447
min    1.000000e+00   13.120000    0.810000       1.260000       47.000000        2.200000             2.570000
25%    1.695750e+03   18.717500    5.200000       1.835000       64.000000        8.425000            63.567500
50%    7.790000e+03   28.650000    8.530000       2.400000       72.500000       18.600000            97.745000
75%    2.453525e+04   37.752500   16.687500       3.905000       76.000000       55.975000           120.805000
max    1.390000e+06   49.990000   31.920000       7.580000       83.000000      181.600000           196.410000
```
Clearly the above result gives us some descriptive statistics regarding the dataset.  We can easily see what the
minimum, maximum, IQR etc values are for each column.

#### Question 6:
How will you display how many .NaN values there are in 'df', making sure to get a single result and not a table which shows how many .NaN values there are per column?
```
print(df.isnull().sum())
```

What it would look like as a table:
```
Country                           0
Region                            0
Population                        0
Under15                           0
Over60                            0
FertilityRate                    11
LifeExpectancy                    0
ChildMortality                    0
CellularSubscribers              10
LiteracyRate                     91
GNI                              32
PrimarySchoolEnrollmentMale      93
PrimarySchoolEnrollmentFemale    93
dtype: int64
```


What it would look like as a single result:
```
print(df.isnull().sum().sum())

330
```

#### Question 7:
Find the min value of the Over60 column using `.describe()`:
```
print(df.describe()['Over60'].min())
```

#### Question 8:
Calculate the IQR of the FertilityRate column using `.describe()`, making sure that your results are printed to the console:
```
print(int(df.describe()['FertilityRate']['75%']) - int(df.describe()['FertilityRate']['25%']))
```

#### Question 9:
Find the maximum value in each column with a single 'For' loop and using `.describe()`
```
for column in df.describe():
    print(df.describe()[column].max())
```

Here is what it would look like:
```
1390000.0
194.0
194.0
183.0
194.0
194.0
196.41
103.0
86440.0
101.0
101.0
```

#### Question 10:
Print all rows of 'df' but only for the columns 'Region', 'Country' and 'GNI'.  Be sure to make use of the functionality `.loc`
```
print(df.loc[:, ['Region', 'Country', 'GNI']])
```

Here is what it would look like:
```
                    Region                                    Country      GNI
0    Eastern Mediterranean                                Afghanistan   1140.0
1                   Europe                                    Albania   8820.0
2                   Africa                                    Algeria   8310.0
3                   Europe                                    Andorra      NaN
4                   Africa                                     Angola   5230.0
5                 Americas                        Antigua and Barbuda  17900.0
6                 Americas                                  Argentina  17130.0
7                   Europe                                    Armenia   6100.0
8          Western Pacific                                  Australia  38110.0
9                   Europe                                    Austria  42050.0
10                  Europe                                 Azerbaijan   8960.0
```

#### Question 11:
For the rows that have .NaN values, calculate the mean of the previous row and the following row and then interpolate the .NaN values with this newly calculated value.
```
df.interpolate(method='linear', axis=0, inplace=True)
```

#### Question 12:
Check if the dataset contains any duplicate values
```
print(df.duplicated())
```

#### Question 13:
Suppose you are told that the assumed Null hypothesis is that a R5 coin is a fair coin, therefore, no matter how many times you flip it, the probability of landing on either side is equal.  Suppose now we flip the coin 10 times and it lands on heads 8 times out of the 10 flips, the following is used to calculate the p-value:
```
- 40320 (The number of ways 8 ‘heads’ can be arranged in 8 spaces)
- 181440 (The number of ways you can have 8 ‘heads’ out of 10 flips)
- Possible arrangements:  181440/40320 = 4,5
- Total outcomes:  2^10 = 1024
- P-value of this happening:  4,5/1024 = 4,3X10^-3 = 0,0044
```
Given that the standard threshold value for rejecting the Null hypothesis is anything less than or equal to 0,05, would you say that there is enough evidence to reject the Null hypothesis and accept the alternative hypothesis?
```
Solution:  Yes, there is enough evidence, we should accept the alternative hypothesis that this coin is indeed not a fair coin.
```