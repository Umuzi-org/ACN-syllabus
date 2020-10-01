---
_db_id: 201
available_flavours:
- kotlin
content_type: project
ready: true
submission_type: repo
title: Incremental Counter
---

This project is an introduction to how the ui of an app communicates with the code in the associated activity.

## Note

- You will make use of xml to create the ui and kotlin to handle events and logic.
- Use git: push your code every day. Maybe even a few times every day. If you don't back up your work and something terrible happens to your computer then you will not be granted an extension. Make sure your commit messages make sense
- Be careful when naming your functions, variables and ui elements. Make sure they are clear and easily understandable.

When creating an element in xml, be sure to indicate in the name what kind of element this is.

example: When creating a button that's purpose is to save the data on the screen, the name of the element can either be saveButton or btnSave.

## Project Description

In this project you will create a screen containing 2 Buttons, a TextView and an EditText.

- The TextView will start with a default value of "0".
- The EditText should accept an integer input.
- 1 Button will, when pressed increment the value of the TextView by the number in the input field.
- 1 Button will, when pressed decrement the value of the TextView by the number in the input field.

The app should handle situations where a user inputs a non-numerical value by displaying a popup message indicating to the user that the input data was incorrect.