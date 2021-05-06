---
_db_id: 223
content_type: project
flavours:
- any_language
prerequisites:
  hard: []
  soft: []
ready: true
story_points: 2
submission_type: repo
tags:
- oop
title: Person
---

Create a `class` called `Person` which defines the generic data and functionality of a human.

A class is a collection of attributes and functions. Different languages use different terminology for these things, but the bacic concepts are the same.

Give your `Person` class should have the following attributes:

- name
- age
- gender
- interests. This is a list or array of strings

Give your `Person` class a `hello` function:

Example usage:

```
// JavaScript:

let person = new Person('Ryan',30,'male',['being a hardarse','agile', 'ssd hard drives'] )
let greeting = person.hello()
console.log(greeting)
```

```
# Python

person = Person('Ryan',30,'male',['being a hardarse','agile', 'ssd hard drives'] )
greeting = person.hello()
print(greeting)
```

```
// Java

Person person = new Person(
    "Ryan",30,"male",
    new String[] {"being a hardarse", "agile", "ssd hard drives"})
String greeting = person.hello()
System.out.println(greeting)
```

This should output:

```
Hello, my name is Ryan and I am a 30 year old male. My interests are being a hardarse, agile and ssd hard drives.
```

In OOP this is known as abstraction. We created a simple model of a more complex thing. We only represent the attributes and functionality that we need.

When an object instance is created from a class, the class's constructor function is run to create it. This process of creating an object instance from a class is called instantiation — the object instance is instantiated from the class. `person` is an instance of `Person`

## Instructions for reviewer

1. **Naming convension** - Unclear names are bad, make sure variable names have clear meanings, stick to javacript camelCasing not Camel_Casing and name it what it is, the class and function should have the exact name and spelling as the example above.
2. **Global variables** - are bad cause their values can be changed by any function and reduce flexibility of the program, it is suggested not to use global variables but instead use local.
3. **Dry and clean Code** - Make sure that the code is well documented, dry and clean. Clean code is easier to read and takes less time to fix bugs if there are any. Dry code means no repeating the same code, rather use a function and call it when needed. check if there are no repeated code anywhere.
4. **Commented code** - check if there are no commented code in the project file, commented code is no good as it can be a blocker and take up unecessary space.
5. **Attributes** - Make sure that the class is using all of the attributes stated in the instructions above.
6. **Multiple Interests, Commas and Spacing** - Make sure that the interests array attribute can take in multiple interests and they all get printed out seperated with a comma and space, and the last interest should have an ``and`` before it.
7. **Component or not yet component** - If all of the instructions above have not been bet then the recruit should get a ``NYC`` with the instructions that have not been followed in his feedback.
## Acceptance criteria

A person might have many interests, or they might only have 1. If they are depressed then they might not be interested in anything at all. Make sure you can handle all cases! 

Also, it's really imporant that you submit good clean code! MAke sure you name your variables clearly. Make sure you are following the convention of the langage you are using. Make sure your code in no way resembles spagetti.
