---
_db_id: 270
content_type: project
flavours:
- any_language
from_repo: projects/tdd/password-checker/part1
prerequisites:
  hard:
  - projects/tdd/password-checker/part1
  soft: []
ready: true
story_points: 3
submission_type: continue_repo
tags:
- logging
title: Add logging to password checker
---

In part one of this exercise you created two functions. Now you are going to upgrade that program by adding some logging capabilities.
You are expected to use the recommended logging library(or framework) for your programming language:

- Javascript: Winston
- Java: log4J-2
- Python: logging

1. Whenever `passwordIsValid` returns true, log the following message

```
User password is valid
```

Otherwise:

```
User password is not valid
```

The log level of these messages should be `debug`.
Make sure that your messages get printed to the standard output / terminal / console.

Take note, we aren't actually logging the user's password. In general you want to avoid logging sensitive information.

2. Whenever an exception is raised by `passwordIsValid` then log the exact error message.

- The log level should be `error`
- The log should be printed to the standard output / terminal / console
- Error logs should also be stored in a file called `errors.log`
- Your debug logs SHOULD NOT be inside the `errors.log` file
- Make sure that you update your `.gitignore` so that the `errors.log` file is not in your repo

**Please take note:** All your previous tests should all pass.


## Instructions for reviewer

- Make sure that all the previous tests still pass.
- Different errors should be logged at different levels `debug` vs `error`.
- Are the log messages printed to the standard output / terminal / console?
- Are the correct errors stored in `errors.log`? Only one type should be there.
- User passwords should NEVER be logged.
