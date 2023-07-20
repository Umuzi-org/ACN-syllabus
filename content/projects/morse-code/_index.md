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

### Python

```
morse_code.py
```

### JavaScript

Your directory structure should look like this:

```
morse_code.js
```

Remember to export both functions like this:

```
module.exports = { function1Name, function2Name };
```

### Java

Your directory structure should look like this:

```
MorseCode.java       <-------- names are important
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

Make sure your functions can handle empty strings. For example, the following should behave in a predictable way:

```
lettersToMorseCode("") 
morseCodeToLetters("") 
```

Include the following assertions in your code:

- Assert that the output and input both have the same number of characters represented.
- Assert that there are the right number of spaces represented in the output.

## A note on error messages

Errors are useful: They tell you exactly what is broken and where it is broken. It is always worth while to put care into crafting meaningful error messages.

Make sure that if an assertion fails then there is an informative error message.

## Resources

- https://en.wikipedia.org/wiki/Morse_code
- https://morsecode.scphillips.com/translator.html
- https://morsecode.world/international/morse2.html
- https://www.electronics-notes.com/articles/ham_radio/morse_code/characters-table-chart.php

## Remarks

Admittedly, this project is a little bit contrived. Assertions are great for adding runtime checks to values and adding documentation-as-code.

For a problem like this one, unit tests are more appropriate. We'll learn about those in a little while :)
