---
title: "QR conference connector - Favorites"
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

If you meet a lot of people at the conference then keeping them all in one long list might not be the most useful thing in the world.

Let's add a few more features to the app:

## Favorites 

If you meet someone super impressive then you will want to highlight them in the app so that they are easier to find.

By default, no contact is a favorite. The user should be able to quickly and easily be able to "favorite" or "unfavorite" any contact. 

### The contact details page

Maybe use of 2 star icons, one outlined and one filled in. The following icons would work, but you can use different ones if you want to:

- https://icons.expo.fyi/AntDesign/staro 
- https://icons.expo.fyi/AntDesign/star 

- if the user is not a favorite then show the outlined star
- if the user is a favorite then show the filled in star
- pressing/clicking on the star will toggle the user's "favorite" status 

Of course, this status needs to be saved in the database.

### The contact list page

If a contact is a "favorite" then it should be at the top of the list. 

Favorite users should be highlighted. 



