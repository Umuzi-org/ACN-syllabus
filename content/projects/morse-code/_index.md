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
lettersToMorseCode("Hi there")
// should return
// ".... .. / - .... . .-. ."
```

Include the following assertions in your code:

- assert that the output and input both have the same number of characters represented
- assert that there are the right number of spaces represented in the output

Make sure that when you do this, your code remains clean and DRY. DRY - it's a thing. Google it.

## Resources

- https://en.wikipedia.org/wiki/Morse_code
- https://morsecode.scphillips.com/translator.html

## Remarks

Admittedly this project is a little bit contrived. Assertions are great for adding runtime checks to values and adding documentation-as-code.

For a problem like this one, unit tests are more appropriate. 

## Up for a challenge?

This is optional.

Add unit tests to your code. Leave the assertions in there just so that we can see that you know how to hit the requirements we laid out. But if you have some passing tests as well that would be sweet.

## Instructions for Reviewers

- Ensure that both functions can convert all types of characters to morse code and morse code to all types of characters like alphabets, numbers and special characters.
- When using assertions make sure that the assert statements are checking if the input and output lengths and input and output spaces are the same by checking if they are equal.
- Make sure that the assertions does not print an error if empty strings are passed in both functions, e.g 
```
lettersToMorseCode("") // shouldn't print an assertion failure
morseCodeToLetters("") // shouldn't print an assertion failure
```
- If Unit tests are used, make sure that there is a test that checks input and output lengths.