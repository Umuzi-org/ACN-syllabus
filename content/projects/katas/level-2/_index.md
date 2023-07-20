---
_db_id: 637
content_type: project
flavours:
- any_language
from_repo: projects/katas/level-1
learning_outcomes:
- code_algorithmic_thinking
- code_pseudo_code
- code_problem_decomposition
- code_control_flow
- code_naming_convention
- code_code_documentation
- code_existing_code_update
- code_basic_calculation
prerequisites:
  hard:
  - projects/katas/level-1
ready: true
story_points: 3
submission_type: continue_repo
tags:
- algorithms
- clean-code
title: Level 2 coding challenges
---

## Project directory structure

Task 2.1 and Task 2.2 are a updates of Task 4 and 5 from {{< contentlink path="projects/katas/level-1" >}}. You should not create new files for them. Rather just update the existing code.

For Task 2.3, you are expected to create a new files with the following names:

- `task2_3.js` for javascript
- `task2_3.py` for python
- `Task2_3.java` for java

**Note:** Accuracy is very important. The output should be exactly as shown in the examples. Unnecessary spaces or newlines will get you marked wrong and taken back.

## Task 2.1

Update your existing square function so that it takes 2 parameters. The first parameter should be the size of the square and the second one should be the character to use when drawing the square. The second parameter should be optional.

For example, `square(2)` should output:

```
##
##
```

For example, `square(2, '*')` should output:

```
**
**
```

## Task 2.2

Upgrade your triangle function so that it takes in an optional argument named `mode`

`triangle(3)` should print:

```
#
##
###
```

`triangle(3, "left")` should print:

```
#
##
###
```

(in other words, the default mode is left)

`triangle(3, "right")` should print:

```
  #
 ##
###
```

`triangle(3, "isosceles")` should print:

```
  #
 ###
#####
```

Negative numbers should still print things upside down.

For example, `triangle(-3, "isosceles")` should print:

```
#####
 ###
  #
```

### Up for a Challenge?

This section of task 2.2 is not compulsory but if you do this, we’ll think you’re cool.

Add some functionality to `triangle` so that an error/exception gets raised if an incorrect mode is entered.

## Task 2.3

Write a function `columns` that takes a list of strings and prints them as columns with a single space between them.

For example, `columns(["Write","good","code","every","day"])` gets printed as:

```
W g c e d
r o o v a
i o d e y
t d e r
e     y
```

**For javascript:** Don't forget to export you function with the code:

```
module.exports = {functionName}
```

## Next Steps

Well done for getting this far! These exercises demonstrated some really fundamental skills. You should be familiar with some loops, if statements, comparisons and the syntax of functions. Even though we have hit the end of this project, there is a lot left for you to learn.

Make sure you really understand all the code you wrote here. You should know what every single line does and why it is there. 

Remember that you are here to become a professional! Professionals take ownership of their learning and skills, and professionals help the people around them become successful.

A professional doesn't just know a bit of syntax, a professional solves real problems with code. So it's worth building up your problem solving skills over time. The only way to do that is through practice and curiosity.

Here are some resources you can use to continue this journey:

- https://adriann.github.io/programming_problems.html: this has a lot of cool little exercises. They're mostly pretty small, you could do a few everyday if you wanted to. Even one per day would be a winner.
- https://www.codewars.com: you should know about this already, it's legit!

Have fun :)
