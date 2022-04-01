---
_db_id: 711
content_type: project
flavours:
- any_language
ready: true
submission_type: link
tags:
- technical-assessment
title: 'Assessment: Classes and objects'
---

## Note about submission format

On Tilde you'll notice that this card is asking for a link submission. **Please don't worry about submitting a link**. You will be assessed according to {{% contentlink path="specific-skill-success-criteria/introduction-to-assessments" %}}

## Python

### Constructors

The constructor is a method that is called when an object is created. This method is defined in the class and can be used to initialize basic variables. In Python the `__init__()` method is called in place of the constructor - to instantiate (initialise) the object.

```
class Rectangle:
  def __init__(self, length, width):
    ...
```

> Learner should know how to create an initialiser that takes in arguments and create instance variables.


### Instantiation

Learner should be able to instantiate the object.

```
rectangle = Rectangle(2,4)
```

Learner should also understand how multiple instances of an object work.

```
small_rectangle1 = Rectangle(2, 4)
small_rectangle2 = Rectangle(2, 4)
medium_rectangle = Rectangle(4, 12)
```

### Inheritance

Learner should know what is inheritance and what it means when a class inherits another class. Both single and multiple inheritance should be understood, and the use of `super()` in both cases.

```
class Square(Rectangle):
  pass

class Cuboid(Rectangle):
  def __init__(self, length, width, height):
      super().__init__(length, width)
      self.height = height
```

### Overriding

Learner should know how to override a function using super and without using super.

## Javascript

### Constructors

Learner should know how constructors work

```
class Rectangle {
  constructor(length, width){
    this.length = length
    this.width = width
  }
}
```
### Instantiation

Learner should know how to instantiate many objects from the same class and interact with them

```
const smallRectangle1 = new Rectangle(2, 4)
const smallRectangle2 = new Rectangle(2, 4)
const mediumRectangle = new Rectangle(4, 12)


console.log(smallRectangle1.length) //2
console.log(mediumRectangle.width) //12

```
### Private members

Learner should know how to modify and access private members of a class

```
class Car {

    _length

    constructor(length, width){
      this._length = length
      ...
    }

    set length(newLength){ //setter
        this._length = newLength
    }

    get length(){ //getter
        return this._length
    }
}

```
### Inheritance and overriding

Learner should understand inheritance and overriding and extending methods
```
class Rectangle {
  ...
  details(){
    console.log(`length: ${this.length}, width: ${this.width}`)
  }
}

class Cuboid extends Rectangle {
  constructor(length, width){
    super();
  };
  details(){
    return `length: ${this.length}, width: ${this.width}`;
  };
};

```

