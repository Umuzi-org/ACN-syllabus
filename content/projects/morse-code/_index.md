---
_db_id: 184
content_type: project
flavours:
- any_language
prerequisites:
  hard: []
  soft: []
ready: true
story_points: 3
submission_type: repo
tags:
- problem solving
- data structures
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
MorseCode.java       
```

## Instructions

Create two functions:

1. `letters to morse code` - this should take in a string and return a string.

For example if you pass in "Hi there", it should return ".... .. / - .... . .-. ."

2. `morse code to letters` - this should do the reverse of `letters to morse code`

Make sure to cater for punctuation marks and all special characters.

Make sure your functions can handle empty strings. For example, the following should behave in a predictable way:

```
lettersToMorseCode("") 
morseCodeToLetters("") 
```
## Resources

- https://en.wikipedia.org/wiki/Morse_code
- https://morsecode.scphillips.com/translator.html
- https://morsecode.world/international/morse2.html
- https://www.electronics-notes.com/articles/ham_radio/morse_code/characters-table-chart.php