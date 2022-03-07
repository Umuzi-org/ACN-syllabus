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
title: password-checker
---

## Set up your environment

### Javascript

Please note that this is a unit testing project. Make sure you demonstrate a solid understanding of unit testing and test your code using the required framework.

Your directory structure should look like this.

```
    >node_modules    <---- make sure this is in your .gitignore
    >spec
        > support
            -jasmine.json
        - password_is_valid_spec.js
        - password_strength_spec.js
    >src
        - password_checker.js
    - package.json
```

### Python

Your project is expected to be completed using `pytest`. You are expected to follow industry best practices in all things. This means that you need to have a directory structure that is in good shape. Please name your files and folders like this:

```
├── password_checker   the package under test
│   └── password_checker.py
├── requirements.txt    installation requirements
├── setup.py            installation script for the package under test
└── tests               all package tests go in this directory
    ├── test_password_is_valid.py
    └── test_password_strength.py
```

Please take a look at this topic to see an explanation of the required directory structure.
{{% contentlink path="topics/python-specific/automated-testing-with-pytest" %}}

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
    |       └── PasswordChecker.java <-------- names are important
    └── test
        └── java
            └── ???.java             <-------- names are important
```

Please refer to the following to find out more: {{% contentlink path="topics/java-specific/project-submission-requirements" %}}

## Instructions

Implement the following function by following a TDD methodology:

```
// Javascript:
passwordIsValid(password)
```

```
// Java:
passwordIsValid(password)
```

```
# Python:
password_is_valid(password)
```

`password_is_valid` will check if the password meets a few different conditions. If one of the below conditions is not met then the relevant error/exception should be thrown/raised (python: make use of ValueError). Your error/exception message should match one of the following conditions exactly (word-for-word).

1. password should exist
2. password should be longer than 8 characters
3. password should have at least one lowercase letter
4. password should have at least one uppercase letter
5. password should have at least have one digit
6. password should have at least one special character
7. password should have at least one whitespace character

In the case of (6) above, a special character is a character that is on the keyboard but is not a number or letter. Eg `{ % & * " '` etc

Next, implement a function called "password strength":

```
// Javascript:
passwordStrength(password)
```

```
// Java:
passwordStrength(password)
```

```
# Python:
password_strength(password)
```

This function should count the number of conditions met and then return a string that describes the strength of the password. Valid strings are "invalid", "weak", "medium" and "strong".

- If number of conditions met >= 6: return "strong"
- If number of conditions met >= 4: return "medium"
- If number of conditions met == 3: return "weak"
- If conditions 1 or 2 are not met: return "invalid"

## Note on DRY code

Please don't re-implement the same check in two different places. Good code is DRY. Every piece of knowledge should be represented once in your code.

## JS Resources

- [JS Errors](https://www.w3schools.com/js/js_errors.asp)
- [Errors and Jasmine](https://stackoverflow.com/questions/4144686/how-to-write-a-test-which-expects-an-error-to-be-thrown-in-jasmine)

## Python Resources

- [Python Errors](https://www.codementor.io/sheena/how-to-write-python-custom-exceptions-du107ufv9?referral=sheena-kvo1e6ewh)
- [Exceptions and Pytest](https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest)

## Java Resources

- https://howtodoinjava.com/junit5/expected-exception-example/

## Instructions for reviewers

- For password strength, make sure cases of invalid passwords are checked, for example these passwords are both invalid; `P@ssw 12`, `User1@`.  
- Actual passwords should never be printed to the terminal, for example in assert messages or when raising exceptions.