---
content_type: topic
ready: true
title: Java Streams
---

Streams are one of the major features introduced in Java 8. Streams are a sequence of elements that can be easily obtained from a `Collection`. Streams should not be confused with File I/O streams which are entirely different.

## The features of Java streams

- A stream is not a data structure. Instead, a stream takes input from the `Collections`, `Arrays`, or `I/O channels`.
- Streams don’t change the original data structure, they only provide the result as per the pipelined methods.
- Each intermediate operation is lazily executed and returns a stream as a result, hence various intermediate operations can be pipelined. Terminal operations mark the end of the stream and return the result.

### We have two types of operations with streams

#### 1. Intermediate Operations

These are operations that result in other streams which means more processing can still be done on them, like:

- **map**: The `map()` method converts `Stream<X>` to `Stream<Y>`. For each object of type `X` a new object of type `Y` is created and put in the new `Stream`.

```
List number = Arrays.asList(2,3,4,5);
List square = number.stream().map(x->x*x).collect(Collectors.toList());
```

- **filter**: The `filter()` method is used to select elements that match the *predicate* that is passed as an argument.

```
List names = Arrays.asList("Reflection","Collection","Stream");
List result = names.stream().filter(s->s.startsWith("S")).collect(Collectors.toList());
```

- **sorted**: The `sorted()` method is used to sort the stream.

```
List names = Arrays.asList("Reflection","Collection","Stream");
List result = names.stream().sorted().collect(Collectors.toList());
```

#### 2. Terminal Operations

These are operations that result in a final value that marks the stream as consumed and no further processing can be done.

- **collect**: The `collect()` method is used to receive elements from stream and store them in a collection.

```
List number = Arrays.asList(2,3,4,5,3);
Set square = number.stream().map(x->x*x).collect(Collectors.toSet());
```

- **forEach**: The `forEach()` method helps iterate over all stream elements and perform some operation on each of them. The operation to be performed is passed as the lambda expression.

```
List number = Arrays.asList(2,3,4,5);
number.stream().map(x->x*x).forEach(y->System.out.println(y));
```

- **reduce**: The `reduce()` method performs a reduction on the elements of the stream with the given function. The result is an Optional holding the reduced value.

```
List number = Arrays.asList(2,3,4,5);
int even = number.stream().filter(x->x%2==0).reduce(0,(ans,i)-> ans+i);
```

#### Resources
- [Stackify](https://stackify.com/streams-guide-java-8/)
- [GeeksForGeeks](https://www.geeksforgeeks.org/stream-in-java/)
