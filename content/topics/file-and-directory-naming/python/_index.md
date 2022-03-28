---
content_type: topic
prerequisites:
  hard:
  - topics/file-and-directory-naming/general
ready: true
tags:
- File and directory naming
- python
title: File and directory naming in Python
---

## How should I name my Python modules and packages?

You should name your files and directories the same way you name Python variables.They should be small letters, and words should be separated by underscores, as that improves readability.

It is important to note that the use of dashes in directory-naming takes preference as opposed to the use of underscores and be sure to keep in mind that all Python files have a .py extension. See below the recommended Python file and directory naming style. 

### NO:
```
TASK
    1task.py
    task 1.py
    task1.1.py
        
passwordChecker
    add-logger.py

snakecase
    productionnotes.py
    keepItShortAndmeaningful.py
```

### Yes:

```
task
    task_1.py
    task_2.py
    task_1_1.py

password-checker
    add_logger.py

snake_case
    production_notes.py
    keep_it_short_and_meaningful.py
```
