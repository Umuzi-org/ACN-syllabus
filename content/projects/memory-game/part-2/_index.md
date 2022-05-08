---
_db_id: 550
content_type: project
flavours:
- javascript
- typescript
- any_frontend_framework
- redux
from_repo: projects/memory-game/part-1
learning_outcomes:
- web_dev_state_management
- web_dev_code_modification
- web_dev_testing_dom_elements_with_jsdom
prerequisites:
  hard:
  - projects/tdd/password-checker/part1
  - projects/memory-game/part-1
  - topics/git-feature-branching
  soft: []
ready: true
submission_type: continue_repo
tags:
- web-frontend
- html
- css
- git-feature-branching
- tdd
title: extra features for your memory game
---

Please make sure you are following Git Feature Branching at this point. It's really important and really useful.

- One branch per feature, please!
- Every branch should come off master.

For example:

```
git checkout master
git pull
git checkout -b feat/configurable-grid-size
```

## Feature 1: Configurable grid size

As a user, I want to be able to choose the dimensions of the grid each time I play the game. For example, I might want to play on a 2x2 grid or a 3x2 grid.

## Feature 2: Timer

As a user, I want to see how long it takes for me to finish the game. When the game is done I want to see a message that tells me how long it took me to finish the game

## Feature 3: Count card flips

As a user, I want to be able to see how many turns I've had. The game needs to keep track of this count. When the game is done I want to see a message that tells me how many moves I took to finish the game.

## Instructions for the reviewer

- Check that once cards are matched, they cannot be flipped over again.
- Make sure the specs actually test the functionality of the code. Changes in the source files should affect the tests.
- Make sure that cards can not be clicked once the timer stops.
- Check that card clicks are registered correctly; no multiple clicks and already flipped or matched cards don't register additional clicks.
