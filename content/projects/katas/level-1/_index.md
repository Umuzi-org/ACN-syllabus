---
_db_id: 219
content_type: project
flavours:
- any_language
ready: true
story_points: 3
submission_type: repo
tags:
- algrithms
- clean-code
title: Level 1 coding challenges
---

These exercises are here to help you test out and demonstrate your knowledge of the basic flow control mechanisms and syntax for your language. These exercises are relevant whether you are doing Java, JavaScript, Python, Kotlin or any other modern language.

Please follow best practices when doing this work!

- Use git: push your code every day! Maybe even a few times every day. If you don't back up your work and something terrible happens to your computer then you will not be granted an extension. Make sure your commit messages make sense
- Be careful about how you name your functions and variables. Be consistent. Be clear. Call it what it is. Any fool can write code that a machine can understand, professionals write code that people understand.

## Note

The exercises below are meant to be language-agnostic. If we use the word `print` in an exercise description then we mean output it to the terminal/console/stdout. We don't mean print to a printer, and we don't want a gui. These exercises just spit out some text.

If we say a function takes an input then we don't mean you should ask the user to type something. What we need is a function parameter or argument.

## Note to web devs

Please don't submit any HTML or CSS. Please don't use `document.write`. We are interested in seeing how you implement these algorithms. Use `console.log` if you are asked to print things.

## What does success look like

Katas are pretty common in coding (and martial arts). Katas are about practicing and perfecting fundamental skills. There are a few different skills we need to see here.

The first thing is Git! It's seriously important so we want to see you developing good habits.

For every exercise in this project you need to make a new Pull Request on github and a new branch.

So if you are writing code for the first exercise you should do this:

```
git checkout main
git pull
git checkout -b task/1
```

Now you have branch for your hello code to live in. Create a file for your hello function to live in. Commit and push. Then make a pull request. Make some noise about your PR so that we can take a look at it and give you feedback.

While you wait for feedback, you can start the next exercise.

```
git checkout main  # Important: Check out the main branch and make sure it is up to date before making a new branch.
git pull
git checkout -b task/2
```

## DO NOT do random chaotic things with git

Look at your network graph for your repo whenever you push your code. It should not resemble spaghetti or any other noodle. It should be neat and tidy.

You can see the network graph of your repo by looking at the url: https://github.com/[YOUR REPO PATH]/network

If you follow the simple instructions in the "what does success look like" section then you'll be fine here.

## Super important!

At this point you should be using git from the command line. If you drag and drop to upload your code: You are doing it wrong. For real. Git is amazingly important and now is the time to get used to it!


## Task 1.1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


## Task 1.2

Write a function that takes 2 numbers as input.
If either of the numbers is 3 AND the sum of the numbers contains a 3 then return true. Otherwise return false

## Task 1.3

Write a function that takes 2 numbers as input.
If either of the numbers is 65, OR if the sum of the numbers is 65 then return true. Otherwise return false.

## Task 1.4

Write a function, name it `square`. It takes in an integer and then prints out a square using the hash character.

eg `square(2)` should print

```
##
##
```

eg `square(4)` should print

```
####
####
####
####
```

## Task 1.5

eg `triangle(2)` should print

```
#
##
```

eg `triangle(4)` should print

```
#
##
###
####
```

If negative numbers are input then the triangle should be upside down

eg `triangle(-2)` should print

```
##
#
```

eg `triangle(-4)` should print

```
####
###
##
#
```

## Task 1.6

Write a function that takes in an array/list of strings and then prints out the longest one

eg: `longest(["the","quick","brown", "fox", "ate", "my", "chickens"])`

should print

```
chickens
```

If there are multiple longest strings then print them all.

eg:

`longest(["once", "upon", "a", "time"])`

should print

```
once
upon
time
```

## Task 1.7

Write a function that combines two lists by taking alternate elements and returns the result. You can assume the lists are of equal size.

If your function can work with lists of unequal size, we'll think you’re cool.

eg `combine([11,22,33], [1,2,3])` should return

```
[11,1,22,2,33,3]
```

## Instructions for Reviewers

**Task 1.1**

- The instructions does not specify whether a value should be returned or printed. Therefore, either is competent.
- The instructions also does not specify whether a function should be created. Therefore, if a function was created or only lines of code were written and it works, it is competent.
- When a 1000 is the input, ensure that the output is 233168.

**Task 1.2 and Task 1.3** 

- Ensure that keywords(**not strings**) true or false are being returned.

**Task 1.6** 

- If there are strings with the same length, all should be printed in "next line" form.

**Task 1.7**

- Ensure that the array which is being outputted consists of alternating values of the two arrays that are being inputted.
