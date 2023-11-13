---
_db_id: 945
content_type: topic
ready: true
title: Introduction to Gradle
---

If you work on simple projects then organising your code is pretty easy. But most projects aren't simple. Life gets tricky when you need to wrangle multiple files and external dependencies.

Gradle aims to solve a lot of the problems that crop up in big Java projects.

Follow the [official quick start guide](https://docs.gradle.org/current/userguide/part1_gradle_init.html) to get yourself set up and familiar.

## To IDE or not to IDE, that is the question

A lot of developers, especially Java developers, use heavy-weight IDEs to write code, for example IntelliJ. It is worth learning IntelliJ at some point, but it is also very useful to know how to do things by hand.

### Why?

If you use a tool that does all your thinking for you then when things break you'll have no idea what is going on. If you want to be a pro it will be worth doing things by hand at least for a little while.

## Gradle by hand

It's not very hard :)

If you wanted to start a new project then you would do the following:

1. Make a directory
2. `cd` into that directory
3. Run `gradle init`

This last command will kick off a process that asks you a bunch of questions. Once you have answered everything then gradle will set up a directory structure for you.

First you'll be asked what type of project you'll want to generate. Generally `application` is a good bet.

You'll be asked a few more questions, you can just use the defaults for most things unless you are doing something unusual.

When it asks you for a "project name" then make sure you enter something sensible. If you have been asked to use Gradle in one of your syllabus projects then please read the project instructions to see what the "project name" should be.
