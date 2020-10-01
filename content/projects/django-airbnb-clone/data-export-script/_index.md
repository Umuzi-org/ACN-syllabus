---
_db_id: 546
available_flavours:
- django
content_type: project
from_repo: projects/django-airbnb-clone/intro
prerequisites:
  hard:
  - projects/django-airbnb-clone/intro
  - projects/django-airbnb-clone/users-can-make-bookings
  soft: []
ready: true
submission_type: continue_repo
title: CloudBnb - Data export script
---

Generally businesses have a whole lot of people who are very comfortable dealing with spreadsheets and possibly even have their own business processes built around them. So it's often useful to write a quick little export script for internal use. Generally building little export scripts is much quicker than writing a whole big frontned.

## Instructions

Create a Django managment script that you can run to create an excel spreadsheet of booking data for a single month.

We need to see the following data in the sheet:

1. property owner email address
2. area where the property is
3. start and end dates of the booking
4. total price of booking
5. number of guests
6. the id of the booking

The script should take a command line parameter that specifies the month and year of the data export.

By default the exporter should filter for bookings that are within the current month.

## Resources

- https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/
- https://openpyxl.readthedocs.io/en/stable/