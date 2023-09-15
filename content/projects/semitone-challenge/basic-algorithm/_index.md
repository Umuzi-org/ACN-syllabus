---
_db_id: 199
content_type: project
flavours:
  - any_language
learning_outcomes:
  - web_dev_shuffling_elements
  - web_dev_indexing
pre: <b>1. </b>
prerequisites:
  hard:
    - projects/tdd/simple-calculator-part1
  soft: []
ready: true
submission_type: repo
tags:
  - problem solving
title: semitone difference - basic algorithm
weight: 1
---

## Set up your environment

### Javascript

Your directory structure should look like this.

```
├── spec
|   ├── support
|   |   └── jasmine.json
|   └── ???
├── src
|   └── jam_buddy.js
└── package.json
```

**Note**: Please export your class using the following syntax at the end of the code:

```
module.exports = { className }
```

### Java

When you use gradle to create your project, give your project the following name: `jam_buddy`

Make sure that all of the classes you define are within the `jam_buddy` package. Do this by including a package declaration at the top of each of your java files.

```
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    ├── main
    |   └── java
    |       └── jam_buddy
    |            └──  JamBuddy.java <-------- names are important
    └── test
        └── java
            └── ???.java             <-------- names are important
```

### Python

```
├── jam_buddy   the package under test
│   └── jam_buddy.py
├── requirements.txt    installation requirements
├── setup.py            installation script for the package under test
└── tests               all package tests go in this directory
    ├── ???

```

## Introduction

This is the first step in a multi-step project designed to level up many different skills.

We want to see the following skills demonstrated in different parts of this project:

- Code structure
- Functions
- Loops
- Conditions
- Datatypes
- Operators
- DOM manipulation

Make sure you test your work!

## Ok... so what is a semitone?

I'm glad you asked. Take a look at these links:

- https://www.justinguitar.com/guitar-lessons/the-note-circle-bc-152
- https://www.justinguitar.com/guitar-lessons/note-circle-with-a-jam-buddy-mt-106

What we want to do, is build a simple application that a musician can use to test their music theory skills.

In the second video, Justin talks about a game that you can play with a jam buddy. Your buddy picks two notes from the note circle and tells them to you, then you tell your buddy how many semi-tones separates those notes. That is basically what we are building here.

The final goal is to have a program that outputs two notes from the note circle and then allows the user to enter a number. The program needs to be able to tell the user if they chose the correct number or not.

## Instructions

Make a class called `JamBuddy`. A JamBuddy instance should be able to keep track of the currently selected notes.

It should have the following functions:

### JavaScript and Python

- `set current notes`: This should take an array/list of 2 notes as an argument. Each note is a string. If an incorrect note is passed in, for example `B#`, then raise/throw an Error/Exception with an appropriate error message.
- `get current notes`: This should return an array/list of the currently selected notes
- `randomize current notes`: This will pick 2 notes at random and then store them in the JamBuddy instance. It should never select 2 of the same note
- `check answer`: This should take in an integer and return a boolean true if the answer is correct and false if the answer is incorrect. Note that since the note circle is a circle, there will always be 2 correct answers. For example, the distance between A and A# is 1 if you go clockwise, and 11 if you go anti-clockwise. Both answers are correct.

### Java
- `set current notes`: This should take an array of 2 notes as an argument. Each note is a string. If an incorrect note is passed in, for example `B#`, then raise/throw an Error/Exception with an appropriate error message.
- `get current notes`: This should return a String array of the currently selected notes
- `randomize current notes`: This will pick 2 notes at random and then store them in the JamBuddy instance. It should never select 2 of the same note
- `check answer`: This should take in an integer and return a boolean true if the answer is correct and false if the answer is incorrect. Note that since the note circle is a circle, there will always be 2 correct answers. For example, the distance between A and A# is 1 if you go clockwise, and 11 if you go anti-clockwise. Both answers are correct.


For now don't worry about "flat" notes. The game will only be played with the following notes:

```
A A# B C C# D D# E F F# G G#
```

## Example usage

Here is some pseudo code

```
buddy = new JamBuddy()
buddy.randomizeCurrentNotes()
buddy.getCurrentNotes() # let's say this returns ['C','D#']
buddy.checkAnswer(1) # This will return a boolean False
buddy.checkAnswer(2) # False again
buddy.checkAnswer(3) # This is correct, so it returns True
buddy.checkAnswer(9) # This is also correct => True

buddy.setCurrentNotes(['A','A#'])
buddy.getCurrentNotes() # this will return ['A','A#']
buddy.checkAnswer(1) # returns a boolean True
```
