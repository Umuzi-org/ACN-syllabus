---
_db_id: 371
content_type: topic
nqf: ncit
ready: false
tags:
- tdd
title: Test-driven development
unit_standards:
- 115359
- 115384
---

## 1. Errors

Error is an inevitable part of developing software. Discovering where your errors are and how to fix them can be one of the most frustrating (and rewarding) parts of being a developer. Let’s take a look at the various types of errors you will encounter so you can be better equipped to fix them.


There are three basic types of program errors.


**Syntax errors**

These are the easiest errors to deal with because your console will usually tell you right away if there is a syntax error. A syntax error occurs when you don’t follow the rules of your programming language. If you make a mistake in how you type a variable or function name (especially a function built in to JavaScript), then the program will end and the console will throw an error message


**Semantic errors**

If there is a semantic error in your program, it will run successfully in the sense that the computer will not generate any error messages. However, your program will not do the right thing. It will do something else. Specifically, it will do what you told it to do. The problem is that the program you wrote is not the program you wanted to write. The meaning of the program (its semantics) is wrong. Identifying semantic errors can be tricky because it requires you to work backward by looking at the output of the program and trying to figure out what it is doing.


**Logic errors**

Logic errors are the hardest ones to debug. They occur when the result the program produces doesn’t match the result you expect it to produce. Most of the time, logic errors are found in the process. Logic errors occur when you implement the algorithm for solving the problem incorrectly. The key to fixing logic errors is to be able to reproduce the error consistently. A repeatable logic error is much easier to track down and fix than an error that appears to be occurring randomly.


One of the ways to find these type of errors is to output the program's relevant variables to the console [calling console.log(myVar) at strategic points in your code] in order to find where the error is in your program. Although this will not work in all cases, it is the easiest way to find the problem if the program produces incorrect results because of an error in logic.

_______

Apart from these errors in your code, it’s possible to encounter errors when you are working with extreme numbers:


**Overflow error**

An error that occurs when the computer attempts to handle a number that is too large for it. Every computer has a well-defined range of values that it can represent. If during execution of a program it arrives at a number outside this range, it will experience an overflow error.


**Underflow error**

The term arithmetic underflow (or "floating point underflow", or just "underflow") happens when the result of a calculation is a number of smaller absolute value than the computer can actually represent in memory on its CPU.


**Conversion error**

When you are converting one type of data to another, errors can often occur. For example, you may find there are errors when you convert a CSV file to an Excel file (or XML to Word). There are no shortage of issues when you are trying to share files between programs, or convert a file type from one program to another.

2. Detecting errors through testing

Now that you’ve seen the types of errors you will deal with as you develop programs, let’s take a look at how we can find these errors and fix them. And most importantly, let’s find a method to minimise the number of errors we make in the first place.


Testing is a huge topic in computer programming. We’ll start by outlining a few basic categories of testing and then introduce the concept of Test-Driven Development.


**Unit Testing**

A great way to isolate errors (and sometimes catch them before they appear) is with unit testing. Unit testing is testing a section of your code, usually a function, that will always give you the same answer with a given input. You test the function with many types of input and check that the output is what you expect each time. There are numerous JavaScript packages that help with unit testing. We’ll try one or two of these out later.


**Integration Testing**


Once you have good unit tests in place, it's time to bring the working parts of your code into a functioning whole with integration testing. Integration tests ensure that various units work together correctly. Integration tests are similar to unit tests, but there’s one big difference: while unit tests are isolated from other components, integration tests are not. For example, a unit test for database access code would not talk to a real database, but an integration test would.


Integration testing is mainly useful for situations where unit testing is not enough. Sometimes you need to have tests to verify that two separate systems – like a database and your app – work together correctly, and that calls for an integration test.


**Functional Testing**


Functional testing is defined as the testing of complete functionality of some application. In practice, with web apps, this means using some tool to automate a browser, which is then used to click around on the pages to test the application.


You might use a unit test to test an individual function and an integration test to check that two parts of the program play nice. Functional tests are on a whole other level. While you can have hundreds of unit tests, you usually want to have only a small amount of functional tests. This is mainly because functional tests can be difficult to write and maintain due to their very high complexity. They also run very slowly, because they simulate real user interaction on a web page, so even page load times become a factor.

## 3. Test-driven development

Check out the following tutorial which teaches the basics of TDD in 30 minutes. There are lots of bonus lessons, including some that use Node.js, which you are encouraged to go through as well. **Don't just read it! Actually download the testing libraries and code it yourself.**


https://github.com/dwyl/learn-tdd


Want more examples? Here’s another great TDD tutorial that focuses on using APIs and HTML.


https://jrsinclair.com/articles/2016/gentle-introduction-to-javascript-tdd-intro/


As these tutorials state, using test-driven development may seem like extra work at first, but the benefits are enormous, especially for larger projects. TDD helps you think through the requirements of your program, and breaks it into bite-sized pieces which makes it more fun to develop and less prone to error.