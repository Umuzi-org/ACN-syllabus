---
_db_id: 838
content_type: topic
title: Python Errors
---

## Problem 1: Catchalls

If you see this kind of thing it's probably wrong.

```
try:
    a whole lotta stuff
except:
    handle errors
```

This is considered bad practice because catchall exceptions can hide the root cause of an error and make it more difficult to troubleshoot and fix the problem. Additionally, catchall exceptions can silence tracebacks, which can make it harder to understand what went wrong in the code. It is generally recommended to catch specific exception types whenever possible, so that you can handle errors in a more targeted and appropriate way.

rather:

```
try: 
    a little bit of stuff. Keep this as small as possible
except TheExceptionYouActuallyIntendToCatch:
    handle the error
```

## Problem 2: Squashing and logging

This kind of thing should be avoided. 

```
try:
    stuff
except SPecificException as e:
    print(e)
```

Basically that says: Squash the error, log it, and move on. There are situations where that is the right thing to do. Usually it's the wrong thing to do. 

Did you know that errors were implemented by very clever people? They were implemented in Javascript, Python, C#, Java, Clojure, Go and basically all languages because they are actually really useful. Always imagine how the code might be used in a larger application. If you are printing your errors to the then any calling code would need to monitor the logs in order to know if there was an error and figure out what to do about it. This would be insane. 

If you aren't handling an exception then don't catch it.