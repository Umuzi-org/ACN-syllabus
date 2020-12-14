---
_db_id: 583
available_flavours:
- django
content_type: project
from_repo: projects/django-airbnb-clone/intro
prerequisites:
  hard:
  - projects/django-airbnb-clone/intro
  - projects/django-airbnb-clone/property-model-and-admin-panel
  soft: []
submission_type: continue_repo
title: Write an ETL script to populate the database
---

Let's imagine that you have contacted a person who owns a bunch of properties and they want to add all their stuff to CloudBnb in bulk. You could get someone do do manual data capturing to get all the data into your db, but that would be pretty soul-destroying work. And manual data capture is prone to human error.

Now most businesses are run on spreadsheets, so it is actually a very common task to take a spreadsheet full of data, clean it up, and stick it into your database.

## Instructions

Write a management command that:

1. Grabs data from this Google spreadsheet: https://docs.google.com/spreadsheets/d/1LU7FDyrCi-S1CYmEoIWetMhf2lUK28gz71EVcE6RJjY/
2. Saves each line into your database

Things to keep in mind:

1. The script should be idempotent. That's a funny word but basically it means that if you run the script twice, it shouldn't screw up and make duplicate properties or anything. Running the script twice should have the same effect as running the script once
2. Your script will need to be able to access Google sheets!

## Why do we care about making things idempotent?

Often an etl script will be run by some other program, for example it might be run by Airflow. Airflow is cool because it can do things like retry tasks if something seems to break. And in production, all sorts of things have downtime.

Eg: the database might be down because updates are being installed, or migrations are being run.

It should always be safe to retry your scripts.

On top of that, certain pipelines get run multiple times. For example, what if the property owner adds a whole lot of new stuff to the spreadsheet and asks you to load up the new stuff?

## Links

- To turn a Google Sheet into a dataframe: https://gspread.readthedocs.io/en/latest/
- Python management commands: https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/
- `get_or_create` is hella useful if you want to avoid duplicating data: https://stackoverflow.com/questions/1941212/correct-way-to-use-get-or-create