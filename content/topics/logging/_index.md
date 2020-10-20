---
_db_id: 48
content_type: topic
ready: true
title: Logging
---

Through the development process logging helps us evaluate computation which we might be uncertain about, or show us what is happening during runtime where we have little control. Its like a third eye helping us see things that we might otherwise finding very difficult to see.

## What?

Logging is basically getting your program to write stuff down. You are already familiar with printing things out to the console or screen, logging is like that but on steroids.

Basically when a program runs in a production environment, logs let us keep track of what it is doing over time. A log is a series of messages that get printed or sent somewhere. They might be stored in a file, or sent over a network to a special logging service, or (during development) you might want to just see log messages on your screen.

## Why?

Because a running program can be super opaque. Sometimes thing break in really interesting ways and logs can be used to understand what actually happened that led up to this breakage. Sometimes logs need to be in place for generating metrics about system performance. Sometimes logs are used to understand security breaches.

Sometimes logs are just useful for a developer making some changes to a system. A dev can watch the log messages roll in and get a clear picture of what the code is doing.

## Log levels

Log messages come in a few different flavours called levels. Basically each log message is given a level (either implicitly or explicitly) and those levels mean different things. The different log levels tend to be pretty consistent between languages.

There are the main levels:

- `debug`: info for devs, these shouldn't be logged on a production environment
- `info`: this veries. Basically there are usually a few different stakeholders involved in a project. These logs should add clarity without being overwhelmingly noisy
- `warn`: something is looking kinda weird
- `error`: oh crap. Some error or exception has happened
- `critical` or `fatal`: This is serious, immediate action required

As an analogy, if you shout "DONT TOUCH THAT!" to a three year old about to put their hand on a stove then that might be a `critical` message. And if you say "I'm going to the shop" then that might be an `info` message. And if you say "I'm going to the shop to buy cigaretts" then that might be an `error` message.

Two major use cases for log levels are:

- deciding which logs should be generated. Eg: In your production environment you wont want to see any `debug` logs. But when you are developing then you do want to see them
- taking different actions on messages of different levels: eg: if there is an `warn` log message then create a ticket on the bugtracker, and if there is a `critical` log message then sound the alarms.

## In your language

Different languages have different tooling that you can use to manage logs. To continue learning about logs, please follow the appropriate link below:

- {{% contentlink path="topics/js-and-node-specific/logging" %}}
- {{% contentlink path="topics/java-specific/logging" %}}
- {{% contentlink path="topics/python-specific/logging" %}}