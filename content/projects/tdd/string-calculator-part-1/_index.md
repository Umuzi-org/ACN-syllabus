---
_db_id: 266
content_type: project
flavours:
- any_language
prerequisites:
  hard:
  - projects/tdd/simple-calculator-part1
  - topics/data_validation_and_verification
  - topics/regular-expressions
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
|   └── string_calculator.js
├── spec/
|   ├── support/
|   |   └── jasmine.json
|   └── ???
└── package.json
```

**Note**: Please export your function using the following syntax at the end of the code:

```
module.exports = {functionName}
```

### Python

Your project is expected to be completed using pytest.

Please name your files and folders like this:

```py
├── string_calculator   # the package under test
│   └── string_calculator.py
├── requirements.txt    # installation requirements
├── setup.py            # installation script for the package under test
└── tests               # all package tests go in this directory
    └── ???
```

Please take a look at this topic to see an explanation of the required directory structure.
{{< contentlink "topics/python-specific/automated-testing-with-pytest" >}}

### Java

Please make use of Gradle from the command line to set up your project. You can learn more about Gradle here:

{{< contentlink path="gradle/introduction" >}}

The code you push to git should have the following structure:

When you use gradle to create your project, give your project the following name: `string_calculator`

```
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── app
    ├── build.gradle
    └── src
        ├── main
        |   └── java
        |       └── string_calculator
        |           └── StringCalculator.java       <-------- names are important
        └── test
            └── java
                └── string_calculator
                    └── ???.java
                
```

## Instructions

Please note that this project should be done in a TDD manner.

### 1. Create an add function that can handle up to two integers passed in as a string

The `add` function should take in one string parameter and return an integer.

**Note:** This is a TDD project. That means that you should write a test, then get that test to pass, then write the next test, etc.

**Java learners:** We should not need to instantiate your `StringCalculator` class in order to call `add`.

```
add("")
// should return 0

add("1")
// should return 1

add("123")
// should return 123

add("1,1")
// should return 2

```

### 2. Modify the add function to handle multiple integers

```
add("1,2,3,4")
// should return 10

add("")
// should still return 0

add("1")
// should still return 1

add("123")
// should still return 123

add("1,1")
// should still return 2
```

As you keep adding more functionality to your code always make sure that the previous functionality you implemented still works flawlessly. Keep this in mind as you continue to modify your code.

### 3. Modify the add function so that it can handle newlines between integers

```
add("1\n2,3" )
// should return 6
```

### 4. Modify the add function so that it can handle custom delimiters

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

#### The snippets below with a **Note** are considered invalid, and will be dealt with in part 2 of this project

**Note:** you are not expected to handle integer delimiters where the delimiter and the digit you are adding are next to each other. Example:

```
add("//88\n18882")
```

**Note:** You are also not expected to handle integer delimeters where the delimeter is at the start and or end of the list of integers. Example:

```
// These input are invalid

// start
add("//4\n434243")

// end
add("//4\n342434")

// start and end
add("//4\n4342434")
```

They are considered invalid and more will be dealt with in part 2 of the project.

### 5. Modify the add function so that it can handle negative integers

If a negative number is passed into the add function it should throw this error/exception:
`negatives not allowed {comma separated list of negative integers found}`

The exception should contain a list of all the negative integers that were passed into the add function.

For example:

```
add("-1,-2,3,4")
// should throw the following:
    'negatives not allowed -1,-2'
```

**Python:** Raise an appropriate exception type. Using the base Exception isn't good practice. Here are [errors](https://www.tutorialsteacher.com/python/error-types-in-python) that can be raised.

### 6. Modify the add function so that it can support delimiters of any length

As long as the string passed in satisfies this format, "//[delimiter]\n[integers...]", which was explained above. The add function should be able to handle it.
For example:

```
add("//***\n1***2***3")
// should return 6
```

**Note:** You are not expected to handle delimeters where the delimeter is at the start and or end of the list of integers. Example:

```
// These are considered invalid

// start
add("//***\n***1***2***3")

// end
add("//***\n1***2***3***")

// start and end
add("//***\n***1***2***3***")

```

They are considered invalid and more will be dealt with in part 2 of the project.

## Instructions for reviewers

- Proper TDD to be followed
- Mocks and Spies are not needed for this project.
- Proper error handling to be used. No `print`/`console.log`. An exception is to be thrown when needed and a value returned when needed.
- Ensure that the add function takes a string as an argument.
- The function that needs to be constantly updated is the `add()` function. It is even better if the `add()` function relies on other tiny functions.
- An understanding of regular expressions should be demonstrated within the project
- Remember that examples with a **Note** should not be used to test for functionality in this project