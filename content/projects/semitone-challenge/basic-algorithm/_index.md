---
_db_id: 199
available_flavours:
- typescript
- javascript
content_type: project
pre: <b>1. </b>
prerequisites:
  hard:
  - projects/tdd/simple-calculator-part1
  soft: []
ready: true
submission_type: repo
title: semitone difference - basic algorithm
weight: 1
---

This is a multi-step project designed to level up many different skills.

We want to see the following skills demonstrated in different parts of this project:

- code structure
- functions
- loops
- conditions
- datatypes
- operators
- DOM maipulation

This project should be completed in a TDD way.

Ok...so WTF is a semitone? I'm glad you asked. Take a look at these links:

- https://www.justinguitar.com/guitar-lessons/the-note-circle-bc-152
- https://www.justinguitar.com/guitar-lessons/note-circle-with-a-jam-buddy-mt-106

What we want to do is build a simple application that a musician can use to test their music theory skillz.

In the second video, Justin talks about a game that you can play with a jam buddy. Your buddy picks two notes from the note circle and tells them to you, then you tell your buddy how many semi-tones seperate those notes. That is basically what we are building here.

The final goal is to have a program that outputs two notes from the note circle and then allows the user to enter a number. The program needs to be ablt to tell the user if they chose the correct number or not.

For those of you studying web dev, you will be expected to build a simple user interface for this thing using vanilla js. For those of you studying Python you can make a command-line utility that does this.

1. {{% contentlink path="projects/semitone-challenge/basic-algorithm" %}}
2. {{% contentlink path="projects/semitone-challenge/gui-part-1" %}}
3. {{% contentlink path="projects/semitone-challenge/advanced-algorithm" %}}
4. {{% contentlink path="projects/semitone-challenge/gui-part-2" %}}

## Instructions

Make a class called JamBuddy. JamBuddy should work like this:

JS:

```
let buddy = new JamBuddy()
let notes = buddy.selectNotes()
console.log(notes) # this will print an array of two notes
correct = buddy.checkAnswer(1)
console.log(correct) # this will print True if the `1` was the correct answer
```

## Some finer points

For now don't worry about "flat" notes. The notes we care about are:

```
A A# B C C# D D# E F F# G G#
```

Here is an example usage:

JS:

```
let buddy = new JamBuddy()
let notes = buddy.selectNotes()
console.log(notes) # let's pretend that this outputs ['A', 'B']

let correct = buddy.checkAnswer(1)
console.log(correct) # false

correct = buddy.checkAnswer(2)
console.log(correct) # true
```

## Acceptance criteria

Make sure you do this in a TDD way. And that code sample from the top needs to run as is.

Please just supply a working class. The only place you should instantiate your class is inside your unit tests