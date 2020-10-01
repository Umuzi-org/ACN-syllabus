---
_db_id: 301
content_type: topic
prerequisites:
  hard:
  - topics/kotlin/properties-and-fields
  soft: []
ready: true
title: Interface
---

### Interfaces in Kotlin are very similar to Java 8.

An interface is defined using the keyword interface
````
interface MyInterface {
    fun bar()
    fun foo() {
    // optional body
    }
    }
````
### Implementing Interfaces
A class or object can implement one or more interfaces
````
class Child : MyInterface {
    override fun bar() {
    // body
    }
    }
````