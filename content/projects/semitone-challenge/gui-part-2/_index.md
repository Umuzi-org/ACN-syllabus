---
_db_id: 194
content_type: project
flavours:
- javascript
- typescript
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
- wed_dev_advanced_gui_design
pre: <b>4. </b>
prerequisites:
  hard:
  - projects/semitone-challenge/basic-algorithm
  - projects/semitone-challenge/gui-part-1
  - projects/semitone-challenge/advanced-algorithm
  soft: []
ready: true
submission_type: continue_repo
tags:
- html
- css
title: semitone difference - A gui that is more...awesome
weight: 4
---

Extend your simple gui with the following behavior:

1. Add a button that lets the user give up. If the user clicks on this button then ALL the notes (A, A#, B,...) should be displayed. The currently selected notes should be highlighted and the final answer should be displayed on the screen. The user should clearly see how the answer was calculated.
2. The user should be able to restart the game and generate new notes. If the game restarts then of course the explanation from (1) should disappear.
3. If the user submits the correct answer then the "explanation" should be populated with the currently selected notes highlighted. The user should be congratulated.
4. Keep track of how many correct answers the user gets in a row and display this answer on the screen. This is referred to as a streak. Have some pseudocode:

```
user accesses gui for first time
gui displays: "Streak: 0"
user gets correct answer
gui displays: "Streak: 1"
user gets correct answer
gui displays: "Streak: 2"
user gets correct answer
gui displays: "Streak: 3"
user gets wrong answer
gui displays: "Streak: 0"   <<< the streak is reset to zero because the user got the answer wrong
```
