---
_db_id: 532
available_flavours:
- javascript
- typescript
content_type: project
prerequisites:
  hard:
  - projects/redux-intro/part-1
  - projects/tilde-mockups
  - topics/web-frontend/react/redux-architecture
  soft: []
ready: true
submission_type: repo
tags:
- React
- Redux
title: 'React and Redux recipe search: Part 1. Presenting the form'
---

This is part 1 of a project where we will be using Redux in order to build a recipe search user interface based on the (RecipePuppy API)[content/projects/recipe-search/part-1].

In this part of the excercise we wont be making any queries to the api, we'll just be using React and Redux to build a kick-ass search form.

## Instructions

Create a search page that has the following functionality:

- It needs a search box where the user can enter keywords, for example "omlette" or "mexican" or whatever else they are keen on.
- It also needs a mechanism for adding ingredients to the search. And removing ingredients if they made a mistake.

Here is a valid user journey:

- Tshepo is wondering what to make for dinner
- He looks around the kitchen to see what he has available
- He has some bacon, leeks, onions and tomatoes and he feels like something Italian. So he selects the ingredients and fills "Italian" into the search box
- he then realises that the leeks are mouldy so he removes "leeks" from the search.

## Success criteria

In this project you are expected to use redux for all your state managment. Don't use useState or any other hooks.

In real life applictions it usually makes sense to use a combination of redux and react hook based state, but the purpose of this project is for you to practice getting redux and react to play nice.

## Hints

Take a look at the api. Be sure that you understand that the ingredients and the search query are two different things. The user should be made aware of this through an intuitive looking form.