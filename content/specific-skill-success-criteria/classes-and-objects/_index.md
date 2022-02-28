---
_db_id: 711
content_type: project
ready: true
flavours:
- any_language
submission_type: link
title: 'Assessment: Classes and objects'
---

## Note about submission format

On Tilde you'll notice that this card is asking for a link submission. **Please don't worry about submitting a link**. You will be assessed according to {{% contentlink path="specific-skill-success-criteria/introduction-to-assessments" %}}



All students need to probably understand all of the following concepts:

- how constructors work
- construction of multiple class instances:
  - make many objects of the same class
  - interact with them and see that they are distinct
- getters and setters
- inheritance and overriding and extending methods
- composition

# Python

## Constructors
The constructor is a method that is called when an object is created. This method is defined in the class and can be used to initialize basic variables. In Python the `__init__()` method is called in place of the constructor - to instantiate (initialise) the object.
```
class Shape:
  def __init__(self):
    pass
```
> Learner should also know how to create an initialiser that takes in arguments.


## Instantiation
Instantiating a class is creating a copy of the class which inherits all class variables and methods. We simply call the class as if it were a function, passing the arguments that the `__init__()` method defines (except `self`).
Here we are going to have a look at a Rectangle object that takes in the `length` and the `width`, respectively:
```
rectangle = Rectangle(2,4)
```

An object can have multiple instances, meaning that each instance has its own different attribute values
```
rectangle_small = Rectangle(2,4)
rectangle_medium = Rectangle(4,12)
rectangle_big = Rectangle(8,24)
```


## Getters and setters
The main purpose that getters and setters serve in object-orientated programs is for ensuring data encapsulation - or put another way, as a mechanism for hiding the implementation details of a class from the user. In Python, getters and setters are not the same as for other object-orientated languages. Private variables in Python are not actually hidden fields. In Python getters and setters are typically used when:

- we want to add validation logic for getting and setting a value
- to avoid the direct access of a class field so that private variables cannot be accessed directly/modified by an outside user


## Inheritance
Inheritance enables us to create a new class from an existing class. The new class (child class) is a specialized version of the existing class (parent class) and it inherits all the non-private variables and methods of the existing class.

If no additional instance variable(s) are required in the child class, `__init__()` can be left out.
```
class Square(Rectangle):
  pass
```

If additional instance variable(s) are required in the child class, `super()` (see below) is one of the methods that can be used.
```
class Cuboid(Rectangle):
  def __init__(self, length, width, height):
      super().__init__(length, width)
      self.height = height
```


### super()
In a child class, a parent class can be referenced by using the `super()` function. This super function returns a temporary object/instance of the superclass (parent class) that gives access to all its methods to its child class. There's no need to specify the parent class name to access its methods. This function can be used both in single and multiple inheritances.
```
class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width


class Square(Rectangle):
  def __init__(self, length):
    super().__init__(length, length)
```

Here, `super()` is used to call the `__init__()` of the Rectangle class, allowing you to use it in the Square class without repeating code. Below, the core functionality remains after making changes:
```
square = Square(4)
print(square.area()) # 16
```

Another example:
```
class Cuboid(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def area(self):
        return super().area() * self.height
```

## Overriding
If a child class defines a method with the same name as a method in the parent class, the child class method will override the parent class method, thus the child class method will be implemented, unless `super` is used.
Using the Cuboid object above if super is not used:
```
  def area(self):
    return self.length * self.width * self.height
```
