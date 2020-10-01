---
_db_id: 190
available_flavours:
- python
content_type: project
prerequisites:
  hard:
  - topics/clean-code/python
  - topics/linux/os-environmental-variables
  - topics/how-the-internet-works
  - projects/github-api-consume
  soft: []
ready: true
submission_type: repo
tags:
- rabbit-mq
title: RabbitMQ
---

RabbitMQ, despite its funny name, is a seriously useful piece of software.

On top of this, it's a great introduction to parallel computing.

Take a look at the offical tutorial here: https://www.rabbitmq.com/getstarted.html.

## Instructions

Create one repo. Inside that repo create 6 directories, name them: `one`, `two`, `three`, etc.
Inside directory one, implement tutorial 1 from here: https://www.rabbitmq.com/getstarted.html. Inside directory 2 implement tutorial 2, etc. Go up to number 6.

Now pay close attention: Copy-pasting code is not sufficient.

### Success criteria 1: DRY CODE

Each of your tutorial implementations must be DRY in itself. eg: If you have the string 'hello' pasted all over the place then your code would not be DRY.

Hint: Here's the expected file structure for the first tutorial:

```
one/
    channel.py
    recieve.py
    send.py
```

### Success criteria 2: Environmental variables

Hard-coding the connection string is no good. You want to fetch it from an environmental variable.
On top of that you want to be able to run your code successfully even if the environmental variable is not set.

eg:

```
python send.py  # this should work as per the tutorials

export HOST="35:456:145:235"
python send.py  # this should attempt to connect to a rabbitmq server at the given ip address
```