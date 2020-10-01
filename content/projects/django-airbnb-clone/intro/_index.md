---
_db_id: 539
available_flavours:
- django
content_type: project
prerequisites:
  hard:
  - topics/git-feature-branching
  - topics/django/official-tutorial/part-1
  soft: []
submission_type: repo
title: CloudBnb - intro
---

In this project we'll be building out a simple version of Airbnb. By the end there will be a lot of cool functionality. But we'll do it piece by piece.

Take a look at Airbnb if you haven't already. https://www.airbnb.co.za/

## End goal

By the end of this multi-part project we'll need the following.

- register
- make bookings for specific dates
- see stats about the properties they own

And we need to give superusers/staff access to a a few different things. But we'll get into that a bit later :)

Airbnb clone

6. expose all data with DRF
7. pull property data and draw graphs for property owner using plotlyjs

## KISS

If you haven't heard of the principle of KISS look it up now. Generally, when building a kick-ass and complicated piece of software, it's very very important to focus on what is actually required.

Many undisciplined developers fall down all sorts of rabbit holes and just build out a lot of half-broken and fully-useless bells and whistles instead of focusing.

You should always aim to follow the leanest, most steamlined path. Start off by making sure you will ne sucessful in building the stuff that is actually required before you consider scope creep.

Never heard of scope creep? Look that up too.

## Feature branching

Please follow best practices here.

## Some notes on infrastructure

Please use a Postgres database. Run it in a docker container.

We use this for Tilde:

https://github.com/Umuzi-org/Tilde/tree/master/database/localhost

And you can look at the Tilde settings.py file here to see how we use environmental variables to set up database access:

https://github.com/Umuzi-org/Tilde/blob/master/backend/backend/settings.py

## Instructions

For this introductory part of the project you'll need to just get a foundation in place on which you can work.

- Set up an empty Django project
- Connect to a postgres db
- Make sure you can create super users