---
_db_id: 545
available_flavours:
- django
content_type: project
from_repo: projects/django-airbnb-clone/intro
prerequisites:
  hard:
  - projects/django-airbnb-clone/intro
  soft: []
ready: true
submission_type: continue_repo
title: CloudBnb - User registration
---

## Instructions

Users from the internet need to register to use the site. Create a simple registration form. This will NOT be a part of a t admin panel. This is user facing.

We need to store the following info for the user:

- email address
- cellphone number
- profile pic

That's it really.

Users should also be able to log in and log out

## Remember KISS

For now dont worry about any kind of email/cellphone verification.
Step 1 is always just to make the code work. once you are through everything you can worry about adding bells and whistles.

## Follow best practices around User managment

Take a looks at this: https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html