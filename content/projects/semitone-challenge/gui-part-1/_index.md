---
_db_id: 196
content_type: project
flavours:
- javascript
- any_frontend_framework
from_repo: projects/semitone-challenge/basic-algorithm
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
learning_outcomes:
  web_dev_shuffling_elements
  web_dev_indexing
  web_dev_two_dimensional_arrays
  web_dev_testing_dom_events_with_spies
  web_dev_testing_dom_elements_with_jsdom
  web_dev_event_handling
  web_dev_simple_gui_design
---

Create a basic web site that a user can use to interact with the JamBuddy class.

If you are required to do this in a web framework then do so, otherwise create a simple `index.html` page that a user can just open in their browser.

- Make a button with the text "Get random notes". If the user clicks on this button then the `selectNotes` function should be called and the notes should be displayed on the screen.
- make an input box where the user can enter their answer.
- create a button with the text "Submit answer". If the user clicks this button then the `checkAnswer` function should be called.
  - if the answer is correct then display the message "You got it right .Well Done!"
  - if the answer is incorrect then display the message "Wrong answer! Try again"

## Acceptance criteria

### Directory structure

Please put your html in a file called index.html in your root directory.

### Unit tests

TDD is a must. Yes, you need to even unit test your DOM manipulations.

This is useful: https://github.com/jsdom/jsdom 

When testing your dom, don't just check that your boring html exists. Make sure that when the "Get random notes" button is clicked then the right dom elements get updated. Tests do not exist to take up space, they exist to make sure your code actually works.

### Make it look reasonably good

We don't need you to win any design awards here, but put some effort into the looks. If you make anyone's eyes bleed that would be a problem.

Here are a few tools you might want to explore:

- [Tailwind](https://tailwindcss.com/docs/installation#using-tailwind-via-cdn) Just use the CDN to keep it simple for now
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

You can also do your own styling from scratch.

Also, think about the user! Imagine a musician using this thing in order to learn music. If your site is confusing then people wouldn't use it. They'd just get annoyed and leave. 

**Bad UX is a bug!** Make sure your user knows how to use your application. Make it dead obvious.