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
  - topics/test-driven-development-questions
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

Remember to make sure your tests still pass after any refactoring.

## Set up environment

### JavaScript

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

**Note**: Please export your two functions using the following syntax at the end of the code:

```
module.exports = {firstFunctionName, secondFunctionName}
```

### Python

Your project is expected to be completed using pytest. 

Please name your files and folders like this:

```
├── simple_calculator   the package under test
│   └── calculator.py
├── requirements.txt    installation requirements
├── setup.py            installation script for the package under test
└── tests               all package tests go in this directory
    └── test_calculator.py
```

Please take a look at this topic to see an explanation of the required directory structure.

{{< contentlink path="topics/python-specific/automated-testing-with-pytest" >}}

### Java

Make use of Gradle from the command line to set up your project. You can learn more about Gradle here:

{{< contentlink path="gradle/introduction" >}}

Your directory structure should look like this:


```
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    ├── main
    │   └── java
    │       └── Calculator.java       <-------- names are important
    └── test
        └── java
            └── CalculatorTest.java   <-------- names are important
```

Create a class named `Calculator`. All your methods should be static methods that have integer arguments and return integers. Eg:

```
    public static int add(....
```

## 1. Create an add function that can add two integers

Write some unit tests for a function named `add` that works like this:

```
add(1,2)
// should return 3
add(-1,-1)
// should return -2
```

When you run your tests, they should fail.

Now write enough code to make your tests pass.

## 2. Modify the add function so that it can add multiple integers.

Write some more tests that expect the `add` function to behave like this:

```
add(1,2,3,4,5)
// should return 15
add(1,2)
// should still return 3
add(-1,-1)
// should still return -2
```

Please note that your function should _NOT_ expect an array or list of numbers, for example:

```
add([1,2,3,4])  # incorrect
add({1,2,3,4})  # incorrect
add(1,2,3,4)    # correct
```

This is NOT what we are looking for. If you have square brackets inside your round brackets, you are doing it wrong. The same will apply to the multiply function you will build in the next section.

Now make your tests pass.

## 3. Create a multiply function that can multiply two integers

Keep following a TDD approach for the rest of this project.

Create a function called `multiply` that works like this:

```
multiply(1,3)
// should return 3
multiply(-1,3)
// should return -3
```

## 4. Modify the multiply function so that it can multiply multiple integers.

The `multiply` function should now behave like this:

```
multiply(1,2,3,4,5)
// should return 120
multiply(1,3)
// should still return 3
multiply(-1,3)
// should still return -3
```

## Instructions for reviewers

- `__init__.py` is not needed if the repo is set up properly (python).
- For a given input we don't just want to know that the function executed without error, the tests should make sure it returns the right thing. 
- Separate tests should be in separate test functions, there should not be one mega-test function that contains all the test code.
- Tests should have descriptive names.
- Built-in functions should not be used in this project.