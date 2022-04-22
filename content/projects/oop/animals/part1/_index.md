---
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

This challenge should test topics from your OOP knowledge.

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Composition

![Screenshot 2019-11-11 at 10 21 38](https://user-images.githubusercontent.com/47598382/68578218-40542900-047a-11ea-9da8-02ed02d0c798.png)

In this challenge, you will create 3 classes.

1. Super class called `Animal`
2. `Dog` and `Cat` class both **extend** `Animal` class (a dog is an animal, and a cat is an animal).
3. `Dog` and `Cat` class should only have one function, which is their own implementation of the `sounds()` function. This is polymorphism.
4. A `Home` class, but we will talk about that later...

```
// Java

? dog1 = new Dog()
? dog2 = new Dog("Simba")

dog1.eat()    // -> 'Rax eats'
dog1.sound() // -> 'Dog barks'

dog2.eat()    // -> 'Simba eats'
dog2.sound() // -> 'Dog barks'

? cat1 = new Cat()
? cat2 = new Cat("Smokey")

cat1.eat()    // -> 'Stormy eats'
cat1.sound() // -> 'Cat meows'


cat2.eat()    // -> 'Smokey eats'
cat2.sound() // -> 'Cat meows'
```

```
// JavaScript

let dog1 = new Dog();
let dog2 = new Dog("Simba")

dog1.eat();    // -> 'Rax eats'
dog1.sound(); // -> 'Dog barks'

dog2.eat()    // -> 'Simba eats'
dog2.sound() // -> 'Dog barks'

let cat1 = new Cat();
let cat2 = new Cat("Smokey")

cat1.eat();    // -> 'Stormy eats'
cat1.sound(); // -> 'Cat meows'

cat2.eat()    // -> 'Smokey eats'
cat2.sound() // -> 'Cat meows'

```

```
# Python

dog1 = new Dog()
dog2 = new Dog("Simba")

dog1.eat()   # -> 'Rax eats'
dog1.sound() # -> 'Dog barks'

dog2.eat()    # -> 'Simba eats'
dog2.sound() # -> 'Dog barks'

cat1 = new Cat()
cat2 = new Cat("Smokey")


cat1.eat()   # -> 'Stormy eats'
cat1.sound() # -> 'Cat meows'

cat2.eat()    # -> 'Smokey eats'
cat2.sound() # -> 'Cat meows'

```

Now let's add composition. Make a new class called `Home`. Lots of people have dogs and cats in their homes. `Home` should have a function called `adoptPet` that takes any `Animal` as an input and returns the number of pets that have been adopted thus far. The new pet should be stored in the `Home` object in an array/list. The `Home` object should also have a function called `makeAllSounds`. It should work like this:

```
// Java

Home home = new Home()
? dog1 = new Dog()
? dog2 = new Dog()
? cat = new Cat()

home.makeAllSounds() // this doesn't do anything
home.adoptPet(dog1) // 1
home.makeAllSounds()
// this prints:
// Dog barks

home.adoptPet(cat) // 2
home.makeAllSounds()
// this prints:
// Dog barks
// Cat meows

home.adoptPet(dog2) // 3
home.makeAllSounds()
// this prints:
// Dog barks
// Cat meows
// Dog barks
```

```
// JavaScript

let home = new Home();
let dog1 = new Dog();
let dog2 = new Dog();
let cat = new Cat();


home.makeAllSounds();// this doesn't give/return any result/data
home.adoptPet(dog1); // 1
home.makeAllSounds();
// this prints :
// Dog barks

home.adoptPet(cat); // 2
home.makeAllSounds();
// this prints :
// Dog barks
// Cat meows

home.adoptPet(dog2); // 3
home.makeAllSounds();
// this prints :
// Dog barks
// Cat meows
//Dog barks


```
```
# Python

home = Home();
dog1 = Dog();
dog2 = Dog();
cat = Cat();

home.make_all_sounds() # this doesn't give/return any result/data
home.adopt_pet(dog1) # 1
home.make_all_sounds()
# this prints :
# Dog barks

home.adopt_pet(cat) # 2
home.make_all_sounds()
# this prints :
# Dog barks
# Cat meows

home.adopt_pet(dog2) # 3
home.make_all_sounds
# this prints :
# Dog barks
# Cat meows
# Dog barks

```

### Up for a challenge?

This section is not compulsory. If you do this, we will think that you are cool.

Add some functionality to `adoptPet` so that an error/exception, `Cannot adopt the same pet twice!`, gets raised if you try to adopt the same pet twice.

For example,

```
home.adoptPet(dog1) // returns the number of pets that have been adopted thus far
home.adoptPet(dog1) // an error/exception gets raised
```

## Instructions for reviewer
- The Animal class should follow the document's diagram's instructions exactly.
- A constructor that accepts a string to set the name for the constructed pet should exist.
- The `makeAllSounds` method should print the exact strings specified in the instructions. e.g "Dog barks", "Cat meows"
- If the bonus part of the project is attempted; a house cannot adopt a specific instance of a pet more than once.