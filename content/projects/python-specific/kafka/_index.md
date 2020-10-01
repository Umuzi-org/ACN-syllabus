---
_db_id: 258
available_flavours:
- python
content_type: project
prerequisites:
  hard:
  - topics/python-specific/kafka
  soft: []
ready: true
submission_type: repo
tags:
- python
- kafka
title: Python and Kafka
---

The first step is to create an "app" on twitter. https://developer.twitter.com/en/apps

And then in your virtualenv, install these dependencies:

```
pip install kafka-python
pip install python-twitter
pip install tweepy
```

Create a topic. Pick something you are interested in. For example you might want to collect tweets about data-engineering, covid-19, or space travel. Whatever you want :)

Write a script that will print tweets to standard out, and also publish them to kafka.

Make sure that you follow good practices - don't hard-code any secret information (like your passwords) and don't hard-code configuration either (it should come from your environmental variables)