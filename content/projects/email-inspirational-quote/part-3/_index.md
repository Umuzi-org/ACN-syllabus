---
_db_id: 954
content_type: project
flavours:
  - any_language
from_repo: projects/email-inspirational-quote/part-1
prerequisites:
  hard:
  - projects/email-inspirational-quote/part-1
  - projects/email-inspirational-quote/part-2
  soft: []
ready: true
story_points: 8
submission_type: continue_repo
tags:
  - mocks
  - smtp
  - apis
  - json
  - command-line parameters
  - errors
title: Email random inspirational quote - part 3
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

## The same quote or different quotes

Sometimes you will want to send exactly the same quote to every single person in the mailing list. And sometimes you'll want to send a different quote to each person. We will also make use of a command-line argument to control this.

The default behavior will be that everyone gets a different random quote.

The following will result in each recipient getting the exact same quote:

```
# if you are writing python:
python send_inspiration.py ~/email_recipients.json --same

# if you are writing javascript:
npm run send_inspiration ~/email_recipients.json -- --same

# if you are writing Java
java SendInspiration ~/email_recipients.json --same
```

## Errors

Please raise/throw an appropriate error/exception in these situations:

1. The file doesn't exist
2. The file contains invalid JSON
3. The file's JSON doesn't match the format above
4. The command-line arguments are invalid in any way

## The original functionality should still work

Please make sure that your original functionality does not break. Ideally your unit tests for the original functionality will not need to change.

## Tests

As usual, test your work well. You will need to make sure that you are using mocks/spies to test this work.
