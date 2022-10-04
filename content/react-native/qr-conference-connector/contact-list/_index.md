---
title: "QR conference connector - Contact list"

content_type: project
flavours:
- javascript
- typescript
from_repo: react-native/qr-conference-connector/proof-of-concept
prerequisites:
  hard:
    - react-native/harvard-cs-50-m/08-data
    - react-native/qr-conference-connector/proof-of-concept
ready: true
submission_type: continue_repo
---

Now that you have the basics of scanning the QR code down, it's time to make this app into something genuinely useful.

## Storage 

Make use of SQLite to save the contacts. As soon as the user scans a qr code then the data should be added into the database.

If the user scans the same QR code twice then we only want one entry in the database.

## Contact list screen 

Create another screen that displays a list of all the contacts that the user has scanned.  This list should work as follows:

For each contact, please display:
    - profile picture
    - name
    - status

Please make sure that the user can scroll through the list. There might be a lot of contacts.

Clicking/pressing on a contact should redirect the user to a contact "details" page

## Navigation 

There are now 3 screens:

- The camera screen: for scanning qr codes.
- The contact details screen: for viewing the details of one contact
- The contact list screen: for seeing a list of all the contacts 

When the user is viewing the list screen, they should be able to navigate to:

- the camera
- any individual contact

When the user is on the contact details screen, they should be able to navigate:

- the camera
- back to the list

When the user is on the camera screen they should be able to "go back" to wherever they were before.


## Testing 

Now that your code is doing real stuff, it is important to 