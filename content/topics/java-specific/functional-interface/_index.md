---
content_type: topic
ready: true
tags:
- functions
title: Java Lambda expressions and Functional Interface
---


#### What are Lambda expressions:

Introduced in Java 8 Lambda expressions are anonymous (don't have names) shortcode blocks that can take parameters and return a value just like methods.

#### What are Functional Interface

Functional Interface in Java is also called Single Abstract Method (SAM) interface. They can have many default and static methods but only one abstract method that is why they are also called Single Abstract Method (SAM) interface. The make it possible to create abstractions that multiple classes can use without copying and pasting code. This is especially helpful when developers need to create a complex abstraction with various methods and behaviors.


All together Functional interface with lambda expressions help us to write smaller and cleaner code by removing a lot of boiler-plate code.


#### Functional Interface have four types

![functional-interface](function-interface.png)

read more about them [here](https://www.geeksforgeeks.org/functional-interfaces-java/#:~:text=Java%20SE%208%20included%20four%20main%20kinds%20of%20functional%20interfaces%20which%20can%20be%20applied%20in)

- Examples of built in functional interface like **Runnable()**
```
// create anonymous inner class object
new Thread(new Runnable() {
    @Override public void run()
    {
        System.out.println("New thread created");
    }
}).start();

```

- Using lambda expressions to re-write the code above

```
// lambda expression to create the object
new Thread(() -> {
    System.out.println("New thread created");
}).start();
```


#### Custom functional interface

```
@FunctionalInterface  
  interface Dog{  
      void sound(String message);  
  }

  public class DogImplementation implements Dog{  
      public void sound(String message){  
          System.out.println("Dog " + message);  
      }  
      public static void main(String[] args) {  
          DogImplementation obj = new DogImplementation();  
          obj.sound("Bark!");
      }  
  }
```


### Recourses
- https://www.geeksforgeeks.org/functional-interfaces-java/
- https://www.javatpoint.com/java-8-functional-interfaces
- https://www.baeldung.com/java-8-functional-interfaces


