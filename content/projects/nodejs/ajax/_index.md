---
_db_id: 283
available_flavours:
- javascript
content_type: project
from_repo: projects/nodejs/file-io
prerequisites:
  hard:
  - topics/intro-to-ajax
  - projects/nodejs/express-forms
  - projects/nodejs/api
  - projects/nodejs/file-io
  soft: []
ready: true
story_points: 8
submission_type: continue_repo
tags:
- node
- ajax
title: Add a little Ajax
weight: 5
---

There is no need to create a new git repo for this code submission. This is a continuation of your previous work.

## a new static resource

Create a new HTML static web page just like the form page you made before. You can even copy-paste your form's html here. Usually copy-pasting pieces of code is a bad idea, this time it's ok.

Serve your new page from the following url: `http://localhost:[YOUR_PORT]/single-page-app`

## form submissions

The submit button should make an AJAX call to the `addNewVisitor`. It should not redirect the user to any kind of "thank you" page

## list existing visitors

Create an html table on the same page (on your single page app).
Use an ajax call to `/viewVisitors` to populate the table

## delete visitors, and update the table

Add a "delete" button to each line of the table. When the user clicks "delete" then

- make a request to `/deleteVisitor:id` and delete that visitor
- update the information displayed in the table

Also make sure that if you create any new visitors then they are visible in the table

## Resources

- {{% contentlink path="topics/intro-to-ajax" %}}