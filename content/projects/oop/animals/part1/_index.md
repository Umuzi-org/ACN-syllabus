![image](https://github.com/Umuzi-org/ACN-syllabus/assets/37469171/ada6eb0c-7bca-4506-88e3-158a9778cc6d)---
_db_id: 224
content_type: project
flavours:
- any_language
learning_outcomes:
- code_oop_class_instantiation
- code_oop_polymorphism
- code_oop_encapsulation
- code_oop_inheritance
- code_oop_composition
prerequisites:
  hard:
  - projects/oop/person
  soft: []
ready: true
story_points: 3
submission_type: repo
tags:
- oop
title: Animals Part 1. OOP basics
---

## Project structure

### JavaScript

Your directory structure should look like this:

```
├── src
|   └── animals.js
└── package.json
```

**Note**: Please export your `Dog`, `Cat` and `Home` classes using the following syntax at the end of the code:

```

module.exports = {class1Name, class2Name, ...}

```

### Python

Your directory structure should look like this:

```
├── animals
│   └── animals.py
├── setup.py
├── requirements.txt
├── .gitignore
```

### Java

Your directory structure should look like this:

```
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    ├── main
       └── java
           ├── Animal.java       <-------- names are important
           ├── Cat.java          <-------- names are important
           ├── Dog.java          <-------- names are important
           ├── Home.java         <-------- names are important
           └── MainProgram.java  <-------- names are important
```

Please refer to the following to find out more: {{< contentlink path="topics/java-specific/project-submission-requirements" >}}

## Instructions

This challenge should test topics from your OOP knowledge.

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Composition

![Animal Flow Diagram](animals-diagram.png)

In this challenge, you will create 3 classes.

1. Super class called `Animal`
2. `Dog` and `Cat` class both **extend** `Animal` class (a dog is an animal, and a cat is an animal).
3. `Dog` and `Cat` class should only have one function, which is their own implementation of the `sound()` function. This is polymorphism.
4. A `Home` class, but we will talk about that later...

```
// Java

? dog1 = new Dog()
? dog2 = new Dog("Simba")

dog1.eat()    // returns 'Rax eats'
dog1.sound() // returns 'Bark'

dog2.eat()    // returns 'Simba eats'
dog2.sound() // returns 'Bark'

? cat1 = new Cat()
? cat2 = new Cat("Smokey")

cat1.eat()    // returns 'Stormy eats'
cat1.sound() // returns 'Meow'

cat2.eat()    // returns 'Smokey eats'
cat2.sound() // returns 'Meow'
```

```
// JavaScript

let dog1 = new Dog();
let dog2 = new Dog("Simba")

dog1.eat();    // returns 'Rax eats'
dog1.sound(); // returns 'Bark'

dog2.eat()    // returns 'Simba eats'
dog2.sound() // returns 'Bark'

let cat1 = new Cat();
let cat2 = new Cat("Smokey")

cat1.eat();    // returns 'Stormy eats'
cat1.sound(); // returns 'Meow'

cat2.eat()    // returns 'Smokey eats'
cat2.sound() // returns 'Meow'

```

```

# Python

dog1 = Dog()
dog2 = Dog('Simba')

dog1.eat()   # returns 'Rax eats'
dog1.sound() # returns 'Bark'

dog2.eat()    # returns 'Simba eats'
dog2.sound() # returns 'Bark'

cat1 = Cat()
cat2 = Cat('Smokey')

cat1.eat()   # returns 'Stormy eats'
cat1.sound() # returns 'Meow'

cat2.eat()    # returns 'Smokey eats'
cat2.sound() # returns 'Meow'

```

Now let's add composition. Make a new class called `Home`. Lots of people have dogs and cats in their homes. `Home` should have a function called `adoptPet` that takes any `Animal` as an input and returns the number of pets that have been adopted thus far. The new pet should be stored in the `Home` object in an array/list. The `Home` object should also have a function called `makeAllSounds`. It should work like this:

```
// Java

Home home = new Home()
? dog1 = new Dog()
? dog2 = new Dog()
? cat = new Cat()

home.makeAllSounds() // this doesn't return anything
home.adoptPet(dog1) // 1
home.makeAllSounds()
// this returns:
// ["Bark"]

home.adoptPet(cat) // 2
home.makeAllSounds()
// this returns:
// ["Bark", "Meow"]

home.adoptPet(dog2) // 3
home.makeAllSounds()
// this returns:
// ["Bark", "Meow", "Bark"]


```

```
// JavaScript

let home = new Home();
let dog1 = new Dog();
let dog2 = new Dog();
let cat = new Cat();


home.makeAllSounds();// this doesn't return anything
home.adoptPet(dog1); // 1
home.makeAllSounds();
// this returns:
// ["Bark"]

home.adoptPet(cat); // 2
home.makeAllSounds();
// this returns:
// ["Bark", "Meow"]

home.adoptPet(dog2); // 3
home.makeAllSounds();
// this returns:
// ["Bark", "Meow", "Bark"]
```

```
# Python

home = Home()
dog1 = Dog()
dog2 = Dog()
cat = Cat()

home.make_all_sounds() # this doesn't return anything
home.adopt_pet(dog1) # 1
home.make_all_sounds()
# this returns:
# ["Bark"]


home.adopt_pet(cat) # 2
home.make_all_sounds()
# this returns:
# ["Bark", "Meow"]

home.adopt_pet(dog2) # 3
home.make_all_sounds
# this returns:
# ["Bark", "Meow", "Bark"]
```

Add some functionality to `adoptPet` so that the error/exception, `Cannot adopt the same pet twice!`, gets raised if you try to adopt the same pet twice.

For example,

```
home.adoptPet(dog1) // returns the number of pets that have been adopted thus far
home.adoptPet(dog1) // an error/exception gets raised
```

## Instructions for reviewer

- The Animal class should follow the document's diagram's instructions exactly.
- A constructor that accepts a string to set the name for the constructed pet should exist.
- The `makeAllSounds` method should return an array of the exact strings specified in the instructions. e.g "Bark", "Meow"
- All the class methods should return the exact strings defined and not print them.
- A house cannot adopt a specific instance of a pet more than once.
- The correct error/exception, `Cannot adopt the same pet twice!`, should be raised/thrown.
