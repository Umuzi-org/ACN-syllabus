---
_db_id: 219
available_flavours:
- any_language
content_type: project
ready: true
story_points: 3
submission_type: repo
title: Level 1 programming katas
---

These Exercises are here to help you test out and demonstrate your knowledge of the basic flow control mechanisms and syntax for your language. These Exercises are relevent whether you are doing Java, JavaScrupt, Python, Kotlin or any other modern language.

Please follow best practices when doing this work!

- Use git: push your code every day. Maybe even a few times every day. If you don't back up your work and something terrible happens to your computer then you will not be granted an extension. Make sure your commit messages make sense
- Be careful about how you name your functions and variables. Be consistent. Be clear. Call it what it is. Any fool can write code that a machine can understand, professionals write code that people understand.

## Note

The Exercises below are meant to be language-agnostic. If we use the word `print` in an Exercise description then we mean output it to the terminal/console/stdout. We dont mean print to a printer, and we dont want a gui. These exercises just spit out some text.

## Note to web devs

Please dont submit any HTML or CSS. Please don't use `document.write`. We are interested in seeing how you implement these algorithms.

## What does success look like

Katas are pretty common in coding (and martial arts). Katas are about practicing and perfecting fundamental skills. There are a few different skills we need to see here.

The first thing is Git! It's seriously important so we want to see you developing good habits.

For every excercise in this project you need to make a new Pull Request on github and a new branch.

So if you are writing code for the first excerchise you can do this:

```
git checkout master
git pull
git checkout -b hello
```

Now you have branch for your hellp code to live in. Create a file for your hello function to live in. Commit and push. Then make a pull request. Make some noise about your PR so that we can take a look at it and give you feedback.

While you wait for feedback, you can start the next excercise.

```
git checkout master  # Important: Check out the master branch and make sure it is up to date before making a new branch.
git pull
git checkout -b even_or_odd
```

## Excercise: Hello

Write a function named `hello`, it needs to take in a string as an argument. The function should work like this:

eg: `hello("Tshepo")` should output

```
Hello Tshepo!
```

## Exercise: check if a number is even

Write a function named `even_or_odd` or `evenOrOdd`. Your function should take an integer and print in the work "even" or "odd"

Please be careful what name you choose to use. Different programming languages have different conventions.

eg, if the input is 3 then the output is "odd". If the input is 4 then the output is "even"

## Exercise: Draw a square

Write a function, name it `square`. It takes in an integer and then prints out a square using the hash character.

eg `square(2)` should output

```
##
##
```

eg `square(4)` should output

```
####
####
####
####
```

## Exercise: Draw a right handed triangle

eg `triangle(2)` should output

```
#
##
```

eg `triangle(4)` should output

```
#
##
###
####
```

## Exercise: Draw an isosceles triangle

eg `isosceles(2)` should output

```
 #
###
```

eg `isosceles(4)` should output

```
   #
  ###
 #####
#######
```

## Exercise: find the longest string

Write a function that takes in an arra/list of strings and then prints out the longest one

eg: `longest(["the","quick","brown", "fox", "ate", "my", "chickens"])`

should output

```
chickens
```

If there are multiple longest strings then print them all.

eg:

`longest(["once", "upon", "a" "time"])`

should output

```
once
upon
time
```

## Exercise: combine two lists/arrays

Write a function that combines two lists by alternatingly taking elements and prints the result

eg `combine([11,22,33], [1,2,3])` should output

```
 [11,1,22,2,33,3]
```

## Exercise: Frame some text

Write a function that takes a list of strings an prints them, one per line, in a rectangular frame.

eg: `frame(["Write","good","code","every","day"])` gets printed as:

```
*********
* Write *
* good  *
* code  *
* every *
* day   *
*********
```

## Next Steps

Well done for getting this far! These excercises practiced some really fundamental skills. You should be familiar with some loops, if statements, comparisons, and the syntax of functions. But even though we have hit the end of this project there is a LOT left for you to learn and practice.

Make sure you really understand all the code you wrote here. You can't build a house without a foundation. You need a solid foundational skills so you can be a pro!

So keep practicing. Practice in your free time, practice if you are ahread of schedule with one of your projects, practice if you need a break from another task. Push yourself and be awesome! You can even practice with a pen and paper if you don't have access to a computer at home.

Remember that you are here to become a professional! Professionals take ownership of their own learning and skills, and professionals help the people around them to become successful.

Here are some resources you can use to continue this journey:

- https://adriann.github.io/programming_problems.html : this has lots of cool little excercises. They're mostly pretty small, you could do a few every day if you wanted to. Even one per day would be a winner
- https://www.codewars.com: you should know about this already, it's legit!

Have fun :)