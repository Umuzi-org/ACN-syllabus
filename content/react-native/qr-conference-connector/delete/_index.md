---
title: "QR conference connector - Delete"
content_type: project
flavours:
- javascript
- typescript
from_repo: react-native/qr-conference-connector/proof-of-concept
prerequisites:
  hard:
  - react-native/qr-conference-connector/proof-of-concept
  - react-native/qr-conference-connector/contact-list
ready: true
submission_type: continue_repo

---

Let's allow the user to delete their contacts.

## Contact details page 

Add a "delete" button.

If the user clicks on the button then ask "Are you sure you want to delete this contact?" before deleting it.

If the user confirms that they want to delete the contact then:

- update the database
- redirect the user to the contact list page

## Contact list page 

If a contact has notes then add a little icon to their element.

You could use something like this, or something else: https://icons.expo.fyi/AntDesign/filetext1 




