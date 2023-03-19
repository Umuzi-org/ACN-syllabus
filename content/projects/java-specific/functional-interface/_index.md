---
content_type: project
flavours:
- java
prerequisites:
  hard:
  - topic/oop
  - topics/java-specific/functional-interface
ready: true
submission_type: repo
tags:
- functional-interface
- lambda-expressions
title: Java Lamba Expressions and Functional Interfaces
---

Write the following methods that return a lambda expression performing a specified action:

1. A method called **isOdd**: The lambda expression must return true if a number is odd or false if it is even.

2. A method called **isPalindrome**: The lambda expression must return true if the number is Palindrome (12321) or false if it is not a Palindrome

3. A method called **isPrime**: The lambda expression must return true if the number is Prime (3) or false if it is not a not Prime (4)

Then you must get a number from the standard input which will go through all three functions and return the correct strings

4. If the user enters 77 in the standard input then you should **Print** 

```
 Number is: Odd, Palindrome and NotPrime
```

Then give the user an Opportunity to enter another number


**Example2: User types 43 this time**

```
 Number is: Odd, NotPalindrome and Prime
```

***ALL FUNCTIONS MUST BE TESTED***


#### Not to reviewer
- All three function return lambada expressions
- All functions are tested
- Where things should be returned are returned and where they should be printed they are printed