---
_db_id: 710
content_type: project
flavours:
- none
ready: true
submission_type: link
tags:
- technical-assessment
title: 'Assessment: Basic data analysis'
---

## Note about submission format

On Tilde you'll notice that this card is asking for a link submission. **Please don't worry about submitting a link**. You will be assessed according to {{% contentlink path="specific-skill-success-criteria/introduction-to-assessments" %}}.

## All concepts

For each of the concepts covered below, the learner should know how to do the calculations by hand. If the learner only knows how to do this work using data science tooling (e.g. pandas) then they won't be in a good position to apply the tools correctly or reason about their output.

## Mean (Average value):

Given a list of numbers, the learner should be able to calculate the mean:

For example, the average of `[87, 94, 78, 77, 85, 86]` is 84.5.

## Median

Given a list of numbers the learner should be able to calculate the median. Make sure to check that they know how to handle:

- lists with an even number of elements. For example : `[87, 94, 78, 77, 85, 86]`
- lists with an odd number of elements. For example : `[87, 94, 77, 85, 86]`
- lists that aren't sorted. For example : `[30,2,12,1,8]`

## Mode

Given a list of numbers, the learner should be able to calculate the mode.

Example 1: `[2,3,4,2]`
Example 2: `[2,3,4,2,3]`

## Interquartile range `IQR`

Given a list of numbers, the learner should be able to calculate the 1st, 2nd and 3rd quartile.

Make sure to check that they know how to handle:

- lists with an even number of elements. For example : `[87, 94, 78, 77, 85, 86]`
- Lists with an odd number of elements. For example : `[87, 94, 77, 85, 86]`
- Lists that aren't sorted. For example : `[30,2,12,1,8]`

## Variance and Standard deviation

- The learner should be able to calculate the variance and standard deviation of a list of numbers.
- If you show the learner a plot of some data and ask them if standard deviation is meaningful, they should be able to tell you. For example, is it worth calculating the standard deviation of an exponential distribution?
- If you have a normal distribution where the curve is flat, and another one where the curve is pointy, then which one has the higher standard deviation?

## Correlation coefficient `R`

The learner should know:
- What is the minimum value that the correlation coefficient can have? What does it mean if we have this value?
- What is the maximum value that the correlation coefficient can have? What does it mean if we have this value?
- What does it mean if the correlation coefficient is 0?

Show the learner some scatter plots and ask them to tell you about the correlation of the various plots. Cover a range of different p values.

## Probability

The learner should be able to do simple calculations of probabilities. They should know when probabilities should be multiplied and when they should be added.

Here are a few sample questions: what is the probability of...
- Throwing a 2 on a six-sided die?
- Throwing an even number on a six-sided die?
- Rolling 2 six-sided dice and getting a total value of 5? (for example, one die lands on a 2 and the other on a 3)
- Rolling 3 sixes in a row if you roll a six-sided die 3 times
- Rolling 3 sixes in a row if you roll a six-sided die 5 times

## P-value

The learner should know:
- What is the minimum number that the p-value can have? What does this imply?
- What is the maximum number that the p-value can have? What does this imply?

The learner should be able to do calculations about p values based on known probabilities.

For example, if you roll a six-sided die 5 times and get 3 sixes in a row then is the die likely to be fair?
