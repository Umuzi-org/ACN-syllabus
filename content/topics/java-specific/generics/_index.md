---
_db_id: 102
content_type: topic
ready: true
title: Java Generics
---

Java generics is a feature that allows you to create "parameterized data types". For example, instead of just declaring a collection that can store any data you can pass it a parameter to allow only the objects of certain data types.

Instead of declaring and instantiating a general collection to store pets like this:

```
  ​ArrayList pets = new ArrayList();
```

you can do it with a parameter so it can store only String objects like this:

```
  ​ArrayList<String> pets = new ArrayList<>();
```

## Advantages of using generics

- Generics ensure compile-time safety which allows the programmer to catch the invalid types while compiling the code.

- Java Generics helps the programmer to reuse the code for whatever type he/she wishes. For instance, a programmer writes a generic method for sorting an array of objects. Generics allow the programmer to use the same method for Integer arrays, Double arrays, and even String arrays.

- Another advantage of using generics is that Individual typecasting isn’t required. The programmer defines the initial type and then lets the code do its job.

- It allows us to implement non-generic algorithms.

## Types of Java Generics

- Generic method: Generic Java method takes a parameter and returns some value after performing a task. It is exactly like a normal function, however, a generic method has type parameters which are reproduced by actual type. This allows the generic method to be used in a more general way. The compiler takes care of the type of safety which enables programmers to code easily since they do not have to perform long, individual type castings.

```
public static <T> int getPets(T[] list, T item) {}
```

- Generic classes: A generic class is implemented exactly like a non-generic class. The only difference is that it contains a type parameter section. There can be more than one type of parameter, separated by a comma. The classes, which accept one or more parameters, ​are known as parametrized classes or parameterized types.

```
class DemoClass<T> {}
```

## Tutorial

Please go through this tutorial to give yourself a better chance to understand the topic

https://howtodoinjava.com/java/generics/complete-java-generics-tutorial/

## Resource

https://www.educative.io/edpresso/what-are-generics-in-java?https://www.educative.io/courses/grokking-the-object-oriented-design-interview?aid=5082902844932096&utm_source=google&utm_medium=cpc&utm_campaign=blog-dynamic&gclid=Cj0KCQiAvc_xBRCYARIsAC5QT9lk7E9OCRYSk5j9kKNwDjsatXCWMIRxr1bGagOKo9jcfk3njeeokRsaAoerEALw_wcB

https://www.tutorialspoint.com/java/java_generics.htm

https://howtodoinjava.com/java/generics/complete-java-generics-tutorial/