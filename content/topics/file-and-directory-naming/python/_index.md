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

When naming files and directories you should use small letters, and yours words should be separated by underscores.
This type of naming convention is called snake_case. As you would recall from the `clean code` content, this type of
naming convention is also used for naming python variable and function names. Read that again :).


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

password_checker
    add_logger.py

snake_case
    production_notes.py
    keep_it_short_and_meaningful.py
    
```
