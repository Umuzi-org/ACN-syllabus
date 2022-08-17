---
content_type: topic
title: Error handling best practices
tags:
  - javascript
flavours:
  - javascript
---

## Errors are useful

There's a reason why errors are in almost all if not all languages. They serve to indicate that something bad and unintended happens. They don't exist to just be squashed or just logged.

Errors that occur usually stop and terminate the program. The most common way of handling errors in javascript is by using the [try catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) statement. This is used to try and gracefully handle the error or use info from the error to handle it accordingly.

```js
try {
  // critical code that may fail goes here
} catch (error) {
  // - if an error occurs in the try the error is caught and made available here
  // - this is where you can verify certain errors, notify the user .etc.
}
```

## Bad error handling

The following are examples of how tutorials/people handle errors:

- just print errors

```js
try {
  // code...
} catch (error) {
  console.log(error);
}
```

- just print errors with a different colour

```js
try {
  // code...
} catch (error) {
  console.error(error);
}
```

- return errors

```js
try {
  // code...
} catch (error) {
  return error;
}
```

- catch expected errors just to re-throw them without added context

```js
try {
  // code...
} catch (error) {
  throw new Error(error);
}
```

- catch but ignore the caught errors

```js
try {
  // code...
} catch (error) {
  throw new Error(
    "new error that may or may not be related to the caught error"
  );
}
```

## When to catch errors

The rule of thumb is to catch errors where you can handle them effectively, this is usually on the UI layer of an application with consumer software. That can either be by using the information from the error thrown and letting a user know if they can do something about it or just re-throwing it with more context for the developers to know what happened.

## Throwing custom errors

Throw custom errors when you know exactly what went wrong, or when you want to add more context to an existing error.

There are different kinds of syntax for throwing errors

just throwing a caught error or any type as an error

```js
// BAD - because it misinterprets where the error occurred you can throw pretty much anything as an error
throw error;

throw "some error";

throw {};
```

using the error object:

```js
// GOOD - because  it tells you exactly where the error occurred and the constructor takes in a message making it more predictable
throw new Error(error);

throw new Error("error message");
```

## Resources

- [Javascript.info error handling](https://javascript.info/error-handling) - how the try catch works and some advice on handling errors
- [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) - learn more about try catch statements
- [Stack Overflow - best practices for javascript error handling](https://stackoverflow.com/questions/6484528/what-are-the-best-practices-for-javascript-error-handling)
