---
_db_id: 222
content_type: project
flavours:
- javascript
- typescript
- any_frontend_framework
- redux
learning_outcomes:
- web_dev_dom_manipulation
- web_dev_event_handling
- web_dev_virtual_dom
- wed_dev_client_side_testing
- web_dev_testing_dom_elements_with_jsdom
prerequisites:
  hard:
  - topics/basic-architecture-concepts
ready: true
story_points: 5
submission_type: repo
tags:
- TDD
- Dom Manipulation
- Mocks and spies
title: Memory game web app
---

Here is an example of a memory game: http://dkmgames.com/memory/pairsrun.php

## Instructions

Create a Memory game MVP with the following requirements:

- Take a moment to google MVP. If you add unnecessary features we'll ask you to remove them.
- Make use of simple dom elements, no fancy graphics needed or canvas stuff.
- Only a single player can play the game.
- Board is a pre-defined size.
- Board allows one set of symbols or images to be randomly hidden.

Build your game in a TDD manner. If you don't include tests in your final submission, you will be held back and you will be expected to start over.

## Unit testing

Tests are very important. Please follow the following best practices:

- Tdd!!!
- If you are using plain ol js, then your tests need to make use of mocks and spies to check that the frontend is being updated as it should be.

## Instructions for the reviewer

- Check that once cards are matched, they cannot be flipped over again.
- Make sure the specs actually test the functionality of the code. Changes in the source files should affect the tests.