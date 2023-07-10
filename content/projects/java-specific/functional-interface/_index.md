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

Create a main method that gets a number from the standard input and then prints a message describing the value. 

Once this message has been printed out then the user should be able to enter another number and then prints another descriptive message.

This should repeat until the user enters `q` to quit the program.

Here are some examples of descriptive messages for different numbers:

- if the user enters 77 then we print `Number is: Odd, Palindrome and NotPrime`
- If the user enters 43 then we print `Number is: Odd, NotPalindrome and Prime`
- if the user enters 44 then we print `Number is: Even, Palendrome and NotPrime`

*Hint:* Think about how you could make use of the above examples in your unit tests. 

## Instructions for reviewers

- Ensure that all three functions should return lambada expressions.
- Ensure that every function is tested.
