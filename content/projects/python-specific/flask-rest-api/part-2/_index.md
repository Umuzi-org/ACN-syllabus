---
_db_id: 700
content_type: project
flavours:
- python
prerequisites:
  hard: []
  soft: []
ready: true
submission_type: repo
tags: []
title: Add logging middleware to your REST API
---

Logging middleware... let's talk about each of those two words.

## Logging 

You can think of logging as really fancy `print`ing. When a serious application is running then it generally generates logs. 

These logs are useful because when something goes wrong, then it's important to be able to diagnose the problem. It's also useful for analysis, if you have a big serious web application and lots of people are accessing it, you might use logs to see what api endpoints get used the most. 

Python logging is handled with the logging package. Read more about it [here](https://docs.python.org/3/library/logging.html)

## Middleware 

When an HTTP request arrives at your application, the data in that request goes straight to your view. The view then generates a response that gets turned into an HTTP response and sent back to the client code. 

```
Client code sends http request to flask app

Flask creates a python request object and sends it to the view

View generates HTTP response as a python object

Flask generates an actual HTTP response to send to the client

```

A middleware is a piece of code that gets to process the request before and after the view. So it looks more like this:

```
Client code sends http request to flask app

Flask creates a request object object and sends it to the MIDDLEWARE

The middleware does some processing then sends the request to the view

View generates HTTP response as a python object and sends it to the MIDDLEWARE

The middleware can do some more processing before passing the response to Flask

Flask generates an actual HTTP response to send to the client
```

These resources should help you understand how to implement a middleware:

- https://medium.com/swlh/creating-middlewares-with-python-flask-166bd03f2fd4
- https://stackoverflow.com/questions/51691730/flask-middleware-for-specific-route/51820573

## Your mission

Your job is to write a middleware from scratch.

Your middleware needs to do the following:

- log an `info` message for every request. The mssage should look like this: `f"[{request_method}] {request_url}"`.  For example: `[POST] /computers`
- log a `debug` message for every request. The message should just contain the body of the request send to your app. For example if there is a POST request sent to your app in order to create a new computer in the database, then POSTed data should be logged.

The logs should be sent to a file called `requuest.log`. Please note that it is BAD practice to add log files to your git repo. You should make sure that your log files are gitignored.

The log level of your middleware should be controlled by an environmental variable called `DEBUG`.

- If DEBUG is 0 then the log level should be `info` 
- If DEBUG is 1 then the log level should be `debug`
- The default log level should be `info`

Don't worry about testing your middleware for now.