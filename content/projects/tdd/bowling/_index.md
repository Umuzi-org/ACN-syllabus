---
_db_id: 272
available_flavours:
- any_language
content_type: project
pre: '<b>HARD: </b>'
ready: true
submission_type: repo
title: ten-pin bowling scoring system
---

## Take Note

This is a Test Driven Development Project. Please follow a test driven methodologies. That means that you write your test code first!

The basic idea of TDD is to write the test code before you write any actual code. So you write a test (which will fail) then you write the code that will make the test pass.

When you submit your code (on Github people!) then your tests MUST BE included in your code base.

In a professional setting, untested code is incomplete code.

In general: Follow recognized best practices around whatever language and test framework you are using. Eg: consistent naming conventions of functions, test files and literally everything else. Literally.

## Instructions

Write a software system for keeping track of bowling scores. You can read about traditional 10 pin bowling scoring [here](https://en.wikipedia.org/wiki/Ten-pin_bowling#Scoring).

Please put your tests in a directory named "tests" unless the testing framework you are using follows some other convention.

## Project Description

### Gameplay

This project is more about data, tests and algorithms than html. It needs a WORKING frontend but don't spend too much time making it beautiful. Here is how it will work:

1. As the game starts the user will be allowed to enter the names of the players eg "Uncle Bob Martin" and "Ada Lovelace"
2. The user then chooses to start the game
3. The user should be able to see the scores of all the players at all times. This includes scores for individual throws and frames, and their total scores
4. The user should be able to see whose turn it is
5. The user should be able to submit the number of pins hit on each throw. One by one. Eg, it's Uncle Bob's turn, so he throws and misses everything. The user submits a 0. The user interface shows that Bob's score is unchanged and it's still his turn. Bob throws again and hits 2 pins, the user submits a 2 and Bob's score is updated and it's still his turn. He throws again and misses. The user enters a 0. We now see that it is Ada's turn. She throws and hits all the pins because she is awesome. The user enters a 10. Ada's score is updated. Now it's Bob's turn again. Get it?

### Notes about frontends

For those of you doing this in JS: Your user interface will be a web page.

For those of you completing this in Python, don't get too fancy. Python is usually considered to be bad t user interfaces so it's really not worth learning a python frontend framework at this point. Just use the terminal. Take a look [here](http://introtopython.org/terminal_apps.html) for some details.

And everyone: Always remember [KISS](https://en.wikipedia.org/wiki/KISS_principle).

### More Outputs

We should be able to see at any point in time:

- the total score of any player
- the "leaderboard" of the current game (who is in first place, second, third etc)
- the points any person accumulated during a single turn (aka frame)
- how many turns are left
- who's turn is it now?
- whose turn is it next?

### Please don't

PLEASE DO NOT IMPLEMENT A FANCY GUI. We don't care to see the bowling pins or the ball, we don't care about physics.

## Resources and things to know

This is not a simple project. To build something awesome you should be aware of a few architectural concepts.

- {{% contentlink path="topics/basic-architecture-concepts" %}}