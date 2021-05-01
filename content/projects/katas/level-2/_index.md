---
_db_id: 637
content_type: project
flavours:
- any_language
from_repo: projects/katas/level-1
prerequisites:
  hard:
  - projects/katas/level-1
ready: true
story_points: 3
submission_type: continue_repo
title: Level 2 coding challenges
tags: 
  - algrithms 
  - clean-code
---

## Task 2.1

Update your existing square function so that it takes 2 parameters. The first parameter should be the size of the square, and the second one should be the character to use when drawing the square. The second parameter should be optional.

eg `square(2)` should output

```
##
##
```

eg `square(2, '*')` should output

```
**
**
```

## Task 2.2

Upgrade your triangle function so that it takes in an optional argument named `mode`.

`triangle(3)` should print

```
#
##
###
```

`triangle(3, "left")` should print

```
#
##
###
```
(in other words, the default mode is left)

`triangle(3, "right")` should print

```
  #
 ##
###
```

`triangle(3, "isosceles")` should print

```
  #
 ###
#####
```

Negative numbers should still print things upside down. Eg:


`triangle(-3, "isosceles")` should print

```
#####
 ###
  #
```

## Task 2.3

Write a function that takes a list of strings an prints them as columns, with a single space between the columns

eg: `columns(["Write","good","code","every","day"])` gets printed as:

```
W g c e d
r o o v a
i o d e y
t d e r
e     y
```


## Next Steps

Well done for getting this far! These exercises practiced some really fundamental skills. You should be familiar with some loops, if statements, comparisons, and the syntax of functions. But even though we have hit the end of this project there is a LOT left for you to learn and practice.

Make sure you really understand all the code you wrote here. You can't build a house without a foundation. You need a solid foundational skills so you can be a pro!

So keep practicing. Practice in your free time, practice if you are ahead of schedule with one of your projects, practice if you need a break from another task. Push yourself and be awesome! You can even practice with a pen and paper.

Remember that you are here to become a professional! Professionals take ownership of their own learning and skills, and professionals help the people around them to become successful.

Here are some resources you can use to continue this journey:

- https://adriann.github.io/programming_problems.html : this has lots of cool little exercises. They're mostly pretty small, you could do a few every day if you wanted to. Even one per day would be a winner
- https://www.codewars.com: you should know about this already, it's legit!

Have fun :)