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
submission_type: continue_repo
tags:
- unit-testing
- oop
title: Animals Part 2. Adding Tests
---

In this project you'll be testing some of your previous work.

## Project structure

### Java

Make use of Gradle from the command line to set up your project. You can learn more about Gradle here:

{{< contentlink "gradle/introduction" >}}

Your directory structure should look like this:


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
    └── test
        └── java
            ├── CatTest.java   <-------- names are important
            └── DogTest.java   <-------- names are important
            ... other logical things
```

You'll be using JUnit to test your code. Make sure you remember to put in the `@Test` tag for all your test methods.

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

Please use `pytest` to test your work.

## Test the existing functionality

Add tests to your project. Make sure you test every method in every class.

Please make sure you test absolutely every function that you wrote in part 1.  Make sure that the different functions do what they are meant to do in all different situations.

Take a bit of time to find out about a concept called "test coverage". WQe want 100% coverage in this project.

## Instructions for reviewers

- There should be no global variables
- If a variable is only used within a given method, then constantly referring to it as `self.variable`/`this.variable` isn't necessary.
- Make sure that there are no redundant tests. For example if there is a test that checks that a dog says "Bark" then it is very pointless to check that the dog does not say "Meow"