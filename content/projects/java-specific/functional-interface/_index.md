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

## Directory structure

```
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    ├── main
    │   └── java
    │       └── FunctionalInterfaceDemo.java       <-------- names are important
    └── test
        └── java
            └── FunctionalInterfaceDemoTest.java   <-------- names are important
```

## What is the number

Create a class called `FunctionalInterfaceDemo` which implements methods called `isOdd`, `isPalidrome` and `isPrime`. Each of the methods should return a lambda expression.

1. `isOdd`: The lambda expression must return true if a number is odd or false if it is even.

2. `isPalindrome`: The lambda expression must return true if the number is Palindrome (12321) or false if it is not a Palindrome

3. `isPrime`: The lambda expression must return true if the number is Prime (3) or false if it is not a not Prime (4)

Once the obove has been implemented, you must get a number from the standard input which will go through all three functions and return the correct strings

4. If the user enters 77 in the standard input then you should **Print** the following: 

```
 Number is: Odd, Palindrome and NotPrime
```

The user should be able to to enter another number in the standard input. For example, if the user inputs 43 the second time around, then you should print the following:

```
 Number is: Odd, NotPalindrome and Prime
```
Remember to test all your functions.

### Instructions for reviewers

- Ensure that all three functions should return lambada expressions.
- Ensure that every function is tested.
