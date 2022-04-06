---
_db_id: 515
content_type: topic
prerequisites:
  hard:
  - topics/redux-intro/
  soft: []
ready: true
title: React + Redux architectural guidelines
---

Redux is a very powerful state management library used in JavaScript apps to manage the data of your application, and was originally designed for React. Redux helps you write applications that behave consistently by facilitating and sharing data across the components of an application.

## Split components into presentational and container components

Presentation components are components that renders HTML and are all stateless.
Presentational components will not interact with the redux store for state and will receive data via props and render it.

Container components are used to get data from the redux store and allow the data to be used by the presentational components. Container components should be stateful unless you are forced to use React component lifecycle methods.

### Architecture Guidelines
- http://joeellis.la/redux-architecture/
