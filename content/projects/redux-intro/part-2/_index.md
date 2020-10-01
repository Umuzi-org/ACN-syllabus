---
_db_id: 552
available_flavours:
- javascript
- typescript
content_type: project
from_repo: projects/redux-intro/part-1
prerequisites:
  hard:
  - projects/redux-intro/part-1
ready: true
submission_type: continue_repo
tags:
- redux
- combineReducers
title: 'Intro to Redux for home automation: combine reducers'
---

## Instructions

Often Redux is tied to pretty complicated applications. There are often many pages, widgets and whatnots that need to be controlled. As things get complicated your reducer can get really really big.

That's why redux has a thing called CombineReducers, it lets you split things up a bit.

Create a few seperate reducers to control different things. You could have a sperate reducer per room, or you could have a sperate reducer for each major function (eg: you could have a "lighting" reducer that controls the lights for the whole house).

Demonstrate your understanding of combineReducers.

This would be a good time to make another PR.