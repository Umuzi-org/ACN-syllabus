---
title: "QR conference connector - Adding tests"
content_type: project
flavours:
- javascript
- typescript
from_repo: react-native/qr-conference-connector/proof-of-concept
prerequisites:
  hard:
  - react-native/qr-conference-connector/proof-of-concept
  - react-native/testing-with-jest
  - react-native/harvard-cs-50-m/13-deploying-and-testing
  - react-native/qr-conference-connector/contact-list

ready: true
submission_type: continue_repo
---

## Instructions

As you know,testing is always a good idea!

Please add jest based unit tests to all your components

In this project we would like to see that you are making good use of snapshot testing.

Please put your test code with the component under test. For example, if you had a single button component you might do this:

```
src/
├─ components/
│  ├─ button.js
│  ├─ button.style.js
│  └─ button.test.js
```

In other words, your tests should be co-located with the code under test. 