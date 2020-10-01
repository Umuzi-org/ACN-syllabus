---
_db_id: 224
available_flavours:
- any_language
content_type: project
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

This Challenge should test topics from your OOP knowledge

1. Encapsulation
2. Inheritance
3. Polymophism
4. Composition

![Screenshot 2019-11-11 at 10 21 38](https://user-images.githubusercontent.com/47598382/68578218-40542900-047a-11ea-9da8-02ed02d0c798.png)

In this challenge you will create 3 classes

1. Super class called `Animal`
2. `Dog` and `Cat` class which both **extends** `Animal` class (a dog is an animal and a cat is an animal)
3. `Dog` and `Cat` class should only have 1 function, which is their own implementation of the `sound()` function. This is polymorphism
4. a `Home` class. But we'll talk about that later...

```
// Java

? dog = new Dog()

dog.eat()    // -> 'Rax eats'
dog.sounds() // -> 'Dog barks'

? cat = new Cat()

cat.eat()    // -> 'Stormy eats'
cat.sounds() // -> 'Cat meows'
```

```
// Javascript

var dog = new Dog();

dog.eat(); // -> 'Rax eat'
dog.sounds();// -> 'Dog barks'

var cat = new Cat();

cat.eat();// -> 'Stormy eats'
cat.sounds();// -> 'Cat meows'

```

Now let's add composition. Make a new class called `Home`. Lots of people have dogs and cats in their homes. `Home` should have a function called `adoptPet` that takes any `Animal` as an input. The new pet should be stored in the `Home` object in an array/list. The `Home` object should also have a function called `makeAllSounds`. It should work like this:

```
// Java

Home home = new Home()
? dog1 = new Dog()
? dog2 = new Dog()
? cat = new Cat()

home.makeAllSounds() // this doesn't do anything
home.adoptPet(dog1)
home.makeAllSounds()
// this prints:
// Dog barks

home.adoptPet(cat)
home.makeAllSounds()
// this prints:
// Dog barks
// Cat meows

home.adoptPet(dog2)
home.makeAllSounds()
// this prints:
// Dog barks
// Cat meows
// Dog barks
```

```
// Javascript

var home = new Home();
var dog1 = new Dog();
var dog2 = new Dog();
var cat = new Cat();


home.makeAllSounds();// this doesn't give/return any result/data
home.adoptPet(dog1);
home.makeAllSounds();
// this prints :
// Dog barks

home.adoptPet(cat);
home.makeAllSounds();
// this prints :
// Dog barks
// Cat meows

home.adoptPet(dog2);
home.makeAllSounds();
// this prints :
// Dog barks
// Cat meows
//Dog barks


```

### Up for a Challenge?

This section is not compulsory. If you do this we'll think you're cool.

Add some functionality to `adoptPet` so that an error/exception gets raised if you try to adoptThe same pet twice

eg:

```
home.adoptPet(dog1) // totally ok
home.adoptPet(dog1) // not ok at all
```