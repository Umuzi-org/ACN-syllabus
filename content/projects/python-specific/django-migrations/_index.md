---
_db_id: 257
available_flavours:
- python
content_type: project
ready: true
submission_type: repo
title: Django - exposing a REST api with a real database
---

Expose a simple TODO list api using Django. Take a look at this first:

- https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/
- https://realpython.com/django-migrations-a-primer/

This is about apis. Please don't make a pretty frontend. Or even an ugly frontend. Just expose an api.

Here is what you need to do:

- create a Django project (in a python3.7 venv)
- create some models and use them to set up a database. Make one model called TodoItem. Is should have a title and a description only
- turn the "admin" interface on and take a look around
- create some REST endpoints that allow a person to:
  - add a TODO item
  - delete a TODO item
  - edit a todo item
  - list all TODO items

Next I want you to be able to update the models and see how that effects your database migrations.

Hint: If you find yourself deleting migration files: You are doing it wrong.

- Add a 'done' boolean column to the TodoItem
- see how that effects your migrations
- update your REST endpoints accordingly