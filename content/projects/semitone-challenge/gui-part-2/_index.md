---
_db_id: 194
available_flavours:
- javascript
- typescript
- any_frontend_framework
content_type: project
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
title: semitone difference - A gui that is more...awesome
weight: 4
---

Extend your simple gui with the following behavior:

1. When the user loads the page for the first time then there should be two notes already displayed on the screen.
2. Add a button with the text "Reveal answer". If the user clicks on this button then ALL the notes (A, A#, B,...) should be displayed in a div with the id "explanation". The currently s4elected notes should be highlighted and the final answer should be displayed on the screen.
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