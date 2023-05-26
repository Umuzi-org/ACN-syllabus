---
content_type: project
flavours:
- java
prerequisites:
  hard:
  - topics/java-specific/oop-basics
  - topics/java-specific/functional-interface
ready: true
submission_type: repo
tags:
- functional-interface
- lambda-expressions
title: Java Lamba Expressions and Functional Interfaces
---

## What is the number

Implement the following methods, each should return a lambda expression performing a specified action:

1. A method called `isOdd`: The lambda expression must return true if a number is odd or false if it is even.

2. A method called `isPalindrome`: The lambda expression must return true if the number is Palindrome (12321) or false if it is not a Palindrome

3. A method called `isPrime`: The lambda expression must return true if the number is Prime (3) or false if it is not a not Prime (4)

Once the obove has been implemented, you must get a number from the standard input which will go through all three functions and return the correct strings

4. If the user enters 77 in the standard input then you should **Print** the following: 

```
 Number is: Odd, Palindrome and NotPrime
```

The user should be able to to enter another number in the standard input.


**Example2: User types 43 this time**

```
 Number is: Odd, NotPalindrome and Prime
```

***ALL FUNCTIONS MUST BE TESTED***


#### Instructions for reviewers

- Ensure that all three functions should return lambada expressions.

- Ensure that every function is tested.
