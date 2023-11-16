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
- skill/oop
title: Person
---

## Language specific setup

### JavaScript

Your directory structure should look like this.

```
person.js
```

It is important that you export your class correctly. Include the following line at the end of your `person.js` file.

```
module.exports = { Person };
```

### Python

Please name your files and folders like this:

```
person.py
```

### Java

```
Person.java
```

If you would like to add another class with a main function so you can test drive your work then please go ahead.

Your `Person` class MUST NOT have a main function. If you want to make another class that does have a main function then that is ok.

## Instructions

Create a `class` called `Person`.

Your `Person` class should have the following attributes:

- name
- age
- gender
- interests. This is a list or array of strings.

Give your `Person` class a `hello` function:

Example usage:

```
// JavaScript:

const person = new Person({ // Take note of the curly brackets here
  name: "Ryan",
  age: 30,
  gender: "male",
  interests: ["being a hardarse", "agile", "SSD hard drives"],
});
const greeting = person.hello();
console.log(greeting);
```

```
# Python

person = Person(
    name="Ryan",
    age=30,
    gender="male",
    interests=["being a hardarse", "agile", "SSD hard drives"],
)

greeting = person.hello()
print(greeting)
```

```
// Java

Person person = new Person(
    "Ryan",
    30,
    "male",
    new String[] {"being a hardarse", "agile", "SSD hard drives"}
    // note that interests is an array of strings
    );
    String greeting = person.hello();
    System.out.println(greeting);
```

This should output:

```
Hello, my name is Ryan, my gender is male and I am 30 years old. My interests are being a hardarse, agile and SSD hard drives.
```

In other words, the `hello` function should return a string.

### Important notes on sentence structure

The sentence describing the `Person`'s interests should have a different format depending on how many interests that person has. Here are a few examples:

- `My interests are being a hardarse, agile and SSD hard drives.`
- `My interests are tea and cake.`
- `My interest is puppies.`
- `I have no interests.`

Pay very careful attention to the format of the strings above. Where are the commas? Which ones have an "and"? What other punctuation is there? Learn to pay attention to the fine details.

Make sure that the `hello` function returns EXACTLY the correct string. The format should match the examples above.

## Push your understanding

Try to answer the following questions for yourself:

- In OOP there is a concept called "Abstraction". Do you know how abstraction relates to this project?
- What is a constructor function?
- When is a constructor called?
- Can you construct multiple instances of the same class?
- What is the difference between a class and an object?

## Instructions for reviewer

Mark this as Excellent if:

1. **There is a separate function just for building the interests string**. If the student makes multiple small, single-purpose, clear functions instead of one giant function then that is good.
2. Makes use of templating instead of string concatenation as much as possible. In Python this means using f-strings, in Javascript, it means using template literals, in Java, this means using `String.format`.
3. Also meets normal excellence criteria as specified on Tilde under "HOW DO I CHOOSE A STATUS?".