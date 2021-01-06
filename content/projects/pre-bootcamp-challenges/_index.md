---
_db_id: 416
available_flavours:
- any_language
content_type: project
prerequisites:
  hard:
  - topics/messaging/honor-code
  - projects/git-exercises
ready: true
submission_type: link
title: Level 0 coding challenges
---

Complete these tasks in the correct language. If you are here to learn JavaScript, do them in JavaScript. If you have been told to use Python then use Python.

Use Git and Github to save your code to the cloud (like a boss)

Please remember that you need to focus on UNDERSTANDING!

Some of these task are kinda easy, but they were all chosen for good reasons. Try think about the lessons each task is trying to teach you. Think about what might confuse other people.

Some of these are difficult. Seek out help when you need it. Always focus on UNDERSTANDING.

## Common problems

A lot of people get the following stuff wrong. Please read this section again before you ask for a review.

### Don't write useless comments

A lot of people think it's a good idea to write lots of comments. They write a line of code and then they write that code out in English. For example

```
c = a + b // add a and b together and store it in c
```

This kind of thing is a giant waste of everyone's time.

Comments can be really useful sometimes. But use them sparingly.

Always remember that coders read code. You don't need to explain every little thing.

Good code uses good function and variable names in order to make it's intention clear. Good code documents itself.

Comments are useful if you need to

- explain why you are doing something
- link to an external document
- add extra facts or info that isn't obvious. Eg: `// Pythagoris formula` can be a comment on a line that implements the formula

### Don't name your functions anything to do with `my` or `function`

The following is bad:

```
def function # python

function myTriangle // js
```

If you are giving a function a name, then give it a name that means something. Names matter.

I know a lot of tutorials out there use `my` a lot in function and variable names. But you'll never see that kind of thing in a professional code base. And now is the time to start building professional habits.

### Do follow the instructions

If the instructions say write a function, then please write a function. If you are meant to return a value and you decide to print it instead then that's incorrect.

### Do check your work

Make sure your code works before you ask for a review. If it doesn't work it will not be accepted.

Good coders pay close attention to detail.

### a function input is a parameter or argument

A lot of people like to get their code to ask the user to enter values using the keyboard. Please don't do that unless it is explicitly requested.

A function's inputs are it's parameters or arguments. We need to see that you know how to drive a function.

### Write readable code

Code is read more often than it is written. Get into the habit of writing clean and readable code. This means:

- consistent and meaningful indentation
- don't leave a million lines of commented out code
- don't leave lots or blank lines
- do choose names wisely and consistently

## Task 1

Convert this pseudocode into actual code. Make it run. Make sure you understand the results. This is a fundamental lesson:

```
x = 0
y = 1
Print the value of x
Print the value of y
x = x + 3
y = y + x
Print the value of x
Print the value of y
```

Check your understanding:

Lots of people think this is easy then get it wrong later. Make sure you check yourself

- do you know what pseudocode means? Did you look it up?
- do you understand why x and y have the values they have at each point in the program?

## Task 2

Convert this pseudocode into actual code. Make it run. Make sure you understand the results. This is a fundamental lesson. If you don’t understand the results then spend some time Googling BODMAS.

```
x = 1 + 1 * 2
y = (1 + 1) * 2
z = 1 + ( 1 * 2 )
a =  1 + 1 * 2 / 2
b =  (1 + 1 * 2 ) /  2
```

Check your understanding:

- do you know what pseudocode means? Did you look it up?
- do you understand why the variables have the values they have at each point in the program?
- do you understand BODMAS?

## Task 3

Write a function that takes 2 numbers as input.
If either of the numbers is 65, OR if the sum of the numbers is 65 then return true. Otherwise return false.

## Task 4

Write a function that takes 2 numbers as input.
If either of the numbers is 3 AND the sum of the numbers contains a 3 then return true. Otherwise return false

## Task 5

Write a function that takes in three numbers. These numbers represent the lengths of the sides of a triangle. The function should return the area of a triangle.

This might help: https://www.wikihow.com/Calculate-the-Area-of-a-Triangle

## Task 6

White a function that takes in three numbers and returns the maximum number.

Do this without using any builtin methods. Write your own logic from scratch.

The function should expect a bunch of numbers, not an array or list.

```
maximum([1,2,3])  // BAD
maximum(1,2,3)  // GOOD

```

Bonus: How can you change the code so it can take in any number of numbers? Do this without using builtin methods. Write your own logic from scratch.

Again, the function should expect a bunch of numbers as input, not an array or list.

Please do not write a whole new function. Upgrade your existing function.

## Task 7

Write a function that takes in a number representing the temperature in Celsius and returns the temperature in Fahrenheit. Write another function that does the opposite (Fereignheit to Celsius)

## Task 8

Make a function to convert any number into hours and minutes. (For example, 71 will become “1 hour, 11 minutes; 133 will become “2 hours, 13 minutes.)

Most people get this question wrong. Make sure you handle singulars and plurals for both hours and minutes.

## Task 9

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## Task 10

Write a function that takes in a string and then prints out all the vowels in the string. Make sure it can deal with capital letters and small letters.

## Task 11

Make a function that takes two strings as input, and outputs the common characters/letters that they share. (For example, Input: ‘house’, ‘computers’ . Output: ‘Common letters: o, u, e, s’)

## Task 12: BONUS task for web devs

This task isn't compulsory but we'll be impressed if you do it.

Can you make a user interface for each of the previous tasks? You'll need HTML and CSS to do it.

NOTE: Good code is DRY. If you copy paste your functions in order to get this to work, then that is no good! We need you to work like a professional developer. Each task should be represented only once in the code.

- Use forms to allow the user to enter inputs to the various functions.
- use the pre tag to format your output https://www.w3schools.com/tags/tag_pre.asp