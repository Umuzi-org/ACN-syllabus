---
_db_id: 223
content_type: project
flavours:
  - any_language
learning_outcomes:
  - code_oop_encapsulation
  - code_oop_class_instantiation
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

## Set up your environment

### JavaScript

Your directory structure should look like this.

```
├── src
|   └── person.js
└── package.json
```

### Python

Please name your files and folders like this:

```
├── person   the package under test
│   └── person.py
├── requirements.txt    installation requirements
└── setup.py            installation script for the package under test

```

The reason for this is that we have automations that will mark your work. If your work is not organised correctly then our friendly robot wont be able to mark your work.

If you want to learn more, check this out: {{% contentlink path="topics/python-specific/automated-testing-with-pytest" %}}

### Java

The code you push to git should have the following structure:

```
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    ├── main
        └── java
            ├── Main.java
            └── Person.java <-------- names are important
```

Please refer to the following to find out more: {{% contentlink path="topics/java-specific/project-submission-requirements" %}}

## Instructions

Create a `class` called `Person` which defines the generic data and functionality of a human.

A class is a collection of attributes and functions. Different languages use different terminology for these things, but the basic concepts are the same.

Your `Person` class should have the following attributes:

- name
- age
- gender
- interests. This is a list or array of strings.

Give your `Person` class a `hello` function:

Example usage:

```
// JavaScript:

let person = new Person('Ryan', 30, 'male', ['being a hardarse', 'agile', 'SSD hard drives'])
let greeting = person.hello()
console.log(greeting)
```

```
# Python

person = Person('Ryan', 30, 'male', ['being a hardarse', 'agile', 'SSD hard drives'])
greeting = person.hello()
print(greeting)
```

```
// Java

Person person = new Person(
    "Ryan", 30, "male",
    new String[] {"being a hardarse", "agile", "SSD hard drives"})
String greeting = person.hello()
System.out.println(greeting)
```

This should output:

```
Hello, my name is Ryan, my gender is male and I am 30 years old. My interests are being a hardarse, agile and SSD hard drives.
```

In OOP this is known as abstraction. We created a simple model of a more complex thing. We only represent the attributes and functionality that we need.

When an object instance is created from a class, the class's constructor function is run to create it. This process of creating an object instance from a class is called instantiation — the object instance is instantiated from the class. `person` is an instance of `Person`.

### Exports

**For those using JavaScript:** Don't forget to export your `Person` class so that the automarker may be able to access your class. You do this by including an export statement like this.

```
module.exports = { YOUR_CLASS_NAME };
```

## Acceptance criteria

A person might have many interests, or they might only have 1. If they are depressed then they might not be interested in anything at all. Make sure you can handle all cases!

Also, you must submit good clean code! Make sure you name your variables clearly. Make sure you are following the convention of the language you are using. Make sure your code in no way resembles spaghetti.

## Instructions for reviewer

### Tasks

1. **Multiple interests, punctuation, and spacing** - Make sure that the interests array attribute can take in multiple interests. The interests should all get printed out separated with a comma and space. The last interest should have an `and` before it followed by a full stop. Your class should contain and use all of the attributes above.
   The output of 2 or more interests should look like this: `Hello, my name is Ryan, my gender is male and I am 30 years old. My interests are reading and coding.`.

2. **Single interest or no interests** - Check if the class can work with a single interest and that the string output is different from the multiple interests string output. Instead of `my interests are` it should be `my interest is`.
   The output of 1 interest should look like this: `Hello, my name is Ryan, my gender is male and I am 30 years old. My interest is being a hardarse.`.
   If there are no interests(empty interests array) then the output should look like this: `Hello, my name is Ryan, my gender is male and I am 30 years old. I have no interests.`.

Mark this as Excellent if:

1. **There is a separate function just for building the interests string**. If the student makes multiple small, single-purpose, clear functions instead of one giant function then that is good.
2. Makes use of templating instead of string concatenation as much as possible. In Python this means using f-strings, in Javascript, it means using template literals, in Java, this means using `String.format`.
3. Also meets normal excellence criteria as specified on Tilde under "HOW DO I CHOOSE A STATUS?".

### Exports

**For those using Javascript:** Make sure they export their class correctly. Otherwise, the marking bot won't be able to access their code
