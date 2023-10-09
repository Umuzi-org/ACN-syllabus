---
content_type: topic
flavours:
- python
ready: true
tags:
- python
title: Python Error Handling Best Practices
---

## Exceptions are Valuable

In Python, exceptions are like alarms that go off when something goes wrong in your code. They're not something you should ignore or just write in a log; you need to deal with them properly.

When your program runs into a problem, it can cause your program to stop unexpectedly. Python has a way to deal with these problems using try and except blocks. These blocks help you handle errors in a way that doesn't crash your program and allows you to get information about what went wrong.

## Poor Error Handling Practices

Let's explore some common mistakes in error handling:

- Just printing errors

```python
try:
  # Code...
except Exception as error:
  print(error)
```

- Just printing errors with a different colour

```python
try:
  # Code...
except Exception as error:
  print(f"Error: {error}")
```

- Returning errors

```python
try:
  # Code...
except Exception as error:
  return error
```

- Catching expected exceptions only to re-raise them without adding context

```python
try:
  # Code...
except ValueError as error:
  raise error
```

- Catching and ignoring the exceptions
  
```python
try:
  # Code...
except Exception as error:
  raise Exception("A new error that may or may not be related to the caught error")
```

## When to Catch Errors

It's important to understand when to catch errors. You should only catch errors that you can handle. If you can't handle the error, you should let it bubble up to the caller. This is especially important when you're writing a library or a module that will be used by other developers. If you catch an error that you can't handle, you're essentially hiding the error from the caller. This can lead to unexpected behaviour and bugs.

## Creating Custom Exceptions

In Python, you can create custom exceptions when you precisely understand what went wrong or when you want to provide more context to an existing exception.

By using the Exception class:

```python
# PREFERRED - It indicates the location of the exception, and the constructor accepts a message for clarity
raise Exception(error)

raise Exception("Error message")
```

## Additional Resources

[Python Official Documentation on Exceptions](https://docs.python.org/3/tutorial/errors.html) - Learn more about handling exceptions in Python.

[Real Python - Python Exceptions: An Introduction](https://realpython.com/python-exceptions/) - Comprehensive guide to Python exceptions and error handling.

[Stack Overflow - Best Practices for Python Error Handling](https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python) - Insights into Python error handling best practices.