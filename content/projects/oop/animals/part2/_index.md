---
_db_id: 225
content_type: project
flavours:
- any_language
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

In this challenge you will update your current Animals project and add unit tests to the project.

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

### JavaScript

Your directory structure should look like this:

```
    >node_modules    <---- make sure this is in your .gitignore
    >spec
        > support
            - jasmine.json
        - animals_spec.js
    >src
        - animals.js
    - package.json
```

### Python

Your directory structure should look like this:

```
├── animals
│   └── animals.py
├── setup.py
├── requirements.txt
├── .gitignore
└── tests
    └── test_animals.py

```

## General Instructions

1. Update the `Animal` super class `eats()` function to return a String, "Food".
2. The `Dog` and `Cat` class `sounds()` functions remain as per part 1 of the project.
3. Make sure the `makeAllSounds()`/`make_all_sounds()` method still works properly.
4. See the pseudocode examples below for what kinds of things should be tested.

### For Java

You'll be using JUnit.
Create a class called `AnimalTests`.

```
// Java

Dog dog = new Dog()

dog.eats()    // returns 'Food'

Cat cat = new Cat()

cat.sounds() // returns 'Meow'
```

Now let's add our first JUnit test to our `AnimalTests`. The class should have the following methods `TestDogSound()`, `TestDogEats()`, `TestCatSound()` and `TestCatEats()`. Each method should have the @Test tag placed above it, the tests should work as follows:

```
// Java

//Dog Tests
Test -> Does dog eat Food should Pass
Test -> Does dog eat food should Fail

//Cat Tests
Cat cat = new Cat();
Test -> Does cat Bark should Fail
Test -> Does cat Meow should Pass
Test -> Does cat eat meat should Fail
Test -> Does cat eat Food should Pass
Test -> Does cat eat food should Fail

```

### For JavaScript

Use Jasmine to test your code.

```
// JavaScript

let dog = new Dog()

dog.eats()    // returns 'Food'

let cat = new Cat()

cat.eats()    // returns 'Food'
```

Then create tests for your `eats()` and `sounds()` methods on the `Dog` and `Cat` classes with Jasmine.

```
// JavaScript

//Dog Tests
let dog = new Dog();
Test -> Does dog eat Food should Pass
Test -> Does dog eat food should Fail
Test -> Does dog Roar should Fail
Test -> Does dog Bark should Pass

//Cat Tests
let cat = new Cat();
Test -> Does cat Bark should Fail
Test -> Does cat Meow should Pass
Test -> Does cat eat meat should Fail
Test -> Does cat eat Food should Pass
Test -> Does cat eat food should Fail

```

### For Python

Use pytest to test your code.

Please refer to the following to find out more: {{% contentlink path="topics/python-specific/automated-testing-with-pytest" %}}

```
# Python

dog = Dog()
dog.eats()    # returns 'Food'

```

Remember the correct naming convention for the tests in your `test_animals.py` file.

```
# Python

#Dog tests
dog = Dog();
Test -> Does dog eat Food should Pass
Test -> Does dog eat food should Fail
Test -> Does dog Roar should Fail
Test -> Does dog Bark should Pass

#Cat Tests
cat = Cat();
Test -> Does cat Bark should Fail
Test -> Does cat Meow should Pass
Test -> Does cat eat meat should Fail
Test -> Does cat eat Food should Pass
Test -> Does cat eat food should Fail

```

### Up for a Challenge?

This section is not compulsory but if you do this we'll think you're cool.

Add some extra tests for your Home class. Make sure that it makes all the right noises and that you can't adopt the same pet twice.

## Instructions for Reviewers

- There should be no global variables.
- If a variable is only used within a given method, then constantly referring to it as `self.variable`/`this.variable` isn't necessary.
- `eats()` method should return "Food" and not print it.
- There should be a test for each method in the child classes.
- `Dog` and `Cat` class `sounds()` should return their respective sounds "Bark" and "Meow".
- There should be a test for each method in the child classes.
