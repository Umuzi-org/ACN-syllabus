---
_db_id: 
content_type: topic
ready: true
title: Java streams
---

Streams are one of the major features introduced in java 8, what do they do you ask, well in short they give data sources super powers. These streams should not be confused with File I/O streams which are a completly different thing.

#### The features of Java stream are –

- A stream is not a data structure instead it takes input from the Collections, Arrays or I/O channels.

- Streams don’t change the original data structure, they only provide the result as per the pipelined methods.

- Each intermediate operation is lazily executed and returns a stream as a result, hence various intermediate operations can be pipelined. Terminal operations mark the end of the stream and return the result.

#### We have two types of operations with streams

***1. Intermediate Operations***

These are operations that result into other streams which means more processing can still be done on them, like:

- map: The map method is used to returns a stream consisting of the results of applying the given function to the elements of this stream.

```
List number = Arrays.asList(2,3,4,5);
List square = number.stream().map(x->x*x).collect(Collectors.toList());
```
- filter: The filter method is used to select elements as per the Predicate passed as argument.

```
List names = Arrays.asList("Reflection","Collection","Stream");
List result = names.stream().filter(s->s.startsWith("S")).collect(Collectors.toList());
```
- sorted: The sorted method is used to sort the stream.

```
List names = Arrays.asList("Reflection","Collection","Stream");
List result = names.stream().sorted().collect(Collectors.toList());
```

***2. Terminal Operations***

These are operations that result into a final value which marks the stream as consumed and no further processing can be done, like:

- collect: The collect method is used to return the result of the intermediate operations performed on the stream.

```
List number = Arrays.asList(2,3,4,5,3);
Set square = number.stream().map(x->x*x).collect(Collectors.toSet());
```

- forEach: The forEach method is used to iterate through every element of the stream.

```
List number = Arrays.asList(2,3,4,5);
number.stream().map(x->x*x).forEach(y->System.out.println(y));
```

- reduce: The reduce method is used to reduce the elements of a stream to a single value.
The reduce method takes a BinaryOperator as a parameter.

```
List number = Arrays.asList(2,3,4,5);
int even = number.stream().filter(x->x%2==0).reduce(0,(ans,i)-> ans+i);
```


### Resources
1. https://stackify.com/streams-guide-java-8/
2. https://www.geeksforgeeks.org/stream-in-java/