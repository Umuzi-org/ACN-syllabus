---
_db_id: 273
content_type: project
flavours:
- any_language
learning_outcomes:
- code_tdd
- code_existing_code_update
- code_basic_calculation
pre: '<b>EASY: </b>'
prerequisites:
  hard:
  - topics/test-driven-development
  soft: []
ready: true
story_points: 2
submission_type: repo
tags:
- tdd
title: simple-calculator part 1
---

The objective of this project is to build a calculator that can perform multiplication and addition on multiple integers. Do not build a front-end (UI). Complete this project by using a TDD approach.

The basic TDD approach is as follows:

1. RED: Write tests. It should fail initially because there isn't any code that it is testing.
2. GREEN: Write code to make the tests pass.
3. REFACTOR: Make sure the code is understandable and clean.

Remember to make sure your tests still pass after refactoring them.

## TDD in industry

Test driven development is pretty weird at first, but it's a very effective way to write bug-free and modular code.  

We are introducing this now because it is important! If you practice then it'll become easy.

**If you find yourself writing your functionality and then testing it afterwards: You are doing it wrong!**

## Set up environment

### JavaScript:

Use Jasmine to test your code. _Please do not use the SpecRunner html file_ to test your code. Run Jasmine on the terminal.

- {{< contentlink path="topics/jasmine-unit-tests" >}} . Look under the heading: _Getting set up (like a boss)_ for instructions to set up.

After setting up Jasmine on the terminal, please ensure that your directory has the following:

Your directory structure should look like this:

```
├── spec
|   ├── support
|   |   └── jasmine.json
|   └── simple_calculator_spec.js
├── src
|   └── simple_calculator.js
└── package.json
```

**Note**: Please export your two functions using the following syntax.

```
module.exports = {firstFunctionName, secondFunctionName}
```

### Python

Your project is expected to be completed using pytest. You are expected to follow industry best practices in all things. This means that you need to have a directory structure that is in good shape. Please name your files and folders like this:

```
├── simple_calculator   the package under test
│   └── calculator.py
├── requirements.txt    installation requirements
├── setup.py            installation script for the package under test
└── tests               all package tests go in this directory
    └── test_calculator.py
```

Please take a look at this topic to see an explanation of the required directory structure.

{{< contentlink "topics/python-specific/automated-testing-with-pytest" >}}



### Java

Please make use of Gradle from the command line to set up your project directory. You can learn more about Gradle here:

{{< contentlink "gradle/introduction" >}}



```
    public static int add(....
```

Your directory structure should look like this:


```
├── app
│   ├── build.gradle
│   └── src
│       ├── main
│       │   ├── java
│       │   │   └── calculator << This is the project name
│       │   │       └── Calculator.java
│       │   └── resources
│       └── test
│           ├── java
│           │   └── calculator  
│           │       └── CalculatorTest.java
│           └── resources
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
└── settings.gradle
```

Create a class named `Calculator`. All your methods should be static methods that return integers. Eg:

## 1. Create an add function that can add two integers

Create some tests for a function called `add` that works like this:

```
add(1,2)
// should return 3
add(-1,-1)
// should return -2
```

Then make the tests pass by implementing the function. 

## 2. Modify the add function so that it can add multiple integers.

Update your tests so that the `add` function can accept any number of arguments:

```
add(1,2,3,4,5) // should return 15
add(1,2)       // should still return 3
add(-1,-1)     // should still return -2
add()          // should return 0
```

Please note that your function should _NOT_ expect an array or list of numbers, for example:

```
add([1,2,3,4])
add({1,2,3,4})
```

This is NOT what we are looking for. If you have square brackets inside your round brackets, you are doing it wrong. The same will apply to the multiply function you will build in the next section.

## 3. Create a multiply function that can multiply two integers

Create a function called `multiply` that works like this:

```
multiply(1,3)  // should return 3
multiply(-1,3) // should return -3
```

## 4. Modify the multiply function so that it can multiply multiple integers.

The `multiply` function should now behave like this:

```
multiply(1,2,3,4,5) // should return 120
multiply(1,3)       // should still return 3
multiply(-1,3)      // should still return -3
```

## Instructions for reviewers

- `__init__.py` is not needed if the repo is set up properly (python).
- The point of tests in TDD isn't only to have tests but to have very specific tests. For a given input we don't just want to know that they pass or fail. So instead of one function that tests everything you want specific tests.
- Tests should have descriptive names.
- Built-in functions should not be used in this project.