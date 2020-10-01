---
_db_id: 260
available_flavours:
- python
content_type: project
ready: true
submission_type: repo
title: expose a simple JSON rest api
---

## Instructions

### Part 1: Data layer

1. Create a class called Visitor. Instances of this class should have the following properties:

- full name
- age
- date of visit
- time of visit
- comments
- name of the person who assisted the visitor

2. Create a function called `save` that saves the visitor's data to a JSON file. The file name should be named like this `visitor_{some_number}.json`. The number part of the file name should be automatically generated as you save the visitor. eg:

```
alice.save()   # results in visitor_1.json
bob.save()     # results in visitor_2.json
charlie.save() # results in visitor_3.json
```

3. Create a function called `load` that takes in a number and returns a Visitor object that was saved to file.

eg:

```
alice = load(1)
bob   = load(2)
```

4. Make sure that this kind of functionality works appropriately

```
alice = Visitor(...stuff)
alice.save() # creates a file
alice.age = 93
alice.save() # DOES NOT create a file. This updates the original file
```

This should also work:

```
bob = load(2)
bob.comments = "great personality"
bob.save() # should update visitor_2.json
```

### Part 2: Expose JSON api

Use Flask to expose the following functionality:

- create a new Visitor in the database
- delete a single Visitor from the database
- delete all Visitors
- view all Visitors
- view a single Visitor
- update a single Visitor

#### Something to think about

Imagine that your api is hosted somewhere on the internet and is very popular. Lots of people are using it.

- What might happen if many people access the "create visitor" functionality at the same time?
- what might happen if many people ty to update the same visitor at the same time?
- what might happen if someone deletes all the visitors while someone else is trying to create a new one?

A lot of really weird bugs can creep in. This class of error is generally referred to as a race condition. There are tools and techniques that exist to help deal with this kind of thing. In general it's good to keep race conditions in mind whenever dealing with processes that access data in parallel.

## Resources

- [Python and JSON](https://www.w3schools.com/python/python_json.asp)
- [Official Python tutorial](https://docs.python.org/3/tutorial/)
- [Official Flask tutorial](http://flask.pocoo.org/docs/1.0/tutorial/)