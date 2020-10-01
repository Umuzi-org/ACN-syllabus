---
_db_id: 420
content_type: project
ready: true
submission_type: nosubmit
title: build a Chrome Extension that measures time spent in meetings
---

## Who should do this?

This project doesn’t have a lot to do with Tilde or the Recruitment Portal just yet. It’s just a cool fun thing. Note, I’ve personally never done this kind of thing so it should be for someone who is up for a challenge.

Chrome extensions make heavy use of JS

## Spec

### Part 1

Create a chrome extension that monitors the time you spend in any Google meetings. You can tell if a tab is relevant by looking at the url.

The extension should record:

- Start-time
- End-time
- Full url
  For each meeting.

See what other info you can grab. Eg, can you record who else is in the meeting?

For now you can just store your data using the Storage api (linked to at the end of this document)

Create a mechanism for displaying the data you collected. You can just put the data in a `<table>` for display, or you can draw it some other way

### Part 2

Get the chrome extension to also measure your internet connection strength during meetings.

## Resources

- https://developer.chrome.com/extensions/devguide
- https://developer.chrome.com/extensions/tabs
- https://developer.chrome.com/extensions/storage