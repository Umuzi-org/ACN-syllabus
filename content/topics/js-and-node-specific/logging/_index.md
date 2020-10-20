---
_db_id: 128
content_type: topic
ready: true
title: Logging in Node and JS
---

Please make sure you read and understand this before moving forward: {{% contentlink path="topics/logging" %}}

**Why we would like to log**

- Quick debugging of unexpected behavior during development
- Browser-based logging for analytics or diagnostics
- Logs for your server application to log incoming requests, as well as any failures that might have happened
- Optional debug logs for your library to assist the user with issues
- Output of your CLI to print progress, confirmation messages or errors

The most basic form of logging in javascript is console logging

The console object provides access to the browser's debugging console and though it might differ from browser to browser they're a set of functions common to all
see more features [here](https://developer.mozilla.org/en-US/docs/Web/API/console)

```
console.log('Logging in Node and JS');
```

**Log Levels**

But, as you know, there are multiple ways and places one can log to, like output logs in a file or on a reporting tool or intecepting a request to the backend. For such activities you might need more than just console.logging. Lucky for us Node provides a few options for this.

- Middleware
  - Expressjs
- Packages such as:
  - Winston
  - Node-Loggly
  - Morgan
  - Retrace agent for server logs

**Resources for reading**

- https://www.twilio.com/blog/guide-node-js-logging
- https://stackify.com/node-js-logging/