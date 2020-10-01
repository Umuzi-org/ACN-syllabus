---
_db_id: 273
available_flavours:
- any_language
content_type: project
pre: '<b>EASY: </b>'
prerequisites:
  hard:
  - projects/basic-flow-control-katas-assertive
  - topics/test-driven-development
  soft: []
ready: true
story_points: 2
submission_type: repo
tags:
- tdd
title: simple-calculator part 1
---

The objective of this project is to build a calulator that can perform multiplication and addition on multiple integers. Do not build a front-end (UI). Complete this project by using a TDD approach.

The basic TDD approach is as follows:

1. RED: Write tests. It should fail initially because there isn't any code that it is testing.
2. GREEN: Write code to make the tests pass.
3. REFACTOR: Make sure code is understandable and clean.

Remember to make sure your tests still pass after refactoring it.

## Set up environment

### JavaScript:

Use Jasmine to test your code. _Please do not use the SpecRunner html file_ to test your code. Run Jasmine on the terminal.

- {{% contentlink path="topics/jasmine-unit-tests" %}} . Look under the heading: _Getting set up (like a boss)_ for instructions to set up.

After setting up Jasmine on the terminal, please ensure that your directory has the following:

- A src folder that has a file called:

  - simple_calculator.js <---- this is where you will implement all your functionality.

- A spec folder that has a file called:
  - simple_calculator_spec.js <---- this is where you will put your tests.

Your directory structure should look like this:

```
    >node_modules    <---- make sure this is in your .gitignore
    >spec
        > support
            - jasmine.json
        - simple_calculator_spec.js
    >src
        - simple_calculator.js
    - package.json
```

### Python

Your project is expected to be completed using pytest. You are expected to follow industry best practices in all things. This means that you need to have a directory structure that is in good shape. Please name your files and folders like this:

```
├── simple_calculator   the package under test
│   └── calculator.py
├── requirements.txt    installation requiremnts
├── setup.py            installation script for the package under test
└── tests               all package tests go in this directory
    └── test_calculator.py
```

Please take a look at this topic to see an explanation of the required directory structure.
{{%contentlink "topics/python-specific/automated-testing-with-pytest" %}}

### Java

You'll be using IntelliJ, Gradle and JUnit to pull this off.

Create a class named `Calculator`. All your methods should be static methods that return integers. Eg:

```
    public static int add(....
```

Please make sure that you make proper use of gitignore. We don't want your junk files. The git repo you give us should have a file hierarchy that looks like this:

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

Please refer to the following to find out more: {{% contentlink path="topics/java-specific/gradle-and-intellij-project-structure" %}}

## 1. Create an add function that can add two integers

Create a function called `add` that works like this:

```
add(1,2)
// should return 3
add(-1,-1)
// should return -2
```

## 2. Modify the add function so that it can add multiple integers.

The `add` function should now behave like this:

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
add([1,2,3,4])
```

This is NOT what we are looking for. If you have square brackets inside your round brackets, you are doing it wrong. The same will apply for the multiply function you will build in the next section.

## 3. Create a multiply function that can multiply two integers

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
mutilply(1,2,3,4,5)
// should return 120
multiply(1,3)
// should still return 3
multiply(-1,3)
// should still return -3
```