---
_db_id: 293
content_type: topic
prerequisites:
  hard:
  - topics/kotlin/basic-control-flow
  soft: []
ready: true
title: Classes
---

Classes in Kotlin are declared using the keyword class:

````
class Invoice {
    }
````

### Constructors
A class in Kotlin can have a primary constructor and one or more secondary constructors.


````
class Person constructor(firstName: String) {
    }

````

### Secondary Constructors
The class can also declare secondary constructors, which are prefixed with constructor:

````
class Person {
    constructor(parent: Person) {
    parent.children.add(this)
    }
    }
````

### Creating instances of classes
To create an instance of a class, we call the constructor as if it were a regular function:
````
 val invoice = Invoice()

    val customer = Customer("Joe Smith")
````

Note: that Kotlin does not have a new keyword.

### Inheritance
All classes in Kotlin have a common superclass Any, that is a default super for a class with no supertypes declared:


````
 class Example // Implicitly inherits from Any
Any is not java.lang.Object; in particular, it does not have any members other than equals(), hashCode() and toString().
````

To declare an explicit supertype, we place the type after a colon in the class header:

````
open class Base(p: Int)

    class Derived(p: Int) : Base(p)
````

### Overriding Methods
Kotlin requires explicit annotations for overridable members (we call them open) and for overrides:

````
open class Base {
    open fun v() {}
    fun nv() {}
    }
    class Derived() : Base() {
    override fun v() {}
    }

````

The override annotation is required for Derived.v(). If it were missing, the compiler would complain.


### Abstract Classes
A class and some of its members may be declared abstract. An abstract member does not have an implementation in its class.

We can override a non-abstract open member with an abstract one

````
open class Base {
    open fun f() {}
    }

     abstract class Derived : Base() {
    override abstract fun f()
    }
````