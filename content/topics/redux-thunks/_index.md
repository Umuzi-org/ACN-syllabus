---
_db_id: 524
content_type: topic
prerequisites:
  hard:
  - topics/redux-intro
  soft: []
title: Redux Thunks
ready: True
---

As we know, redux changes application state upon instructions or events like a mouse or button click that the user initiates. Redux-thunk is a tool that puts those instructions into a queue and makes sure each instruction is performed one at a time.

### Why are Redux-Thunks useful?

The most common reason for using redux-thunk is to allow different kinds of asynchronous logic to interact with the store. This allows you to write code that can dispatch actions and check the store state while keeping that logic separate from the UI.

Suppose you build an application that stores information about students and you want to extract the data as part of your applications logic. Imagine you want to make two requests: In the first request, you fetch student's profile information from the back-end API, and then in the second request, using the student's id that came in the from the first request, You want to fetch details about the student's projects. 

Since both requests are asynchronous, the second request can start and end before the first request is completed, or vice versa. Put simply, we have a few concurrent requests, and so our code is prone to "race condition bugs" (because it's like the two requests are racing each other). That's where redux-thunks come in, they help us explicitly control the order of each action’s execution, avoid data race conditions and they also allow you to:

- Execute extra logic when any action is dispatched.
- Pause, modify, delay, or replace dispatched actions.
- Write extra code that has access to dispatch and getState.
- Teach dispatch how to accept other values besides plain action objects, such as functions and promises, by intercepting them and dispatching real action objects instead.

The official Redux tutorial explains thunks really well. Please read the following and make sure you understand it

- https://redux.js.org/advanced/async-actions
- https://github.com/reduxjs/redux-thunk