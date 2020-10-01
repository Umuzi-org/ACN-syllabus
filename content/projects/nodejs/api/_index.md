---
_db_id: 278
available_flavours:
- javascript
content_type: project
from_repo: projects/nodejs/file-io
pre: '<b>4: </b>'
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

- `/addNewVisitor`: create a new Visitor in the database
- `/deleteVisitor:id`: delete a single Visitor from the database
- `/deleteAllVisitors`: delete all Visitors
- `/viewVisitors`: view all Visitors
- `/viewVisitor:id`: view a single Visitor
- `/updateVisitor:id`: Update a single Visitor

### Resources

- {{% contentlink path="topics/apis/basics" %}}
- {{% contentlink path="topics/js-and-node-specific/apis-with-node" %}}