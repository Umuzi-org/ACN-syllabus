---
_db_id: 625
content_type: project
flavours:
- any_language
learning_outcomes:
- code_validation
- code_problem_decomposition
- code_algorithmic_thinking
- code_tdd
prerequisites:
  hard:
  - projects/tdd/simple-calculator-part1
ready: true
submission_type: repo
tags:
- tdd
- problem-solving
- validation
title: Validate a South African ID number
---

In this project, we'll be practising Test Driven Development while solving a validation problem.

Please make sure that you commit your code often! At least every time you get one of your tests to pass. Also please make sure you make your git commit messages meaningful.

## Set up your environment

### Javascript

Your directory structure should look like this:

```
├── spec
|   ├── support
|   |   └── jasmine.json
|   └── ???
├── src
|   └── validate_sa_id.js
└── package.json
```

**Note**: Please export your function using the following syntax at the end of the code:

```
module.exports = {firstFunctionName}
```

### Python

Your directory structure should look like this:

```
├── validate_sa_id
│   └── validate_sa_id.py
├── setup.py
├── requirements.txt
├── .gitignore
└── tests
    └── test_validate_sa_id.py
```

### Java

Please make use of Gradle from the command line to set up your project directory. You can learn more about Gradle here:

{{< contentlink "gradle/introduction" >}}

When you use gradle to create your project, give your project the following name: `validate_sa_id`.

Your directory structure should look like this:

```
├── app
│   ├── build.gradle
│   └── src
│       ├── main
│       │   ├── java
│       │   │   └── validate_sa_id << This is the project name
│       │   │       └── ValidateSaId.java
│       │   └── resources
│       └── test
│           ├── java
│           │   └── validate_sa_id  
│           │       └── ValidateSaIdTest.java
│           └── resources
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
└── settings.gradle
```

Create a class named `ValidateSaId`. Your `isIdNumberValid` function should be a `static` method and it should return a boolean value.

## Validation problems

As a coder, you will often be asked to validate things. For example, you might be getting data from a crazy CSV file and you could be given the instruction: get all the valid South African cellphone numbers. Or you might need to help users choose a valid password (e.g. the password needs to be more than 6 characters and some other conditions). You might need to check that the email addresses given to you are valid. Or any number of other things.

Validating data is pretty easy when you get the hang of it.

Generally, the procedure would be something like this;

This is the pseudocode:

```
function validate_stuff(stuff){

    if not meets_first_validation_condition(stuff)
        throw error
    if not meets_second_validation_condition(stuff)
        throw error
    if not meets_third_validation_condition(stuff)
        throw error
    etc... until all the conditions have been checked
    return "Stuff is valid!"
}

```

So if you are given a validation problem to solve, your first job would be to break the logic down into all the different conditions that you would need to check. Then you check the conditions one by one. Then if no condition fails the input is valid.

Concrete example: Write a function that takes in a South African phone number. It needs to check if the phone number is valid. Note that the number will have no spaces, dashes, plus sign or anything else. Also note that the country code in South Africa is '27', so all phone numbers need to start with '27'. It'll just be a string of numbers. E.g. "27829873476" is a valid number.

Your function would look a bit like this (pseudocode):

```
function validate_phone_number(phone_number){
    if the phone number doesnt start with +27:
        throw an error
    if the phone number is not the right length:
        throw an error
    if the phone number contains characters that aren't numbers:
        throw an error

    return "phone number is valid"
}

```

## Your mission

Write a function called `is id number valid` that validates South African ID numbers. Make sure the name of the function is according to the common naming conventions for the language you are using.

The function should accept a string parameter, and return a boolean value.

If the ID number is valid then return true, if it is not valid then return false.

A South African ID number is a 13-digit number that is defined by the following format: YYMMDDSSSSCAZ.

- The first 6 digits (YYMMDD) are based on your date of birth. 20 February 1992 is displayed as 920220.
- The next 4 digits (SSSS) are used to define your gender. Females are assigned numbers in the range 0000-4999 and males from 5000-9999.
- The next digit (C) shows if you're an SA citizen status with 0 denoting that you were born an SA citizen and 1 denoting that you're a permanent resident.
- The last digit (Z) is a checksum digit – used to check that the number sequence is accurate using a set formula called the Luhn algorithm.

### Follow this procedure

Note that we'll be following a TDD approach. This means you need to write a test, make the test pass, then write the next test, etc. Here are the first few steps of the process:

The TDD procedure is often summarised as RED, GREEN, REFACTOR.

- RED = write a test. The test should fail.
- GREEN = write just enough code to make the test pass.
- REFACTOR = if your code is messy, clean it up and make sure all the tests still pass.

#### Step 1:

Write a test that expects your validator to return True if it is passed any of the following ID numbers: `2001014800086`, `2909035800085`

Pseudocode:

```
expect isIdNumberValid("2001014800086") to be True
expect isIdNumberValid("2909035800085") to be True
```

Run your test. It should fail (RED).

#### Step 2:

Write enough code to make your test pass.

Pseudocode:

```
function isIdNumberValid(id_number){
    return True
}

```

Run your tests again. Everything is GREEN now.

#### More steps

1. Write a test that expects your validator to return False if you pass it a string that is too short.
2. Make the test pass. Note that ALL your previous tests should still pass.
3. Write a test that expects your validator to return False if you pass it a string that is too long.
4. Make the test pass. Note that ALL your previous tests should still pass.
5. Write a test that expects your validator to return False if you pass it a string that contains characters that aren't numbers. Eg '20010A4800086' should fail.
6. Make the test pass.

#### Keep going

Now it starts to get more interesting. Each of the digits in the ID number means different things and has different validation logic.

1. Use TDD to implement validation logic for the 2 digits denoting the year.
2. Use TDD to implement validation logic for the 2 digits denoting the month.
3. Use TDD to implement validation logic for the 2 digits denoting the day.

And keep going until you've validated everything.