---
_db_id: 695
content_type: project
flavours:
- python
ready: true
submission_type: repo
tags:
- FileIO
title: interacting with files
---

You are required to create a back-end service that will help capture basic information about prospective students who come to inquire here at Umuzi. In this project you'll just be storing and retrieving information from plain old json files.

## Instructions

1. Create a class called `Visitor`. Instances of this class should have the following properties:

- full name
- age
- date of visit
- time of visit
- comments
- name of the person who assisted the visitor

2. Create a function called `save` that saves the visitor's data to a JSON file. The file name should be named like this, `visitor_{their_full_name}.json`.

```
alice.save()   # results in visitor_alice_cooper.json
bob.save()     # results in visitor_bob_marley.json
charlie.save() # results in visitor_charley_sheen.json
```

Notice that the full name used in the file is all lower-case and spaces are replaced by underscores.

3. Create a function called `load` that takes in a name and then grabs a Visitor object from file. It should return the visitors instance.

For example:

```
Visitor.load("Alice Cooper")
# returns all of Alice's goodies

Visitor.load("Bob Marley")
# Same deal for good ol Bob
```

## Resources

- [Working With Files in Python](https://realpython.com/working-with-files-in-python/)
- [JSON](https://www.w3schools.com/js/js_json_intro.asp): Make sure you understand everything up to the end of "JSON Arrays"
- [Python JSON package](https://www.w3schools.com/python/python_json.asp)

## Up for a challenge?

Here are some upgrades you can add to your project if you are up for it.

5. Make use of integer ids when saving things to files. Update your save function so it works like this:

```
alice.save()   # results in visitor_1.json
bob.save()     # results in visitor_2.json
charlie.save() # results in visitor_3.json

alice.comments = "Kinda weird, I don't think he'll fit in"
alice.save()   # results in an UPDATE to visitor_1.json
```

Your load function should also get a bit of an update.

```
charlie = load(3)
charlie.comments = "Winning!"
charlie.save() # results in an UPDATE to visitor_3.json
```

6. Add tests to your project to make sure all the functions are working as specified. Since you'll be interacting with files, you'll need to know about mocks. Check out the python resources from here {{< contentlink path="topics/unit-testing-mocks-and-spies" >}}.

## Instructions for reviewer

- The load function should return a visitor instance and not just print the visitor data.
- Edge cases should be catered for. The learner should make sure that the load function takes in the proper data type.
- Please pay careful attention to DRY code. How do you do this:
- **If the learner completed point 6 under "Up for a challenge?"** the learner should use mocks if/when testing this project - since the project requires interacting with the file system.

 > Imagine that the code produced by the learner needs to be maintained and some parts of the code will have to change over time. Ideally, changes to the code should be made just once, and that change should affect everything else without going through the file(s) looking to change the same thing.