---
_db_id: 225
available_flavours:
- any_language
content_type: project
from_repo: projects/oop/animals/part1
prerequisites:
  hard:
  - projects/tdd/simple-calculator-part1
  - projects/oop/animals/part1
  soft: []
ready: true
story_points: 3
submission_type: continue_repo
tags:
- unit-testing
- oop
title: Animals Part 2. Adding Tests
---

In this challenge you will update your current Animals project and add unit tests to the project

## Project structure

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
    |   └── java
    |       ├── Animal.java       <-------- names are important
    |       ├── Cat.java          <-------- names are important
    |       ├── Dog.java          <-------- names are important
    |       ├── Home.java         <-------- names are important
    |       └── MainProgram.java  <-------- names are important
    └── test
        └── java
            ├── CatTest.java   <-------- names are important
            └── DogTest.java   <-------- names are important
            ... other logical things
```

Please refer to the following to find out more: {{% contentlink path="topics/java-specific/project-submission-requirements" %}}

## Instructions

You'll be using JUnit.

1. Create a class called `AnimalTests`
2. Update `Animal` super class `eats()` function to return a String, "Food".
3. Update `Dog` class `sounds()` function to return a `String`, "Bark".
4. Update `Cat` class `sounds()` function to return a `String`, "Meow".

```
// Java

Dog dog = new Dog()

dog.eats()    // -> 'Food'
dog.sounds() // -> 'Barks'

Cat cat = new Cat()

cat.eat()    // -> 'Food'
cat.sounds() // -> 'Meow'
```

Now let's add our first JUnit test to our `AnimalTests`. The class should have the following methods `TestDogSound()`, `TestDogEats()`, `TestCatSound()` and `TestCatEats()`.Each method should have the @Test tag placed above it. The tests should work as follows.

```
// Java

//Dog Tests
Test -> Does dog eat Food should Pass
Test -> Does dog eat food should Fail

//Cat Tests
Cat cat = new Cat();
Test -> Does cat Barkark should Fail
Test -> Does cat Meow should Pass
Test -> Does cat eat meat should Fail
Test -> Does cat eat Food should Pass
Test -> Does cat eat food should Fail

```

### Up for a Challenge?

This section is not compulsory. If you do this we'll think you're cool.

Add some functionality to `TestDog()` and `TestCat()` so that the tests aren't case sensitive

eg:

```
Test -> Does dog eat Food -> Pass
Test -> Does dog eat food -> Pass
```