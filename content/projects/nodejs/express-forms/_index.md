---
_db_id: 279
content_type: project
flavours:
- javascript
from_repo: projects/nodejs/file-io
learning_outcomes:
- web_dev_server_setup
- web_dev_form_creation
- web_dev_using_templating_engines
- wed_dev_client_side_testing
- web_dev_data_rendering
- web_dev_dbms_set_up
- web_dev_host_static_files
- web_dev_routes_and_controllers
- web_dev_crud_operations
pre: '<b>3: </b>'
prerequisites:
  hard:
  - projects/nodejs/sql
  - projects/nodejs/file-io
  - topics/js-and-node-specific/expressjs
  soft: []
ready: true
story_points: 3
submission_type: continue_repo
tags:
- node
- express
title: Express, forms and templates
weight: 3
---

## Create a basic HTML form

Create an HTML form. This form will (eventually) be used to create Visitor fields in your database. Your form should have the following fields:

- visitor name
- your name (name of the person who assisted the visitor)
- visitor's age
- date of visit
- time of visit
- comments

## use express to host the form as a static resource

Create a basic express.js application and serve your form as a static file

The URL should be `http://localhost:[YOUR_PORT]/new_visit`

## submit the form

There should be a submit button on the form. When the user submits the form then the following should happen:

1. The form data will be collected and your `addNewVisitor` function will be called to save the visitor details into your database
2. The user should then be redirected to a page that says: "Thanks for the info! The following was saved to the database:". This page should display the information that was saved, as well as the id of the new Visitor instance.

Make use of the pug template engine to render the "Thank you" page

### Resources

- {{% contentlink path="topics/js-and-node-specific/expressjs/" %}}
- {{% contentlink path="topics/js-and-node-specific/template-engines" %}}
- {{% contentlink path="topics/js-and-node-specific/fetch" %}}