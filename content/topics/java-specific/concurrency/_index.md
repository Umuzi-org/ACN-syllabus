---
content_type: topic
ready: true
tags:
- threads
- concurrency
title: Java Multithread, Concurrency and Parallelism
---

You may have heard about Java being multi-threaded - but what does that mean exactly?

A thread is like a separate CPU executing your application. Thus, a multithreaded application is like an application that has multiple CPUs executing different parts of the code at the same time. Multi-threaded applications have multiple threads so they can be much faster than single-threaded applications.

A thread goes through a life-cycle which can be seen in the diagram below:

...

## What is Multithreading

Multithreading means that you have multiple threads of execution inside the same application. A thread is like a separate CPU executing your application. Thus, a multithreaded application is like an application that has multiple CPUs executing different parts of the code at the same time. 

***A thread goes through a life-cycle which can be seen in the diagram below***

![thread-life-cycle](Thread_Life_Cycle.jpg)

### How to create a Thread

Java can handle multiple threads, but you need to do a bit of work to set it up. This is because you, as the programmer, need to decide what each thread should be responsible for.

```
// Thread definition used here where Runnable is a functional interface
Thread(Runnable r)

// so to create a new thread you would do it like this
class Test {
    public static void main(String args[]) {
        // lambda expression to create the object
        new Thread(() -> {
            System.out.println("New thread created");
        }).start();
    }
}

```

## What is Concurrency

Concurrency actually means that multiple tasks can be executed in an overlapping time period. This means that one of the tasks can begin before the preceding one is completed; however, they won’t be running at the same time. The CPU will adjust time slices per task and appropriately switch contexts. That’s why this concept is quite complicated to implement and especially debug.

There are a lot of components/utilities in the concurrency package, one of the commonly used ones is `Executor`.

The Executor interface represents an object that executes tasks. Depending on the implementation, the task can be run on either a new thread or the current thread. This `decoupling` of the task execution flow from the execution mechanism allows for greater flexibility and control.

```
public interface Executor {
    void execute( Runnable command );
}
```

Since Executor is an interface, we can't just create instances. We need to implement the Executor interface. We do this by creating an `Invoker` class like so:

```
public class Invoker implements Executor {
   @Override
   public void execute(Runnable r) {
       r.run();
   }
}
```

Now, for the execution of the task, we can use this invoker:

```
public void execute() {
   Executor exe = new Invoker();
   exe.execute( () -> {
       // task to be performed
   });
}
```

Explore Java documentation and official Java tutorials provided by Oracle. The [Java Concurrency tutorial](https://docs.oracle.com/javase/tutorial/essential/concurrency/), in particular, covers the Executor framework and provides detailed explanations and examples.

## What is Parallelism

Parallelism is the ability to execute independent tasks of a program in the same instant of time. Contrary to concurrent tasks, these tasks can run simultaneously on another processor core, another processor, or an entirely different computer that can be a distributed system. As the demand for computing speed from real-world applications increases, parallelism becomes more common and affordable.

![concurnecy-vs-parallelism](con-vs-par.webp)

#### Extra Resources

- https://www.baeldung.com/cs/concurrency-vs-parallelism
- https://www.geeksforgeeks.org/java-util-concurrent-package/
- https://www.geeksforgeeks.org/java-util-concurrent-package/
- https://www.tutorialspoint.com/java_concurrency/concurrency_overview.htm
- https://www.tutorialspoint.com/java_concurrency/concurrency_major_operations.htm
- https://www.tutorialspoint.com/java_concurrency/concurrency_deadlock.htm
- https://deadlockempire.github.io/#menu - this one is fun
