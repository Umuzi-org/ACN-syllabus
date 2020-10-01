---
_db_id: 419
content_type: project
ready: true
submission_type: nosubmit
title: Pair Stairs
---

## Who should do this?

We have some options.

1. It could be fully implemented as a React frontend-only app BUT this would then just be a proof of concept, it wouldn’t be practically useful without a database
2. It could be fully implemented using only Django. This would be a useful thing
3. A full stack app would also work - a React frontend dev working with a Django dev. This would be the most awesome but also the most difficult because teamwork is hard. If you go this route then use Django Rest Framework to expose apis from Django.

## Spec

Create an application that keeps track of pair programming sessions between people. Take a look at this: https://tanzu.vmware.com/content/blog/pair-programming-matrix

### Data Entry

Basically what you would need to do is record pairing sessions like this

1. Allow the user to enter/select 2 names
2. The user can say what the pairing session was about. Eg: Factoryboy on Tilde attendance app
3. Specify date and time that the session happened

Every time the form is submitted then the data is saved. If you are doing a pure React implementation then you can just put it in your app state or, preferably, in a redux store.

### Display the stairs

The other piece of functionality is of course drawing the stairs graphic to display how many times people paired together.

Step 1: Draw all the sessions

Step 2: Add a date filter so we can see how many sessions happened between two dates

Step 3: If the user clicks on a person’s name then your application must display all the things that were covered in pairing sessions for that user.

Eg:

- Tshepo paired with Boitumelo and they worked on "Factoryboy on Tilde attendance app"
- Thsepo paired with Margaret and they worked on "writing selenium tests for user registration on the recruitment portal"

If only those 2 sessions have been recorded then we can say that

- Tshepo worked on:
  - "Factoryboy on Tilde attendance app"
  - "writing selenium tests for user registration on the recruitment portal"
- Boitumelo worked on:
  - "Factoryboy on Tilde attendance app"
- And Margaret worked on:
  - "writing selenium tests for user registration on the recruitment portal"

## Resources