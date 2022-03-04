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

## How should I name my PYTHON modules and packages?


Modules should have short, all-lowercase names and underscores can be used to improves readability. 

Packages should also have short, all-lowercase names, although the use of underscores is discouraged.


#### NO:

    TASK/
        1task.py
        task 1.py
        task1.1.py
        
    passwordChecker/
        add-logger.py

    snakecase/
        productionnotes.py
        keepItShortAndmeaningfull.py

#### Yes:
    task/
        task_1.py
        task_2.py
        task_1_1.py

    password-checker/
        add_logger.py

    snake_case/
        production_notes.py
        kee_it_short_and_meaningfull.py


