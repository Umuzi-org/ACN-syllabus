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
Hello, my name is Ryan, my gender is male and I am 30 years old. My interests are being a hardarse, agile and ssd hard drives.
```

In OOP this is known as abstraction. We created a simple model of a more complex thing. We only represent the attributes and functionality that we need.

When an object instance is created from a class, the class's constructor function is run to create it. This process of creating an object instance from a class is called instantiation — the object instance is instantiated from the class. `person` is an instance of `Person`

## Acceptance criteria

A person might have many interests, or they might only have 1. If they are depressed then they might not be interested in anything at all. Make sure you can handle all cases! 

Also, it's really important that you submit good clean code! MAke sure you name your variables clearly. Make sure you are following the convention of the language you are using. Make sure your code in no way resembles spaghetti.

## Instructions for reviewer

1. **Multiple interests, commas and spacing** - Make sure that the interests array attribute can take in multiple interests and they all get printed out separated with a comma and space, and the last interest should have an ``and`` before it also your class should contain and use all of the attributes above.
2. **Single interest or no interests** - Check if the class can work with single interests, and the string output should be different from the multiple interest output instead of `my interests are` it should be `my interest is`, also if there are no interests then the output should a string with the first 3 attributes name, age, and male `Hello, my name is Ryan, my gender is male and I am 30 years old.` and you could add something like `I have no interests`.

Mark this as Excellent if:

1. **There is a separate function just for building the interests string** If the student makes multiple small, single purpose, clear functions instead of one giant function then that is good. 
2. Makes use of templating instead of string concatenation as much as possible. In Python this means using f-strings, in Javascript it means using template literals, in Java this means using `String.format`.
