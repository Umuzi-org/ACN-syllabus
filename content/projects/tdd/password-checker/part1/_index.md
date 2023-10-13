---
_db_id: 269
content_type: project
flavours:
- any_language
prerequisites:
  hard:
  - projects/tdd/simple-calculator-part1
  - language-agnostic/validate-id-number
  soft: []
ready: true
story_points: 3
submission_type: repo
tags:
- tdd
- error-checking
title: Password strength checker
---

Please note that this is a unit testing project. Make sure you demonstrate a solid understanding of unit testing and test your code using the required framework.

## Set up your environment

### JavaScript


Your directory structure should look like this.

```
├── spec
|   ├── support
|   |   └── jasmine.json
|   └── ???
├── src
|   └── password_checker.js
└── package.json
```

**Note:** It is important that you export all the functions we are asking you to write. Use the following named export syntax:

```
module.exports = { firstFunctionName, secondFunctionName }
```

### Python

Your project is expected to be completed using `pytest`. You are expected to follow industry best practices in all things. This means that you need to have a directory structure that is in good shape. Please name your files and folders like this:

```
├── password_checker   the package under test
│   └── password_checker.py
├── requirements.txt    installation requirements
├── setup.py            installation script for the package under test
└── tests               all package tests go in this directory
    ├── ???

```

Please take a look at this topic to see an explanation of the required directory structure.
{{< contentlink path="topics/python-specific/automated-testing-with-pytest" >}}

### Java

The code you push to git should have the following structure:

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
    |   └── java
    |       └── password_checker
    |           └── PasswordChecker.java <-------- names are important
    └── test
        └── java
            └── ???.java             <-------- names are important
```

Please name your project `password_checker` and put your work in the `password_checker` package.

## Implement a function that calculates the strength of a password

Create a function called `password strength`. This function should take one parameter (the password) and it should return the strength of the password.

Here are criteria that are used for judging the strength of a password:

1. password should not be empty
2. password should be longer than 8 characters
3. password should have at least one lowercase letter
4. password should have at least one uppercase letter
5. password should have at least one digit
6. password should have at least one special character. a special character is a character that is on the keyboard but is not a number or letter. Eg: `{ % & * " '` etc.
7. password should have at least one whitespace character

This is how the strength of the password is calculated 

- If number of conditions met >= 6: return "strong"
- If number of conditions met >= 4: return "medium"
- If number of conditions met == 3: return "weak"
- If conditions 1 or 2 are not met: return "invalid"

**Java learners:** We should not need to instantiate your class in order to call this function. 

## Instructions for reviewers

- For password strength, make sure cases of invalid passwords are checked, for example these passwords are both invalid; `P@ssw 12`, `User1@`.