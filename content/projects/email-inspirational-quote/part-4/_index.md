---
content_type: project
flavours:
- any_language
prerequisites:
  hard:
  - topics/unit-testing-mocks-and-spies
  - topics/linux/os-environmental-variables
  - projects/email-inspirational-quote/part-1
  - projects/email-inspirational-quote/part-3
  soft: []
ready: true
submission_type: continue_repo
from_repo: projects/email-inspirational-quote/part-1
tags:
- logging
title: Email random inspirational quote - part 4
---

Now you are going to upgrade your program by adding some logging capabilities.

You are expected to use the recommended logging library(or framework) for your programming language:

- Javascript: Winston
- Java: log4J-2
- Python: logging

## Log errors

Whenever an exception/error is raised or thrown then it should be logged to a file called errors.log.

Note that even network errors should be logged.

## Log every sent email

Whenever an email is sent then it there should be an "info" message printed to the terminal. Just log who the email was sent to, don't log the entire emailed message.

## Gitignore

Make sure your log files are gitignored.