---
content_type: topic
title: Error handling best practices
---

## Errors are useful

There's a reason why errors are in almost all if not all languages. They serve to indicate that something bad and unintended happens. They don't exist to just be squashed or just logged.

The common way of handling javascript errors is by using the [try catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) statement.

## How others generally handle errors

## When to catch errors

The rule of thumb is to catch errors on the highest layer of the application where you can handle them effectively with consumer software. That can either be by using the info from the error thrown and letting a user know if they can do something about it or just rethrowing it with more context for the developers to know what happened.

## Throwing custom errors

Throw custom errors when you know exactly what went wrong, or when you want to add more context to an existing error.

There are different kinds of syntax for throwing errors

just throwing a caught errors or any type as an error

```js
// BAD - because it misinterprets where the error occured you can throw pretty much anything as an error
throw error;

throw "some error";

throw {};
```

using the error object:

```js
// GOOD - because  it tells you exactly where the error occured and the constructor takes in a message making it more predictable
throw new Error(error);

throw new Error("error message");
```
