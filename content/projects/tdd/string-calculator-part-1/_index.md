---
_db_id: 266
content_type: project
flavours:
- any_language
prerequisites:
  hard:
  - projects/tdd/simple-calculator-part1
  soft: []
ready: true
submission_type: repo
tags:
- tdd
- regular-expressions
title: string-calculator part 1
---

## Set up your environment

### JavaScript

Please test your code using jasmine.

Your directory structure should look like this.

Make sure that the `node_modules` are in your `.gitignore` file.

```
├── src/
|   └── string _calculator.js
├── spec/
|   ├── support/
|   |   └── jasmine.json
|   └── string_calculator_spec.js
└── package.json
```

### Python

Your project is expected to be completed using pytest. You are expected to follow industry best practices in all things. This means that you need to have a directory structure that is in good shape. Please name your files and folders like this:

```
├── string_calculator   the package under test
│   └── calculator.py
├── requirements.txt    installation requirements
├── setup.py            installation script for the package under test
└── tests               all package tests go in this directory
    └── test_calculator.py
```

Please take a look at this topic to see an explanation of the required directory structure.
{{< contentlink "topics/python-specific/automated-testing-with-pytest" >}}

### Java

Please use junit to test your code https://www.guru99.com/junit-test-framework.html

```
├── src
    └── main
    |   └── java
    |       └── StringCalculator
    |       └── Main    
    └── test
        └── java
           └── StringCalculatorTest

```

## Instructions

Before you commence, first read through {{< contentlink path="/topics/data_validation_and_verification/" >}}. Upon completion, read through {{< contentlink path="/topics/regular-expressions/" >}}.

Please note that this project should be done in a TDD manner.

#### 1. Create an add function that can handle up to two integers passed in as a string

Create a function called `add()` that takes in a string as a parameter and behaves in the following way:

```
add("")
// should return 0

add("1")
// should return 1

add("1,1")
// should return 2

```

_Note: The output that the function returns should be an integer and not a string._

#### 2. Modify the add function to handle multiple integers

```
add("1,2,3,4")
// should return 10

add("")
// should still return 0

add("1")
// should still return 1

add("1,1")
// should still return 2
```

As you keep adding more functionality to your code always make sure that the previous functionality you implemented still works flawlessly. Keep this in mind as you continue to modify your code.

#### 3. Modify the add function so that it can handle newlines between integers

```
add("1\n2,3" )
// should return 6
```

#### 4. Modify the add function so that it can handle different delimiters

Delimiters will be specified in the following manner:

- **"//[delimiter]\n[numbers…]"**, the default delimiter will be in the beginning of the string just before a newline character ("\n"). For example:

```
add("//;\n1;2")
// should return 3

add("//4\n142")
// should return 3

add("//;\n1")
// should return 1

add("//;\n")
// should return 0
```

In the first case, the default delimiter is: ";".

In the second case, the default delimiter is: "4".

**Note:** you are not expected to handle integer delimiters where the delimiter and the digit you are adding are the same. For example

```
add("//4\n14244")
add("//88\n18882")
```

Strings like these should raise an error, `'ERROR: invalid input'`. When this isn't the case, your function should work as explained above;

```
add("//88\n18820882")
// should return 23
```

**Python:** Raise an appropriate exception type. Using the base Exception isn't good practice. Here are [errors](https://www.tutorialsteacher.com/python/error-types-in-python) that can be raised.

#### 5. Modify the add function so that it can handle negative integers

If a negative number is passed into the add function it should throw this exception:
`"negatives not allowed"`

The exception should contain a list of all the negative integers that were passed into the add function.

For example:

```
add("-1,-2,3,4")
// should throw the following:
    'ERROR: negatives not allowed -1,-2'
```

#### 6. Modify the add function so that it can support delimiters of any length

As long as the string passed in satisfies this format, "//[delimiter]\n[integers...]", which was explained above. The add function should be able to handle it.
For example:

```
add("//***\n1***2***3")
// should return 6
```


### Why is this important?

- If you are wondering, "Why is this so important!?" take a look at {{< contentlink path="/topics/data_validation_and_verification/" >}}

## Instructions for reviewers

- Proper TDD to be followed. Mocks and Spies are not needed for this project.

- Proper error handling to be used. no `print`/`console.log`. an exception is to be thrown when needed and a value returned when needed.

- Ensure that the add function takes a string as an argument.

- The function that needs to be constantly updated is the `add()` function. It is even better if the `add()` function relies on other tiny functions.

- An understanding of regular expression methods should be demonstrated within the project.
