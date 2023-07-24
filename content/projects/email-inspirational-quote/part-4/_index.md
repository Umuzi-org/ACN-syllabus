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
story_points: 8
submission_type: continue_repo
from_repo: projects/email-inspirational-quote/part-1
tags:
- mocks
- environmental variables
- smtp
- apis
title: Email random inspirational quote - part 2
---

Upgrade your project so that it can accept either an email address or a file path as a command line argument.

For example:

```
# if you are writing python:
python send_inspiration.py ~/email_recipients.json

# if you are writing javascript:
npm run send_inspiration ~/email_recipients.json

# if you are writing Java 
java SendInspiration ~/email_recipients.json
```

The file path should point to a json file with the following format:

```
[
    {
        "email": "someone@email.com",
        "name": "Tshepo"
    },
    {
      "email": ...
      "name": ...
    },
    {...},
    ...
]
```

The script should send an email to each of the email addresses above. 

The email should include the name of the person who is receiving the email. For example:

```
Dear Tshepo,

"It is good even for old men to learn wisdom." - Aeschylus
```

## The original functionality should still work

Please make sure that your original functionality does not break. Ideally your unit tests for the original functionality will not need to change.

## Tests

As usual, test your work well. You will need to make sure that you are using mocks/spies to test this work.

