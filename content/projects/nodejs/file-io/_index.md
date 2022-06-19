---
_db_id: 280
content_type: project
flavours:
- javascript
learning_outcomes:
- web_dev_file_system
- web_dev_json_file_creation
- web_dev_classes
- web_dev_methods_and_functions
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

You are required to create a backend service that will help capture basic information about prospective students who come to inquire here at Umuzi. In this project, you'll just be storing and retrieving information from plain old JSON files.

## Instructions

1. Create a class called Visitor. Instances of this class should have the following properties:

- full name
- age
- date of visit
- time of visit
- comments
- the name of the person who assisted the visitor

2. Create a function called `save` that saves the visitor's data to a JSON file. The file name should be named like this `visitor_{their_full_name}.json`.

```
alice.save()   # results in visitor_alice_cooper.json
bob.save()     # results in visitor_bob_marley.json
charlie.save() # results in visitor_charley_sheen.json
```

Notice that the full name used in the file is all lower-case and spaces are replaced by underscores.

3. Create a function called `load` that takes in a name and then grabs a Visitor object from a file. It should simply `console.log` the visitor.

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

4. Update your `load` function so that it returns an instance of `Visitor` instead of just `console.log`. You'll need to learn a little bit about Synchronous versus Asynchronous code to get this one right :)

5. Make use of integer ids when saving things to files.

Update your save function so it works like this:

```
alice.save()   # results in visitor_1.json
bob.save()     # results in visitor_2.json
charlie.save() # results in visitor_3.json

alice.comments = "Kinda weird, I don't think he'll fit in"
alice.save()   # results in an UPDATE to visitor_1.json
```
- Do not overwrite existing `.json` files when `save()` is called on a different instance.

Your load function should also get a bit of an update.

```
charlie = load(3)
charlie.comments = "Winning!"
charlie.save() # results in an UPDATE to visitor_3.json
```

## Instructions for a reviewer

- The load function should print/console.log the visitor data. Ensure that the visitor data is not returned instead. UNLESS the learner has taken on the challenge laid out in the instructions section (instruction 4)

- Edge cases should be catered for. The learner should make sure that the load function takes in the proper data type.

- The learner should use mocks and spies if/when testing this project - since the project requires interacting with the file system.

- Please pay careful attention to DRY code. How do you do this :

 > Imagine that the code produced by the learner needs to be maintained, imagine that some parts of the code will have to change over time. Ideally, changes to the code should be made just once, and that change should affect everything else without going through the file(s) looking to change the same thing.