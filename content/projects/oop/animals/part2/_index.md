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
├── spec
|   ├── support
|   |   └── jasmine.json
|   └── animals_spec.js
├── src
|   └── animals.js
└── package.json
```

**Note**: Please export your class using the following syntax at the end of the code:

```

module.exports = {className: className}

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

1. Add tests to your project.
2. The `Dog` and `Cat` class methods should still remain as per part 1 of the project.
3. Include tests for your Home class. Make sure its methods return the correct values and that you can't adopt the same pet twice.
4. See the pseudocode examples below for what kinds of things should be tested.

### For Java

You'll be using JUnit.
Create a class called `AnimalTests`.

Now let's add our first JUnit test to our `AnimalTests`. The class should have the following methods `TestDogSound()`, `TestDogEat()`, `TestCatSound()` and `TestCatEat()`. Each method should have the @Test tag placed above it, the tests should work as follows:

```

//Dog Tests
Dog dog = new Dog();
Test -> Does <dog name> eats should Pass
Test -> Does dog Bark should Pass
Test -> Does dog Meow should Fail

//Cat Tests
Cat cat = new Cat();
Test -> Does <cat name> eats should Pass
Test -> Does cat Meow should Pass
Test -> Does cat Bark should Fail

```

### For JavaScript

Use Jasmine to test your code.

Then create tests for your `eat()` and `sound()` methods on the `Dog` and `Cat` classes with Jasmine.

```

//Dog Tests
let dog = new Dog();
Test -> Does <dog name> eats should Pass
Test -> Does dog Bark should Pass
Test -> Does dog Meow should Fail

//Cat Tests
let cat = new Cat();
Test -> Does <cat name> eats should Pass
Test -> Does cat Meow should Pass
Test -> Does cat Bark should Fail

```

### For Python

Use pytest to test your code.

Please refer to the following to find out more: {{% contentlink path="topics/python-specific/automated-testing-with-pytest" %}}

Remember the correct naming convention for the tests in your `test_animals.py` file.

```

#Dog tests
dog = Dog()
Test -> Does <dog name> eats should Pass
Test -> Does dog Bark should Pass
Test -> Does dog Meow should Fail

#Cat Tests
cat = Cat()
Test -> Does <cat name> eats should Pass
Test -> Does cat Meow should Pass
Test -> Does cat Bark should Fail

```

## Instructions for Reviewers

- There should be no global variables.
- If a variable is only used within a given method, then constantly referring to it as `self.variable`/`this.variable` isn't necessary.
- There should be a test for each method in the child classes.

```

```
