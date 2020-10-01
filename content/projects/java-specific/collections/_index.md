---
_db_id: 211
available_flavours:
- java
content_type: project
prerequisites:
  hard:
  - projects/oop/animals
  - topics/java-specific/collections-and-datastructures
  soft:
  - topics/intro-to-docker
  - topics/java-specific/intro-to-gradle-with-intellij
  - projects/oop/dice
  - projects/oop/person
ready: true
submission_type: repo
title: Java collections
---

This project assumes you have gone through the reading for both data structures as well as collection, but for a quick recap for the purpose of this project:

Java has a collection framework that gives us a list of classes which help us efficiently deal with objects, one of these is called a dequeue/deque(double-ended queue). A deque is magical because it allows us to add or remove anything from either the front(head) or back(tail) of the queue.

You can implement a Deque by using either a LinkedList of an ArrayDeque class. For example

```
Deque queue = new LinkedList<>();
or
Deque queue = new ArrayDeque<>();
```

**Now for the FUN part... Project time**

```
intNumber = 9 // Number of integer in the set
subArraySize = 3 // Size of the subArray to consider
queue = 6 2 6 8 3 7 1 4 4 // integer sample
```

You have to print out the maximum number of unique integers among all possible adjacent subarrays of size **subArraySize**

Example of the project

**Input**

```
intNumber = 9
subArraySize = 3
queue = 6 2 6 8 3 7 1 4 4
```

**Output**

3

**Explanation**

```
r1 => (6 2 6) = Has 2 unique numbers

r2 => (2 6 8) = Has 3 unique numbers

r3 => (6 8 3) = Has 3 unique numbers

r4 => (8 3 7) = Has 3 unique numbers

r5 => (3 7 1) = Has 3 unique numbers

r6 => (7 1 4) = Has 3 unique numbers

r7 => (1 4 4) = Has 2 unique numbers
```

So the highest number of unique integer in a subArray is **3**

If your code is correct it should return these outputs for these inputs

**Input #1**

```
intNumber = 8
subArraySize = 4
queue = 2 2 2 2 2 2 2 2
```

**Output**

```
1
```

**Input #2**

```
intNumber = 10
subArraySize = 3
queue = 7 5 5 7 5 5 7 5 5 6
```

**Output**

```
 2
```

**HAVE FUN!!**