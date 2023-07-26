---
_db_id: 196
content_type: project
flavours:
- javascript
- any_frontend_framework
from_repo: projects/semitone-challenge/basic-algorithm
learning_outcomes:
- web_dev_shuffling_elements
- web_dev_indexing
- web_dev_two_dimensional_arrays
- web_dev_testing_dom_events_with_spies
- web_dev_testing_dom_elements_with_jsdom
- web_dev_event_handling
- web_dev_simple_gui_design
pre: <b>1. </b>
prerequisites:
  hard:
  - projects/semitone-challenge/basic-algorithm
  - topics/js-and-node-specific/dom-manipulation-with-vanilla-js
  soft: []
ready: true
submission_type: continue_repo
tags:
- html
- css
title: semitone difference - Make a simple GUI
weight: 2
---

Create a basic web site that a user can use to interact with the JamBuddy class. 

If you are required to do this in a web framework then do so, otherwise create a simple `index.html` page that a user can just open in their browser. This file should be in the root directory of your repo.

## User experience 

- When the user opens the web page they should immediately see 2 random notes, they should be able to immediately start playing the game
- There should be a button that lets the user randomize the notes. Clicking on this button will choose another 2 random notes and display them to the user
- the user should be able to enter their answer. Make use of a form input and a button
- if the user enters the correct answer then display a success message
- if the user enters an incorrect answer then display a message. Let the user keep trying if they get the answer wrong, do not automatically randomize the notes

## UI

We don't need you to win any design awards here, but put some effort into the looks. If you make anyone's eyes bleed that will be a problem.

Here are a few tools you might want to explore:

- [Tailwind](https://tailwindcss.com/docs/installation#using-tailwind-via-cdn) Just use the CDN to keep it simple for now
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

You can also do your own styling from scratch.

Also, think about the user! Imagine a musician using this thing in order to learn music. If your site is confusing then people won't use it, they'd just get annoyed and leave.

**Bad UX is a bug!** Make sure your user knows how to use your application and make it really obvious.

## Unit tests

Make sure you unit test your website, even your DOM manipulations.

This is useful: https://github.com/jsdom/jsdom

When testing your DOM, don't just check that your boring html exists. Make sure that when the "Get random notes" button is clicked then the right DOM elements get updated. Tests do not exist to take up space, they exist to make sure your code actually works.

## Take note

- The JamBuddy class should still work correctly in the terminal and should not be mixed up with frontend DOM manipulation.
