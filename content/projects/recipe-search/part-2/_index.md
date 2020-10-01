---
_db_id: 533
available_flavours:
- javascript
- typescript
content_type: project
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

Now that your frontend is awesome, let's get the "search" button to work.

Take a look at this neat little API:

http://www.recipepuppy.com/about/api/

As APIs go it's pairly straight-forward. It's also free and requires no authentication.

## Instructions

Add a Button labelled "Search" to your web application. When the user clicks on this button do the following:

1. Access the api using a thunk
2. once the results arrive, display them in a nice table. Make sure you display all the info and that it is nice and neat.
3. Make sure that the user can easily do another search without having to refresh the page or anything weird like that

## Getting to Excellent

If you want to be marked as excellent then there are a few things you can do:

- Add a "next" and "previous" button to add paging to your application. Or, better yet, automatically fetch the next page of results as the user scrolls to the end of the returned recipes list.
- Make use of a spinner widget to show that the search results are still loading: https://material-ui.com/components/progress/