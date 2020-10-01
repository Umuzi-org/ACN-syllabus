---
_db_id: 263
available_flavours:
- python
content_type: project
prerequisites:
  hard:
  - topics/python-specific/sqlalchemy
  - topics/apis/basics
  soft: []
ready: true
submission_type: repo
tags: []
title: create a REST api to interact with actual database
---

In this project you'll be taking a lot of your existing knowledge and pulling it together. At this point you know what it means to consume an API. Now you're going to make one :)

The tools to use:

- [Flask](https://palletsprojects.com/p/flask/)
- [Sqlalchemy](https://www.sqlalchemy.org/)

Please note, people have been making APIs for a loooong time now. So there are loads of cool and useful tools out there that make this kind of thing quick and easy. That said: it's super important that you know how to make one from scratch on your own instead of just using someone else's stuff.

What you need is a profound apprectation for what an API is and how it works.

## Why Flask?

Firstly Flask is simple compared to Django. You can jump right in and learn the API lessons we are trying to teach here. The lessons you learn in Flask are very transferrable - if you do get into Django later on then you'll have a good understanding of its foundations by default.

## Let's go

Create a Flask app that exposes a REST API for keeping track of computers owned by Umuzi.

Just make one table in your database: Computer.

For every computer we'll need to know:

- hard drive type
- processor
- amount of ram
- maximum ram
- hard drive space
- form-factor (mini, mini,etc)

Note that some of the fields can only allow certain values. This is often called enumeration.

Expose some REST api endoints. The content type must be json.

The following operations should be allowed (and should be exposed at well named urls)

1. List all computers
2. Add a computer
3. Edit a computer
4. Delete a computer

## Bonus!

Umuzi is growing pretty fast. So that means we keep having to buy computers. Eventually when you call the list computers endpoint the list will be way too long.

To combat this there is a technique called paging.

Implement that :)

## Resources

- [Official Flask Tutorial](https://flask.palletsprojects.com/en/1.1.x/)
- [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)