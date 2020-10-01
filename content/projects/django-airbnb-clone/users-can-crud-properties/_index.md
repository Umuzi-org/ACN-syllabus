---
_db_id: 547
available_flavours:
- django
content_type: project
from_repo: projects/django-airbnb-clone/intro
prerequisites:
  hard:
  - projects/django-airbnb-clone/intro
  - projects/django-airbnb-clone/property-model-and-admin-panel
  - projects/django-airbnb-clone/user-registration
  - topics/django/official-tutorial/part-4
  soft: []
submission_type: continue_repo
title: CloudBnb - users can CRUD properties that they own
---

Users using your application should be able to manage properties that they own. They need to be able to **C**reate, **R**ead, **U**pdate and **D**elete their properties. This is often referred to as CRUD.

We'll need views at the following urls:

- `properties/create/`: Display a form that allows a user to create a new property. If the form is saved then that property needs to be associated with the currently logged in user

- `properties/`: This should list out all the properties owned by the currently logged in user. The user should be able to see a `delete` and `edit` buttons for the different properties.
  The user should see:

  - the main image associated with the property
  - the location and desrcription
  - tags

- `properties/{id}/`: This should show all the details of a property in a form. The user can change the details and hit save.

- `properties/{id}/delete`: If the user lands on this page then display all the info about the property and have a message that says "Are you sure you want to delete this property?". The user can click on "Yes" or "No".

## Notes on branching

This spec actually has a few pieces to it.

There is a permission system thing that you ned to build. We can't let just anyone edit any property, they can only edit the stuff that they own. And there are 4 different pages that need to be implemented.

Please make many pull requests. If you make one gigantic branch with everything in it then you'll just be making the life of the reviewer hard. Plan your work properly. Every time anything gets merged into the master branch then it should make the master branch better. IT shouldn't make the master branch broken.

## Notes on UX

Always be thinking about the user experience. Think about:

- where a user will be redirected after submitting a form or taking an action.
- "escape hatches": there should always be a way for the user to navigate out of a situation. For example if the user is on the "create property" page and they decide that they actually aren't keen, what buttons can they use to get off that page? Where will the buttons take them?

## Notes on testing

Make sure you test things. Especially your permission system.