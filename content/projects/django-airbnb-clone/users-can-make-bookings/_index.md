---
_db_id: 540
available_flavours:
- django
content_type: project
from_repo: projects/django-airbnb-clone/intro
prerequisites:
  hard:
  - projects/django-airbnb-clone/intro
  - projects/django-airbnb-clone/property-model-and-admin-panel
  - projects/django-airbnb-clone/property-search
  - projects/django-airbnb-clone/user-registration
  soft: []
ready: true
submission_type: continue_repo
title: CloudBnb - Users can make bookings
---

Once a user has found where they would like to stay, they can make a booking.

## Data Model

Make a new model to represent a `Booking`. It should refer to a `Property` and a `User`. A Booking will have the following attributes:

- start and an end date.
- number of guests
- comments

## Frontend

When booking a place, a user needs to specify all the info required by the model.

If the user tries to make a booking that overlaps with existing bookings, show them an error message. For example if a user tries to make a booking for the 5th to the 7th of this month, and another user already has a booking from the 6th to the 9th then there is a problem.

Note that one user can check out on the same day that another one checks in.
For example if a user tries to make a booking for the 5th to the 7th of this month, and another user already has a booking from the 7th to the 9th then there is No problem. The one user will leave the accomodation on the morning of the 7th and the other one will arrive later that day.

If a user tries to book for too many people then that is also an error. For example if a user tries to book a 2-guest apartment and tries to squeeze in 8 people then that would be a problem.

If the user tried to hake a booking for 1 or 2 guests then that would be fine.

## Notes on error messages

The user experience must not be confusing, the error messages need to make sense to your grandma.

Dont say "Integrity Error" or "Your form is wrong" or any such nonesense. Empathise with the user. Dont say or do confusing things. Generally if you confuse a user they leave and dont come back.