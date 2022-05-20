---
_db_id: 553
content_type: topic
flavours:
- javascript
- typescript
prerequisites:
  hard:
  - topics/redux-thunks
  soft: []
ready: true
title: Redux Saga
---

So thunks are cool and all, but as soon as you try to do anything actually complicated with them then you end up with some highly indented very messy scrambley code. It gets pretty hard to understand, it's so bad that a lot of people refer to it as callback-hell.

Saga allows you to write simple code in order to manage very complicated side effects.

As usual, the official docs are highly recommended:

https://redux-saga.js.org/docs/introduction/BeginnerTutorial.html