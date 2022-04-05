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

On Tilde you'll notice that this card is asking for link submission. **Please don't worry about submitting a link**. You will be assessed according to {{% contentlink path="specific-skill-success-criteria/introduction-to-assessments" %}}



All students need to provably understand all of the following concepts:

- how constructors work
- construction of multiple class instances:
 - make many objects of the same class
 - interact with them and see that they are distinct
- getters and setters
- inheritance and overriding and extending methods
- composition

## Python

### Constructors

The constructor is a method that is called when an object is created. This method is defined in the class and can be used to initialize basic variables. In Python the `__init__()` method is called in place of the constructor - to instantiate (initialise) the object.

```
class Rectangle:
  def __init__(self, length, width):
    ...
```

> The learner should know how to create an initialiser that takes in arguments and create instance variables.


### Instantiation

The learner should be able to instantiate the object.

```
rectangle = Rectangle(2,4)
```

The learner should also understand how multiple instances of an object work.

```
small_rectangle1 = Rectangle(2, 4)
small_rectangle2 = Rectangle(2, 4)
medium_rectangle = Rectangle(4, 12)
```

### Inheritance

The learner should know what is inheritance and what it means when a class inherits another class. Both single and multiple inheritances should be understood, and the use of `super()` in both cases.

```
class Square(Rectangle):
  pass

class Cuboid(Rectangle):
  def __init__(self, length, width, height):
      super().__init__(length, width)
      self.height = height
```

### Overriding

The learner should know how to override a function using super and without using super.


## Java

### Constructors

The learner should know that the constructor name must be the same as its class name. 

```
class Rectangle{

    Rectangle(){
      ....
    }    
```
The learner should know that a single class can have multiple constructors with different numbers of parameters. 

```
class Rectangle{
    ....

    // no arg constructor
    Rectangle()
    ....

    // parameterized constructor
    Rectangle(double length, double width)
    ....
```

### Instantiation

The learner should know how to instantiate a class object.

```
  Rectangle rectangle1 = new Rectangle();
  Rectangle rectangle2 = new Rectangle(10.0, 6.0);
  Rectangle rectangle2 = new Rectangle(6.0, 7.0);
```

### Inheritance

The learner must know that to inherit from a class, the keyword extends is used. 

```
class Square extends Rectangle { .... }

class Cuboid extends Rectangle {
  private double length, width, height;
   
  public Cuboid(double length, double width, double height) {
    super(length, width);
    this.length = height;
  }
  ....
}
```

### Overriding

The learner should know that constructors and methods declared with final or static cannot be overridden. If a method cannot be inherited, it cannot be overridden.

