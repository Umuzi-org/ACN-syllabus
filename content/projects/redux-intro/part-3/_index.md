---
_db_id: 551
available_flavours:
- javascript
- typescript
content_type: project
from_repo: projects/redux-intro/part-1
prerequisites:
  hard:
  - topics/redux-thunks
  - projects/redux-intro/part-1
  - projects/redux-intro/part-2
ready: true
submission_type: continue_repo
tags:
- redux
- redux-thunks
title: 'Intro to Redux for home automation: Party mode with thunks'
---

## Instructions

Now one super cool thing about redux is that you dont really have to dispatch actions one at a time. You can have an action with side effects, and those side effects can dispatch other actions!

There are two main ways to handle side effects in redux. Thunks and Sagas. Thunks are the easy way, and they are worth understanding before movin onto sagas.

Your mission is to create a few more actions that use Thunks to combine a few of your existing actions. For example you might have an action with type `GOOD_MORNING` that starts playing soothing morning tunes and turns the kettle on. You might have another action of type `PARTY_MODE` that dimms the lights, turns on the disco ball, and changes the volume of the door bell.

What combinations of actions would you want to trigger?