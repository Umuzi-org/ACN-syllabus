---
_db_id: 184
content_type: project
flavours:
- any_language
prerequisites:
  hard:
  - topics/intro-to-asserive-programming
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

Create two functions:

```
lettersToMorseCode
morseCodeToLetters
```

eg:

```
lettersToMoreseCode("Hi there")
// should return
// ".... .. / - .... . .-. ."
```

Make sure to cater for punctuation marks and all special characters.

Include the following assertions in your code:

- assert that the output and input both have the same number of characters represented
- assert that there are the right number of spaces represented in the output

Make sure that when you do this, your code remains clean and DRY. DRY - it's a thing. Google it.

## Resources

- https://en.wikipedia.org/wiki/Morse_code
- https://morsecode.scphillips.com/translator.html
- https://www.electronics-notes.com/articles/ham_radio/morse_code/characters-table-chart.php

## Remarks

Admittedly this project is a little bit contrived. Assertions are great for adding runtime checks to values and adding documentation-as-code.

For a problem like this one, unit tests are more appropriate. 

## Up for a challenge?

This is optional.

Add unit tests to your code. Leave the assertions in there just so that we can see that you know how to hit the requirements we laid out. But if you have some passing tests as well that would be sweet.