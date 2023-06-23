---
_db_id: 184
content_type: project
flavours:
  - any_language
learning_outcomes:
  - code_assert_statements
  - code_error_messages
prerequisites:
  hard:
    - topics/intro-to-assertive-programming
  soft: []
ready: true
story_points: 3
submission_type: repo
tags:
  - problem solving
  - data structures
  - defensive programming
title: Morse code
---

## Project structure

### JavaScript

Your directory structure should look like this:

```
├── src
|   └── morse_code.js
└── package.json
```

Remember to export both functions like this:

```
module.exports = { function1Name, function2Name };
```

### Java

Your directory structure should look like this:

```
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    └── main
        └── java
            └── MorseCode.java       <-------- names are important
```

## Instructions

Create two functions:

```
lettersToMorseCode
morseCodeToLetters
```

eg:

```js
lettersToMorseCode("Hi there");
// should return
// ".... .. / - .... . .-. ."

morseCodeToLetters(".... .. / - .... . .-. .");
// should return
// "hi there"
```

Make sure to cater for punctuation marks and all special characters.

Include the following assertions in your code:

- Assert that the output and input both have the same number of characters represented. Use the string `"input and output characters are not equal"` as the assertion error message.
- Assert that there are the right number of spaces represented in the output. Use the string `"input and output space characters are not equal"` as the assertion error message.

Make sure that when you do this, your code remains clean and dry.

## Resources

- https://en.wikipedia.org/wiki/Morse_code
- https://morsecode.scphillips.com/translator.html
- https://morsecode.world/international/morse2.html
- https://www.electronics-notes.com/articles/ham_radio/morse_code/characters-table-chart.php

## Remarks

Admittedly, this project is a little bit contrived. Assertions are great for adding runtime checks to values and adding documentation-as-code.

For a problem like this one, unit tests are more appropriate.

## Up for a challenge?

This is optional.

Add unit tests to your code. Leave the assertions in there, so that we can see you know how to hit the requirements we laid out. But if you have some passing tests as well, that would be sweet.

## Instructions for reviewers

- Ensure that the `lettersToMorseCode` function can convert numbers, special characters and letters of the alphabets to morse code. The `morseCodeToLetters` function can convert morse code to numbers, letters of the alphabets and special characters.
- Make sure that both functions return the output. Neither function should print the output.
- When using assertions make sure that the assert statements are checking if:
  - the input and output character lengths are the same
  - input and output spaces are the same
- If unit tests are used, make sure that there is a test that checks the input and output lengths and ensure that imports and exports were used correctly.
- Make sure an assertion function was used to assert if both functions input and output data are the same.
- Make sure that the assertions do not print an error if empty strings are passed in both functions, for example:

```
lettersToMorseCode("") // shouldn't print an assertion failure
morseCodeToLetters("") // shouldn't print an assertion failure
```
