---
_db_id: 645
content_type: project
flavours:
- any_language
ready: true
story_points: 3
submission_type: repo
tags:
- algrithms
- clean-code
title: Level 1 coding challenges (alt)
---

These exercises are here to help you test out and demonstrate your knowledge of the basic flow control mechanisms and syntax for your language. These exercises are relevant whether you are doing Java, JavaScript, Python, Kotlin or any other modern language.

Please follow best practices when doing this work!

- Use git: push your code every day! Maybe even a few times every day. If you don't back up your work and something terrible happens to your computer then you will not be granted an extension. Make sure your commit messages make sense
- Be careful about how you name your functions and variables. Be consistent. Be clear. Call it what it is. Any fool can write code that a machine can understand, professionals write code that people understand.
- submit a separate file for each task, submit a separate PR for each task
- make sure your file names are consistent

## Note

The exercises below are meant to be language-agnostic. If we use the word `print` in an exercise description then we mean output it to the terminal/console/stdout. We don't mean print to a printer, and we don't want a gui. These exercises just spit out some text.

If we say a function takes an input then we don't mean you should ask the user to type something. What we need is a function parameter or argument.

## Note to web devs

Please don't submit any HTML or CSS. Please don't use `document.write`. We are interested in seeing how you implement these algorithms. Use `console.log` if you are asked to print things.

## What does success look like

Katas are pretty common in coding (and martial arts). Katas are about practicing and perfecting fundamental skills. There are a few different skills we need to see here.

## Professional use of git

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
# do the work
# commit the work
# push the work
# make a PR
# then repeat this process for the next task
```

### DO NOT do random chaotic things with git

Look at your network graph for your repo whenever you push your code. It should not resemble spaghetti or any other noodle. It should be neat and tidy.

You can see the network graph of your repo by looking at the url: https://github.com/[YOUR REPO PATH]/network

If you follow the simple instructions in the "what does success look like" section then you'll be fine here.

### Use git from the command line

At this point you should be using git from the command line. If you drag and drop to upload your code: You are doing it wrong. For real. Git is amazingly important and now is the time to get used to it!

### Write clean code

Use clear and consistent names. Good code makes it's intentions clear.

## Task 1.1

Create a function that takes in an array/list of numbers. It should find the second biggest number and the second smallest number and return them as a string with a space in between them.

For example: if the array contains [7, 7, 12, 98, 106] the output should be "12 98" because 12 is the second smallest number, and 98 is the second biggest number.

The array will not be empty and will contain at least 2 numbers.

Examples:

Input: [1, 2, 3, 4, 5]
Output: "2 4"

Input: [1, 1, 2, 3, 4, 4, 5]
Output: "2 4"

## Task 1.2

Create a function that takes a string parameter as input, then returns a string that has the first letter of each word capitalised.

Examples

Input: "hello world"
Output: Hello World

Input: "i ran there"
Output: I Ran There

## Task 1.3

Create a function that takes one string parameter as input. It should return a boolean True if there is an equal number of x's and o's, otherwise return false.

For example: if str is "xooxxxxooxoweeeeestuffwhatever" then the output should return false because there are 6 x's and 5 o's.

Input: "xoox"
Output: true

Input: "x"
Output: false

## Task 1.4

Create a function that takes in two strings representing 2 times, the function should return the number of minutes between the 2 times. The input times will be of a 12 hour format, there will be a colon between the hours and minutes, and there will be an 'am' or 'pm' on the end of each input string.

Examples

Input: "12:40pm", "12:00am"
Output: 680

Input: "1:24am", "1:10am"
Output: 1426

## Task 1.5: BONUS

This is not compulsory. But if you get it right we'll put smiley faces in your code review :)

Write a function named `maximum row sum` (name it according to the convention that is common in the programming language you are writing in). This function should take in a string that represents a grid of numbers. Here is an example input:

```[]
1 3 5 8
3 2 1 2
5 5 5 7
```

- Each row is separated by a newline character.
- Each number in each row is separated by whitespace.

Your function needs to return the sum of the row with the biggest sum.

Following from our example above:

```[]
1 + 3 + 5 + 8 = 17
3 + 2 + 1 + 2 = 8
5 + 5 + 5 + 7 = 22 <--- This is the biggest sum
```

In this case the function should return 22.