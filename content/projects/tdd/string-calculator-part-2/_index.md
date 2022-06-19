---
content_type: project
flavours:
- python
prerequisites:
  hard:
  - projects/tdd/string-calculator-part-1
  soft: []
ready: true
from_repo: projects/tdd/string-calculator-part-1
submission_type: continue_repo
tags:
- tdd
- regular-expressions
title: string-calculator part 2
---

This a continuation of {{% contentlink path="projects/tdd/string-calculator-part-1" %}}. All the functionality developed there should still work here.


## Instructions

Please note that this project should be done in a TDD manner.


### 1. Modify the add function so that it ignores integers greater than or equal to 1000

```
add("//;\n1000;1;2")
// should return 3
```

### 2. Modify the add function so that it can support different delimiters of any length

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

### 3. Modify the add function so that it can handle invalid input

If the string passed in is invalid, your code should be able to detect this and throw an error.

Hint: A valid string input follows these formats:

```md
- "integer,integer,integer" e.g "1,2" or "1,2,3,4"

- "integer \n integer,integer e.g "1\n2,3"

- "//delimiter \n integer delimiter integer" e.g "//;\n1;2"

- "//[delimiter][delimiter]\n integer delimiter integer" e.g "//[\*][%]\n1\*2%3"
```

If the string does not abide by any of these formats, it should be considered invalid. Square brackets (`[` or `]`) are used as identifiers, and will not be used as delimiters. Any string with these as delimiters should also be considered invalid.

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

add("//]\n90]11]20")
// should throw the following:
    'ERROR: invalid input'

add("//[[][[][&&]\n1[2[3&&4")
// should throw the following:
    'ERROR: invalid input'

```


## Instructions for reviewers

- Proper TDD to be followed. Mocks and Spies are not needed for this project.

- Proper error handling to be used. no `print`, an exception is to be thrown when needed and a value returned when needed.

- All functionality from part 1 should still work.

- An understanding of regular expression methods should be demonstrated within the project.
