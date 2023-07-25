---
_db_id: 552
content_type: project
flavours:
- javascript
- typescript
- react
from_repo: projects/redux-intro/part-1
prerequisites:
  hard:
  - projects/redux-intro/part-1
  - topics/web-frontend/react/redux-architecture
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

Create a few separate reducers to control different things. You could have a separate reducer per room, or you could have a separate reducer for each major function (eg: you could have a "lighting" reducer that controls the lights for the whole house).

Demonstrate your understanding of `combineReducers`.

Make sure that you organise your code according to the architectural guidelines already covered here:

{{< contentlink path="topics/web-frontend/react/redux-architecture" flavour="react,redux" >}}

It's likely that you will need to refactor a lot of your work.