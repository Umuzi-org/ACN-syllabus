---
_db_id: 27
content_type: workshop
ready: true
title: Basic intro to oop with IntelliJ
---

This is a live coding workshop. To pull it off you need a computer with intelliJ installed. Ideally you should have already started a gradle project before the workshop begins because it takes a little bit of time.

The following class hierarchy is useful for explaining this stuff:

- base class Car
    - constructor takes a colour 
    - position starts at 0
    - drive function increments position 
- Bakkie inherits from Car
- RaceCar inherits from Car
    - these are faster thn bakkies
    - default colour 

Cover the following topics:

- Java requires all executable code to be wtrapped in a class
- Difference between classes and objects
- How to instantite different objects, make 2 cars with different colours, chow that their attributes are independent 
- Inheritance and overrides

Also be sure to cover clean coding best practices, there is a lot of kak on the internet

- Flat is better than nested
- readability counts
- reusability counts
- dont put your main method inside a class that you intend to instantiate
- dont put Bakkie inside the Car or RaceCar class. It gets its own file
- use sensible names. names matter