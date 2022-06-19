---
_db_id: 199
content_type: project
flavours:
- typescript
- javascript
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
 
Your directory structure should look like this.
 
```
   >node_modules    <---- make sure this is in your .gitignore
   >spec
       > support
           - jasmine.json
       - semitone_spec.js
   >src
       - semitone.js
   - package.json
```

This is a multi-step project designed to level up many different skills.

We want to see the following skills demonstrated in different parts of this project:

- Code structure
- Functions
- Loops
- Conditions
- Datatypes
- Operators
- DOM manipulation

This project should be completed in a TDD way.

Ok...so what is a semitone? I'm glad you asked. Take a look at these links:

- https://www.justinguitar.com/guitar-lessons/the-note-circle-bc-152
- https://www.justinguitar.com/guitar-lessons/note-circle-with-a-jam-buddy-mt-106

What we want to do, is build a simple application that a musician can use to test their music theory skills.

In the second video, Justin talks about a game that you can play with a jam buddy. Your buddy picks two notes from the note circle and tells them to you, then you tell your buddy how many semi-tones seperates those notes. That is basically what we are building here.

The final goal is to have a program that outputs two notes from the note circle and then allows the user to enter a number. The program needs to be able to tell the user if they chose the correct number or not.

For those of you learning web dev, you will be expected to build a simple user interface for this thing using Vanilla js. For those of you learning Python you can make a command-line utility that does this.

1. {{% contentlink path="projects/semitone-challenge/basic-algorithm" %}}
2. {{% contentlink path="projects/semitone-challenge/gui-part-1" %}}
3. {{% contentlink path="projects/semitone-challenge/advanced-algorithm" %}}
4. {{% contentlink path="projects/semitone-challenge/gui-part-2" %}}

## Instructions

Make a class called JamBuddy. JamBuddy should have an attribute that keeps track of the currently selected notes and should be called currentSelectedNotes. JamBuddy class should work like this:

JS:

```
let buddy = new JamBuddy()
let notes = buddy.selectNotes()
console.log(notes) # this will print an array of two notes
console.log(currentSelectedNotes) # this will print the same array of two notes 
console.log(notes === currentSelectedNotes) # should print true notes and currentSelectedNotes should be the same 
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
console.log(correct) # true because: A A# B

# we should be able to play the game again without making another instance

notes = buddy.selectNotes()
console.log(notes) # let's pretend that this outputs ['G', 'B']

correct = buddy.checkAnswer(4)
console.log(correct) # true because: G G# A A# B - the note circle is a CIRCLE, remember that!
```

## Acceptance criteria

Make sure you do this in a TDD way, and that code sample from the top needs to run as is.

Please just supply a working class. The only place you should instantiate your class is inside your unit tests.