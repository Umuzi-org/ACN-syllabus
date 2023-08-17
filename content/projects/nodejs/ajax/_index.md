---
_db_id: 283
content_type: project
flavours:
  - javascript
from_repo: projects/nodejs/sql
learning_outcomes:
  - wed_dev_client_side_testing
  - web_dev_crud_operations_and_data_presentation
  - web_dev_routes
prerequisites:
  hard:
    - topics/intro-to-ajax
    - projects/nodejs/sql
    - projects/nodejs/api
  soft: []
ready: true
story_points: 8
submission_type: continue_repo
tags:
  - node
  - ajax
title: Add a little Ajax
---

In this project you'll be creating a more modern frontend for your application. You'll need to create a whole new page that allows a user to see a list of visitors and to delete visitors.

## The technology to use for sending AJAX requests

As a developer, it's important that you can think for yourself and read up on things. Tech changes all the time.
Do some googling - read up on the current best practices. Find out the pros and cons for using a certain technology to make requests from the client-side applications. Then make a choice.

## A new page

Create a new static web page. Serve your new page from the following URL: `http://localhost:[YOUR_PORT]/app`

## List existing visitors

Create an HTML table on the same page (on your single-page app). Use an ajax call to populate the table. Your frontend should be retrieving data from an api endpoint you already created.

## Delete visitors

Add a "delete" button to each line of the table. When the user clicks "delete" then

- ask the user if they are sure that they want to delete the visitor. Use some kind of modal or pop up.
- make an api call to delete the visitor from the database
- update the information displayed in the table

Also, make sure that if you create any new visitors then they are visible on the table

## Add a visitor

Add a button labelled "New Visitor". This button should redirect the user to the new visitor form that was created in an earlier step in this project.

Update the "thank you page" so that it only displays for 3 seconds and then redirects the user back to the visitors table. Of course the new visiter should be visible in the table.

## Up for a challenge?

So far, you've made use of only 3 API end points(`POST`, `GET` and `DELETE`). Can you figure out how to make use the `PUT` endpoint? The implementation here is completely up to you.

## Resources

- {{< contentlink path="topics/intro-to-ajax" >}}
