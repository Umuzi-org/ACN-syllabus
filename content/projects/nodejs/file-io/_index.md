---
_db_id: 280
available_flavours:
- javascript
content_type: project
pre: '<b>1: </b>'
prerequisites:
  hard:
  - topics/js-and-node-specific/node
  soft: []
ready: true
story_points: 3
submission_type: repo
tags:
- Node
- FileIO
title: Node & File IO
weight: 1
---

You are required to create a back-end service that will help capture basic information about prospective students who come to inquire here at Umuzi. In this project you'll just be storing and retrieving information from plain old json files.

## Instructions

1. Create a class called Visitor. Instances of this class should have the following properties:

- full name
- age
- date of visit
- time of visit
- comments
- name of the person who assisted the visitor

2. Create a function called `save` that saves the visitor's data to a JSON file. The file name should be named like this `visitor_{their_full_name}.json`.

```
alice.save()   # results in visitor_alice_cooper.json
bob.save()     # results in visitor_bob_marley.json
charlie.save() # results in visitor_charley_sheen.json
```

Notice that the full name used in the file is all lower-case and spaces are replaced by underscores.

3. Create a function called `load` that takes in a name and then grabs a Visitor object from file. It should simply `console.log` the visitor.

eg:

```
load("Alice Cooper")
// prints out all of Alice's goodies


load("Bob Marley")
// Same deal for good ol Bob
```

## Resources

- [Accessing the file system](https://www.w3schools.com/nodejs/nodejs_filesystem.asp)
- [JSON](https://www.w3schools.com/js/js_json_intro.asp): Make sure you understand everything up to the end of "JSON Arrays"

## Up for a challenge?

Here are some upgrades you can add to your project if you are up for it.

4. Update your `load` function so that it returns an instance of `Visitor` instead of just `console.log`ging it. You'll need to learn a little bit about Syncronous versus Asyncronous code to get this one right :)

5. Make use of integer ids when saving things to files.

Update your save function so it works like this:

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