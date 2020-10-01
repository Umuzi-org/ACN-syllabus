---
_db_id: 266
available_flavours:
- any_language
content_type: project
prerequisites:
  hard:
  - projects/tdd/simple-calculator-part1
  soft: []
ready: true
submission_type: repo
tags:
- tdd
- regular-expressions
title: string-calculator
---

## Set up your environment

### Javascript

Please test your code using jasmine.

Your directory structure should look like this.

```
    >node_modules    <---- make sure this is in your .gitignore
    >spec
        > support
            - jasmine.json
        - string_calculator_spec.js
    >src
        - string_calculator.js
    - package.json
```

### Python

Your project is expected to be completed using pytest. You are expected to follow industry best practices in all things. This means that you need to have a directory structure that is in good shape. Please name your files and folders like this:

```
├── string_calculator   the package under test
│   └── calculator.py
├── requirements.txt    installation requiremnts
├── setup.py            installation script for the package under test
└── tests               all package tests go in this directory
    └── test_calculator.py
```

Please take a look at this topic to see an explanation of the required directory structure.
{{%contentlink "topics/python-specific/automated-testing-with-pytest" %}}

## Instructions

Before you commence, first read through {{% contentlink path="/topics/data_validation_and_verification/" %}}. Upon completion, read through {{% contentlink path="/topics/regular-expressions/" %}}.

Please note that this project should be done in a TDD manner.

#### 1. Create an add function that can handle up to two integers passed in as a string.

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

#### 2. Modify the add function to handle multiple integers.

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

#### 3. Modify the add function so that it can handle new lines between integers.

```
add("1\n2,3" )
// should return 6
```

#### 4. Modify the add function so that it can handle different delimeters.

Delimiters will be specified in the following manner:

- **"//[delimiter]\n[numbers…]"**, the default delimiter will be in the beginning of the string just before a new line character ("\n").For example:

```
add("//;\n1;2")
// should return 3

add("//4\n142")
// should return 3
```

In the first case, the default delimiter is: ";".

In the second case, the default delimiter is: "4".

#### 5. Modify the add function so that it can handle negative integers.

If a negative number is passed into the add function it should throw this exception:
`"negatives not allowed"`

The exception should contain a list of all the negative integers that were passed into the add function.

For example:

```
add("-1,-2,3,4")
// should throw the following:
    'ERROR: negatives not allowed -1,-2'
```

#### 6. Modify the add function so that it ignores integers greater than or equal to 1000.

```
add("//;\n1000;1;2")
// should return 3
```

#### 7. Modify the add function so that it can support delimiters of any length

As long as the string passed in satisfies this format, "//[delimiter]\n[integers...]", which was explained above. The add function should be able to handle it.
For example:

```
add("//***\n1***2***3")
// should return 6
```

#### 8. Modify the add function so that it is able to support different delimiters of any length

As long as the string passed into the add function follows this format, "//[delim1][delim2]\n[integers...]", the add function should be able to handle it:

For example:

```
add("//[:D][%]\n1:D2%3")
// should return 6

add("//[***][%%%]\n1***2%%%3")
// should return 6

add("//[(-_-')][%]\n1(-_-')2%3")
// should return 6

add("//[abc][777][:(]\n1abc27773:(1")
// should return 7

```

#### 9. Modify the add function so that it can handle invalid input.

If the string passed in is invalid, your code should be able to detect this and throw an error.

Hint: A valid string input follows these formats:

```md
- "integer,integer,integer" e.g "1,2" or "1,2,3,4"

- "integer \n integer,integer e.g "1\n2,3"

- "//delimiter \n integer delimiter integer" e.g "//;\n1;2"

- "//[delimiter][delimiter]\n integer delimiter integer" e.g "//[\*][%]\n1\*2%3"
```

If the string doesn't abide by any of these formats, it should be considered invalid.

```
add("//;\n1000;1;2;")
// should throw the following:
    'ERROR: invalid input'

add("   //;\n1000,1;2")
// should throw the following:
    'ERROR: invalid input'

add("1,2,3//;\n1000,1;2")
// should throw the following:
    'ERROR: invalid input'

```

### why is this important?

- If you're wondering to yourself, "Why is this sooo important!?" take a look at {{% contentlink path="/topics/data_validation_and_verification/" %}}