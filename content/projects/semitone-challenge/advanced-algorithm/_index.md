---
_db_id: 197
content_type: project
flavours:
- javascript
- typescript
from_repo: projects/semitone-challenge/basic-algorithm
learning_outcomes:
- web_dev_shuffling_elements
- web_dev_indexing
- web_dev_two_dimensional_arrays
pre: <b>3. </b>
prerequisites:
  hard:
  - projects/semitone-challenge/basic-algorithm
  soft: []
ready: true
submission_type: continue_repo
tags:
- problem solving
title: semitone difference - Advanced algorithm
weight: 3
---

Adjust your `JamBuddy` class so that it can handle flats and sharps.

Here is an example usage:

JS:

```
let buddy = new JamBuddy()
let notes = buddy.selectNotes()
console.log(notes) # let's pretend that this outputs ['A#', 'Db']

let correct = buddy.checkAnswer(1)
console.log(correct) # false

correct = buddy.checkAnswer(3)
console.log(correct) # true
```

Have fun :)

## Acceptance criteria

The usual. TDD is a must