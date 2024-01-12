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
- skill/oop
title: Animals Part 2. Adding Tests
---

In this project you'll be testing some of your previous work.

## Project structure

### Java


Your directory structure should look like this:


```
├── app
│   ├── build.gradle
│   └── src
│       ├── main
│       |   └── java
│       |       └── animals
│       |           └── Animals.java <-------- names are important
│       |           └── Cat.java <-------- names are important
│       |           └── Dog.java <-------- names are important
│       |           └── Home.java <-------- names are important
│       └── test
│           └── java
│               └── animals
│                   └── ???.java
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
└── settings.gradle             
```

You'll be using JUnit to test your code. Make sure you remember to put in the `@Test` tag for all your test methods.

### JavaScript

Your directory structure should look like this:

```
├── spec
|   ├── support
|   |   └── jasmine.json
|   └── ???
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
  └── ???

```

Please use `pytest` to test your work.

## Test the existing functionality

Add tests to your project. Make sure you test every method in every class.

Please make sure you test absolutely every function that you wrote in part 1.  Make sure that the different functions do what they are meant to do in all different situations.

Take a bit of time to find out about a concept called "test coverage". We want 100% coverage in this project.

## Instructions for reviewers

Make sure that there are no redundant tests. For example if there is a test that checks that a dog says "Bark" then it is very pointless to check that the dog does not say "Meow", "caterpillar" or "whatzit", because we already know that it says "Bark".