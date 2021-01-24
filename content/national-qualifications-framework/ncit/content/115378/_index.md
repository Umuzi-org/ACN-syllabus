---
_db_id: 358
content_type: topic
nqf: ncit
ready: false
tags:
- oop
title: Object-Oriented Programming
unit_standards:
- 115378
---

## 1. OOP theory and practice

Object-oriented programming is one of the most powerful design philosophies in all of software development. It is a conceptual framework (sometimes called a paradigm) that you can use in many different programming languages and on many different projects. At the most introductory level, OOP consists of 4 key concepts:


 - Encapsulation

 - Abstraction

 - Inheritance

 - Polymorphism


These sound like very technical and difficult concepts, but as this video will show, they are relatively straightforward to understand and use.


Watch this video: [OOP in 7 minutes](https://youtu.be/pTB0EiLXUC8)

After you’ve learned the basic concepts of what Object-Oriented Programming is, there are countless things you can practice. First read through [this tutorial](https://scotch.io/tutorials/object-oriented-programming-in-javascript) to learn more about building objects from other objects. In other languages those “object templates” are called classes. That 2015 update to JavaScript (ES6) includes a [“class” keyword](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes). You may find it easiest to use the class keyword when you are building OOP programs. However, as you will discover, the same functionality can be coded in many different ways in JavaScript.

Read this this tutorial before moving on and start to practice these concepts:

https://scotch.io/tutorials/object-oriented-programming-in-javascript

[Intro video covering similar concepts (optional)](https://youtu.be/rlLuL3jYLvA)

If you are looking to get more practice, this video tutorial covers all of the basics of OOP and JavaScript prototypes. Remember, the most important thing is to start practicing these methods. You could watch hours of videos about this topic, but you won’t really learn anything until you start to apply it in your own code.

Also watch: [What is Object-oriented Programming](https://youtu.be/PFmuCDHHpwk)

## 2. Definitions

**Abstraction**

Abstraction is the process of hiding all but the relevant information about a thing to make things less complex and more efficient for the user. For example, we don’t need to know how a clock works in order to use it to tell time. Abstraction lets you focus on what the thing does instead of how it does it.


**Encapsulation**

The combining together of properties (data/attributes) and methods (behaviour/processes) into a single abstract data type with a public interface and a private implementation. This allows the implementation to be altered without affecting the interface.


**Inheritance**

The derivation of one class from another so that the attributes and methods of one class are part of the definition of another class. The first class is often referred to the base or parent class. The child is often referred to as a derived or sub-class.

Derived classes are always ‘a kind of’ their base classes. Derived classes generally add to the attributes and/or behaviour of the base class. Inheritance is one form of object-oriented code reuse.

E.g. Both Motorbikes and Cars are kinds of MotorVehicles and therefore share some common attributes and behaviour but may add their own that are unique to that particular type.


**Object**

An instance of a class. Objects have state, identity and behaviour.


**Polymorphism**

Literally, “many forms”. Generally, the ability of different classes of object to respond to the same message in different, class-specific ways. Polymorphic methods are those which might have the same name, but but different implementations. For example, a subclass (child class) might override a parent class's method and implement it in a different way.

*E.g. Both the Plane and Car types might be able to respond to a turnLeft message. While the behaviour is the same, the means of achieving it are specific to each type.*

## 3. Abstract classes and wrappers


## Abstract classes

When you’re developing a program with many similar parts, it takes way too much time and effort to keep duplicating code for each class. Imagine how hard it would be to maintain a large project with thousands of classes! Besides, it violates the **DRY** principle of good programming: **Don’t Repeat Yourself!** There must be a better way.


Thankfully, there are many design patterns that allow you to share code between classes. One of these is called an “abstract class”. (Unfortunately, JavaScript doesn’t have native support for the concept of “abstract classes”, but it is still possible to implement as you will see below.) In languages like C# and Java, you simply create a new class with the keyword “abstract” (e.g. “public abstract class Mammal”) and write in its body all the methods you would like your other classes to share in common. Since an abstract class is still a class, your “Cat” and “Dog” classes can inherit from it. This means that instead of writing a “sleep” method for each animal, you only need to write it in the “Mammal” class, and the other animals will be able to use it too.


But if any class can have inheritance, why not just use a regular class? The answer is that abstract classes have two special features:

**1. They cannot be instantiated** (made into objects),

**2. They can have special methods called “abstract methods”.**


“Wait a minute,” you may be thinking, “Why would I want a class that can’t become an object?!” Sounds useless, right? However, **consider the purpose of an abstract class:** it contains common methods (and properties) that multiple child classes inherit from, but it does not attempt to follow these directions itself. In fact, a parent class is often missing vital information about the methods and fields it contains, because each child may use them a little bit differently. The “Mammal” abstract class only has what is common to all mammals — since some mammals can’t crawl and other mammals can’t gallop, the “Mammal” class can’t do either one. Imagine what would happen if you tried to instantiate a “generic” mammal: you’d get a featureless mass of hair, muscle and bone that probably wouldn’t survive on its own! In the same way, it is undesirable (sometimes dangerous!) to leave a class open to instantiation when it is simply a placeholder for common features. Guard against this possibility by using an abstract class.

Abstract classes can be very useful in more complicated programs. You have to be clever about how you implement them. Look at the examples below, or at this link (easier to view in the link)

________

If you would like a class that cannot be constructed, but whose subclasses can, then you can use new.target:

```
class Abstract {
constructor() {
if (new.target === Abstract) {
throw new TypeError("Cannot construct Abstract instances directly"); }
}
}
class Derived extends Abstract {
constructor() {
super(); // more Derived-specific stuff here, maybe
}
}
const a = new Abstract(); // new.target is Abstract, so it throws

const b = new Derived(); // new.target is Derived, so no error
```


For more details on new.target, you may want to read this general overview of how classes in ES2015 work: http://www.2ality.com/2015/02/es6-classes-final.html

If you're specifically looking for requiring certain methods be implemented, you can check that in the superclass constructor as well:

```
class Abstract {
constructor() {
if (this.method === undefined) { // or maybe test typeof this.method === "function"
throw new TypeError("Must override method"); }
}
}
class Derived1 extends Abstract {}
class Derived2 extends Abstract { method() {} }
const a = new Abstract(); // this.method is undefined; error
const b = new Derived1(); // this.method is undefined; error
const c = new Derived2(); // this.method is Derived2.prototype.method; no error
```

_____

Abstract classes help you improve your code not only through what they can do, but also through what they can’t. They can hold common features for many classes to inherit, without accidentally becoming objects themselves. They can also force you to write unique implementations of a common method, preventing human errors of forgetfulness. When you set up a class hierarchy, seriously consider whether you need a normal class to inherit from, or whether an abstract class will do. It may end up making the difference between a solid or buggy program.



### Wrapper classes


**Wrapper classes** are a topic you won’t come across much in JavaScript. In other languages, like C# and Java, they have methods to turn primitive data types (int, float, string, etc) into objects. Wrapper classes are used to convert any data type into an object.


A wrapper class wraps (encloses) around a data type and gives it an object appearance. Wherever, the data type is required as an object, this object can be used. Wrapper classes include methods to unwrap the object and give back the data type. It can be compared with a chocolate. The manufacturer wraps the chocolate with some foil or paper to prevent from pollution. The user takes the chocolate, removes and throws the wrapper and eats it.


In JavaScript, nearly everything is an object, which means you can assign properties and methods to nearly everything. However if you try to assign a property to a String, you’ll get “undefined”. By reading the short article below, you can learn more about the quirks of JavaScript and how it wraps its primitive data types as objects temporarily.

**http://adripofjavascript.com/blog/drips/javascripts-primitive-wrapper-objects.html**

## 4. Design patterns

Design patterns are reusable solutions to commonly occurring problems in software design. They are both exciting and a fascinating topic to explore in any programming language.


One reason for this is that they help us build upon the combined experience of many developers that came before us and ensure we structure our code in an optimized way, meeting the needs of problems we're attempting to solve.


Design patterns also provide us a common vocabulary to describe solutions. This can be significantly simpler than describing syntax and semantics when we're attempting to convey a way of structuring a solution in code form to others.


[This book](https://addyosmani.com/resources/essentialjsdesignpatterns/book/) is a wonderful resource on design patterns in JavaScript. It’s worth bookmarking so you can revisit it as needed. For now, you must read the following sections. The first 2 provide an intro to design patterns. The following 3 give examples of common design patterns you will use in your code:


https://addyosmani.com/resources/essentialjsdesignpatterns/book/#categoriesofdesignpatterns

https://addyosmani.com/resources/essentialjsdesignpatterns/book/#summarytabledesignpatterns

https://addyosmani.com/resources/essentialjsdesignpatterns/book/#constructorpatternjavascript

https://addyosmani.com/resources/essentialjsdesignpatterns/book/#singletonpatternjavascript

https://addyosmani.com/resources/essentialjsdesignpatterns/book/#factorypatternjavascript