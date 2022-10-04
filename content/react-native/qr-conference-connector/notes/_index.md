---
_db_id: 799
content_type: project
flavours:
- javascript
- typescript
from_repo: react-native/qr-conference-connector/proof-of-concept
prerequisites:
  hard:
  - react-native/qr-conference-connector/proof-of-concept
  - react-native/qr-conference-connector/adding-tests
ready: true
submission_type: continue_repo
title: QR conference connector - Notes
---

It is often useful to keep some notes about the people you meet, especially if you are meeting a lot of new people! 

## Contact details page 

Add a small form to the bottom of the contact details page. It should just have one textarea. 

There are a few scenarios to cover:

1. If there are no notes about the user then the textarea should have a placeholder such as "You can make notes here..."
2. If there are already notes saved in the database, then the textarea should be pre-populated with that info
3. If the user has not made any changes to the notes in the text area  then the save button should be disabled or invisible.
4. If the user has unsaved changes then they should have access to a "save" button and a "cancel" button.

## Contact list page 

If a contact has notes then add a little icon to their element.

You could use something like this, or something else: https://icons.expo.fyi/AntDesign/filetext1