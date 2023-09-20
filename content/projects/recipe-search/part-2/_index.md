---
_db_id: 533
content_type: project
flavours:
- javascript
- typescript
- react
from_repo: projects/recipe-search/part-1
prerequisites:
  hard:
  - projects/recipe-search/part-1
  - topics/redux-thunks
  soft: []
ready: true
submission_type: continue_repo
tags:
- React
- Redux
- Thunks
title: 'React and Redux recipe search: Part 2. API Access with thunks'
---

Now that your frontend is awesome, let's get the "Search" button to work.

Take a look at [this neat little API](https://developer.edamam.com/edamam-recipe-api)

As far as APIs go it's fairly straight-forward. All you need to do is create an account and use the free developer plan.

## Instructions

Add a Button labelled "Search" to your web application. When the user clicks on this button do the following:

1. Access the api using a thunk.
2. Once the results arrive, display each recipe's name, ingredients and picture in a nice and neat way.
3. Make sure that the user can easily do another search without having to refresh the page or anything weird like that.
4. Please test your code, you will be expected to use a react testing library to test your components, here is the documentation {{< contentlink path="topics/web-frontend/react/unit-testing" >}}.

## Getting to Excellent

If you want to be marked as excellent then there are a few things you can do:

- Add a "next" and "previous" button to add paging to your application. Or, better yet, automatically fetch the next page of results as the user scrolls to the end of the returned recipes list.
- Make use of a [spinner widget](https://material-ui.com/components/progress/) to show that the search results are still loading.