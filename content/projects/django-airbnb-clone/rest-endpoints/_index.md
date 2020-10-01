---
_db_id: 542
available_flavours:
- django
content_type: project
from_repo: projects/django-airbnb-clone/intro
prerequisites:
  hard:
  - projects/django-airbnb-clone/intro
  soft: []
submission_type: continue_repo
title: CloudBnb - Expose apis to be consumed by modern mobile app
---

Django is great and all but the frontend it renders using views and templates is a little bit limited.

Imagine our airbnb clone becomes super duper popular and there is a business decision to invest in different kinds of frontends.

For example maybe the decision is made to use Ionic to build a cross-platform hybrid frontend. Or maybe React will be used to make a pwa. Or any number of other things.

By exposing nice clean APIs, we "decouple" our django app from the frontend. That gives us a lot of freedom in the tools we use.

Can you think of other situations where exposng APIs would add flexibility to our application?

## User journey

We have 2 main kinds of users. Supply users and Demand users. On the supply side we have people who own property and try get it rented out. On the demand side there are people who need a place to stay.

We're going to focus on the demand side now. The reasons for this are:

- there are likely more "demand" users than "supply" users
- our "demand" users are often people who are travelling, so they are morelikely to use their phones for making bookings.

## Requirements

Expose a bunch of apis in order to allow travellers to do everythin they need to do. This includes:

- registering on the system
- logging in and out
- searching for properties
- getting detailed info on a specific property
- making a booking

## Technical requirements

- Use the Django Rest Framework to do this.
- Test your api
- Keep things DRY!