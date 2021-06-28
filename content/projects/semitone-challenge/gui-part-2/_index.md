---
_db_id: 194
content_type: project
flavours:
- javascript
- typescript
- any_frontend_framework
from_repo: projects/semitone-challenge/basic-algorithm
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

1. When the user loads the page for the first time then there should be two notes already displayed on the screen.
2. Add a button with the text "Reveal answer". If the user clicks on this button then ALL the notes (A, A#, B,...) should be displayed in a div with the id "explanation". The currently selected notes should be highlighted and the final answer should be displayed on the screen.
3. If the user clicks on the "Get random notes" button then the "explanation" div should be emptied.
4. If the user submits the correct answer then the "explanation" div should be populated as above. The user should be congratulated just like before
5. Keep track of how many correct answers the user gets in a row and display this answer on the screen. This is referred to as a streak. Have some pseudocode:

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

## Instructions for Reviewer
- Ensure that when multiple calls have been made to the selectNotes function only two notes are returned. 
- To check if the code contains a bug call the function twice, have a print statement under it, and check if two notes are returned.
- Make sure the notes always get updated when the select notes button is clicked.
- The JamBuddy class should still work correctly in the terminal and should not be mixed up with frontend DOM manipulation.
- Ensure that the spec file contains tests that check the correct distance between the two notes.
- Ensure that there are no unnecessary copying and pasting of variables, all variables used in different files should be exported and imported correctly.
- Ensure that the specs also contain DOM manipulation test cases.
- Ensure that the scorestreak gets incremented by 1 each time when a user gets the correct answer and when the answer is not correct the scorestreak gets reset to 0.