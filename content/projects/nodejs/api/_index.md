---
_db_id: 278
content_type: project
flavours:
  - javascript
from_repo: projects/nodejs/file-io
learning_outcomes:
  - web_dev_expose_business_logic
pre: "<b>4: </b>"
prerequisites:
  hard:
    - projects/nodejs/sql
    - topics/js-and-node-specific/apis-with-node
    - projects/nodejs/file-io
  soft: []
ready: true
story_points: 5
submission_type: continue_repo
tags:
  - node
  - api
  - express
title: Expose a JSON API
weight: 4
---

There is no need to create a new git repo for this code submission. This is a continuation of your previous work.

## Instructions

Use Express to expose the following JSON endpoints.

- GET `/visitors` : lists all the visitors
- POST `/visitors` : creates a new visitors
- GET `/visitors/{id}` gets the details of a specific visitor
- DELETE `/visitors/{id}` deletes a specific visitor
- PUT `/visitors/{id}` updates a specific visitor

### Resources

- {{% contentlink path="topics/apis/basics" %}}
- {{% contentlink path="topics/js-and-node-specific/apis-with-node" %}}
