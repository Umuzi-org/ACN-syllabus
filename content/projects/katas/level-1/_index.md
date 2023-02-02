---
_db_id: 219
content_type: project
flavours:
- any_language
learning_outcomes:
- code_algorithmic_thinking
- code_pseudo_code
- code_problem_decomposition
- code_control_flow
- code_naming_convention
- code_code_documentation
- code_basic_calculation
prerequisites:
  hard:
  - topics/reopening-pull-request
ready: true
story_points: 3
submission_type: repo
tags:
- algorithms
- clean-code
title: Level 1 coding challenges
---

These exercises are here to help you test out and demonstrate your knowledge of the basic flow control mechanisms and syntax for your language. These exercises are relevant whether you are doing Java, JavaScript, Python, Kotlin or any other modern language.

Please follow best practices when doing this work!

- Use git: push your code every day! Maybe even a few times every day. If you don't back up your work and something terrible happens to your computer then you will not be granted an extension. Make sure your commit messages make sense.
- Be careful about how you name your functions and variables. Be consistent, clear and call it what it is. Any fool can write code that a machine can understand but professionals write code that people can understand.

## Note

The exercises below are meant to be language-agnostic. If we use the word `print` in an exercise description then we mean output it to the terminal/console/stdout. We don't mean print to a printer, and we don't want a gui. These exercises just spit out some text.

If we say a function takes an input then we don't mean you should ask the user to type something. What we need is a function parameter or argument.

## Note to web devs:

Please don't submit any HTML or CSS. Please don't use `document.write`. We are interested in seeing how you implement these algorithms. Use `console.log` if you are asked to print things.

## What does success look like?

Katas are pretty common in coding (and martial arts). Katas are about practicing and perfecting fundamental skills. There are a few different skills we need to see here.

The first thing is git! It's seriously important so we want to see you developing good habits.

For every exercise in this project, you need to make a new pull request and a new branch on github.

So, if you are writing code for the first exercise then you should do this:

```
git checkout main
git pull
git checkout -b task/1
```

Now you have branch for your hello code to live in. Create a file for your hello function to live in. Commit, push then make a pull request. Make some noise about your PR so that we can take a look at it and give you feedback.

While you wait for feedback, you can start the next exercise.

```
git checkout main  # Important: Check out the main branch and make sure it is up to date before making a new branch.
git pull
git checkout -b task/2
```

## DO NOT do random chaotic things with git

Look at your network graph for your repo whenever you push your code. It should not resemble spaghetti or any other noodle. It should be neat and tidy.

You can see the network graph of your repo by looking at the url: https://github.com/[YOUR REPO PATH]/network. Note: please put in your own repo path in [YOUR REPO PATH]

If you follow the simple instructions in the "what does success look like?" section then you'll be fine here.

## Super important!

At this point you should be using git from the command line. If you drag and drop to upload your code, you are doing it wrong. Git is amazingly important and now is the time to get used to it!

**Name your files according to the tasks e.g task1.js and the functions according to the instructions**

## Task 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Write a function `multiples` without parameters that prints the sum of all the multiples of 3 or 5 below 1000.

## Task 2

Write a function `hasThree` that takes 2 numbers as input.
If either of the numbers is 3 and the sum of the numbers contains a 3 then return true. Otherwise, return false.

## Task 3

Write a function `isSixtyFive` that takes 2 numbers as input.
If either of the numbers is 65, or if the sum of the numbers is 65 then return true. Otherwise, return false.

## Task 4

Write a function `square`. It takes in an integer and then prints out a square using the hash character.

For example, `square(2)` should print:

```
##
##
```

For example, `square(4)` should print:

```
####
####
####
####
```

## Task 5

Write a function `triangle` that takes in an Integer and prints a triangle accordingly, `triangle(2)` should print:

```
#
##
```

For example, `triangle(4)` should print:

```
#
##
###
####
```

If negative numbers are input then the triangle should be upside down.

For example, `triangle(-2)` should print:

```
##
#
```

For example, `triangle(-4)` should print:

```
####
###
##
#
```

## Task 6

Write a function `longest` that takes in an array/list of strings and then prints out the longest one.

For example, `longest(["the","quick","brown", "fox", "ate", "my", "chickens"])` should print:

```
chickens
```

If there are multiple longest strings then print them all.

For example, `longest(["once", "upon", "a", "time"])` should print:

```
once
upon
time
```

## Task 7

Write a function `combine` that combines two lists by taking alternate elements and returns the result. You can assume the lists are of equal size.

Your combine function should be able to work with lists of unequal size.

For exampe, `combine([11,22,33,45], [1,2,3])` should return:

```
[11,1,22,2,33,3,45]
```

Also, the output lists should maintain the list items in the original order in which they appeared in the input lists, so combine([12, 4, 2], [1, 5, 3]) should return:

```
[12,1,4, 5, 2, 3]
```



## Instructions for Reviewers

**Task 1**

- Ensure that the output is 233168.

**Task 2 and Task 3**

- Ensure that keywords(**not strings**) true or false are being returned.

**Task 6**

- If there are strings with the same length, all should be printed in "next line" form.

**Task 7**

- Ensure that the array which is being outputted consists of alternating values of the two arrays that are being inputted.