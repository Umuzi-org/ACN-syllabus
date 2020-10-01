---
_db_id: 212
available_flavours:
- java
content_type: project
prerequisites:
  hard:
  - projects/java-specific/collections
  - topics/java-specific/logging
  soft: []
ready: true
submission_type: repo
title: File IO + Logging + Errors
---

You are required to create a back-end service that will help capture basic information about prospective students who come to inquire here at Umuzi. In this project you'll just be storing and retrieving information from plain old txt files.

## Instructions

Create the following functionality in a TDD way. And make sure that everything has the correct Exception handling and those exceptional cases should have tests as well. In an error occured it through

1. Create a class called Visitor. Instances of this class should have the following properties:

- full name
- age
- date of visit
- time of visit
- comments
- name of the person who assisted the visitor

2. Create a function called `save` that saves the visitor's data to a Text file. The file name should be named like this `visitor_{their_full_name}.txt`.

**On a successful save, a log to the console should be made using log4j and the same when an error occurs;**

```
alice.save()   # results in visitor_alice_cooper.txt
bob.save()     # results in visitor_bob_marley.txt
charlie.save() # results in visitor_charley_sheen.txt
```

Notice that the full name used in the file is all lower-case and spaces are replaced by underscores.

3. Create a function called `load` that takes in a name and then grabs a Visitor object from file. It should simply `System.out.println` the visitor.

**On a successful read, a log to the console should be made using log4j and the same when an error occurs;**

eg:

```
alice.load("Alice Cooper")
// prints out all of Alice's information


bob.load("Bob Marley")
// Same deal for good ol Bob
```

## Resources

https://www.w3schools.com/java/java_files_create.asp

https://www.loggly.com/ultimate-guide/java-logging-basics/