---
_db_id: 794
content_type: project
flavours:
- javascript
- typescript
prerequisites:
  hard:
  - react-native/harvard-cs-50-m/04-react-native
ready: true
submission_type: repo
title: QR conference connector - Proof of concept
---

## The scenario 

You are a part of an organizing team for a tech conference. A conference is a great place to network and meet like-minded geeks. A lot of the time, people who meet at a conference want to stay in touch after the event. This means that the attendees spend a lot of time trading contact information. This is a tedious and error prone thing to do. 

Your job is to solve this with technology!

## Solution

After some brainstorming with the conference team, you have come up with the following solution:

1. All conference attendees will get a name badge as they enter the conference
2. Each name badge will have a unique qr code printed on it, the qr code will contain the person's contact information
3. The conference app will have a qr scanning function, people will be able to scan each other's name tags to quickly get the right info.

## QR code specification 

QR codes can hold up to 4000 characters of info. Your QR code should contain the following information:

- name (required)
- email address (required)
- link to profile pic (required)
- status (optional) - this is a string of text, similar to a tweet
- github username (optional)
- linkedin profile (optional)
- twitter handle (optional)
- personal website url (optional)
- company name (optional) 
- company url (optional) 

Since the number of characters you can put in a QR code is limited and we might want to save space later, please format your data as YAML and NOT JSON.

You might need to do some research here.

## App specification

1. When you open the app then it should immediately be ready to scan a qr code (after camera permissions have been granted)
2. As soon as a qr code is detected, the app should display the person's details. Please make sure that everything that should be a link, behaves like a link. Eg if a person includes their github username, then pressing/clicking on their username should link you to their github profile.

## Component library

Please use [NativeBase](https://nativebase.io/) to make your app beautiful. NativeBase is a component library with a really nice feature set and good documentation. It's also fairly straightforward to set up. 

## Extra instructions

- Please create a directory in your repo called "qr_code_samples". Put at least 5 qr code images into the directory. This will make it easier for the reviewers to test your app.
- Your README file should include screenshots of your app