---
_db_id: 203
available_flavours:
- java
content_type: project
prerequisites:
  hard:
  - projects/java-specific/data-structures
  - topics/java-specific/generics
  soft: []
ready: true
submission_type: repo
title: Java Generics
---

## Generic method

Generic Java method takes a parameter and returns some value after performing a task. It is exactly like a normal function, however, a generic method has type parameters which are reproduced by actual type. This allows the generic method to be used in a more general way. The compiler takes care of the type of safety which enables programmers to code easily since they do not have to perform long, individual type castings.

**Example**

```
public static <T> int getPets(T[] list, T item) {}
```

Fun Time!!

You have two arrays,
First array is of type Integers

```
12
324
6
7900
```

Second array is of type String

Please write a single function called:

```
printArrayContent(array);
```

This function should accept one parameter and be able to accept an integer array or string array and print out the contents of that array.

**Notes: If you use method overload the answer wont be accepted**

## Generic classes:

A generic class is implemented exactly like a non-generic class. The only difference is that it contains a type parameter section. There can be more than one type of parameter, separated by a comma. The classes, which accept one or more parameters, ​are known as parametrized classes or parameterized types.

Create a class called GenericClass that is able to set and get a private single variable which can either be String or Integer

```
stringInstance = new GenericClass<?>();
stringInstance.set("Test");

stringInstance.get() // print out Test

integerInstance = new GenericClass<?>();
integerInstance.set(1000);

integerInstance.get() // print out 1000

```