---
_db_id: 786
content_type: topic
prerequisites:
  hard:
  - file-and-directory-naming/general
ready: true
tags:
- File and directory naming
title: File and directory naming in JavaScript
---

## How should I name my JavaScript files and directories?

When thinking about how to name files and directories in JavaScript, please keep consistency and readability in mind. With that said, please make sure to to follow examples in the project instructions if any were given (e.g. {{< contentlink path="projects/oop/animals/part2" >}}). If there are no directory and file structure examples provided, please make use of snake_case to name your files and directories.

### Why snake case ?

Students are expected to be on the same page when it comes to naming their files and directories - utilizing the same convention makes reviewing files easier for everyone involved. Snake case also makes it easier to separate long file names. 

#### Example of what is expected

```
├── spec
|   ├── support
|   |   └── jasmine.json
|   └── simple_calculator_spec.js
├── src
|   └── simple_calculator.js
└── package.json
```
