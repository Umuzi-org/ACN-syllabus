---
_db_id: 712
content_type: project
flavours:
- any_language
ready: true
submission_type: link
tags:
- technical-assessment
title: 'Assessment: For loops'
---

Many people do pattern matching instead of understanding. Here are some common things that will be tested:

## Note about submission format

On Tilde you'll notice that this card is asking for a link submission. **Please don't worry about submitting a link**. You will be assessed according to {{< contentlink path="specific-skill-success-criteria/introduction-to-assessments" >}}

## JS and Java learners understand that they can count up and down.

```
for (some_initialiser,some_check,some_update){
    ...
}
```
They should be able to reason about each of the different parts of the configuration of the loops.

\## Python learners understand `range` and `in`.

```
for x in [1,2,3,4,5]:
   ...

for x in range(len(arr))
    ...
```

- They should be able to move forward or backwards.
- They should also understand how to use `enumerate`.

## All learners understand that the whole body of the loop executes on each iteration.

```
for i in range(5):
    print('a')
    print('b')
```

## All learners understand that loop counters don't magically fetch information from other data structures.

```
arr = ['a','b','c']

for (let i = 0; i< arr.length; i++){
    console.log(i)    // this does not print a, b or c ever
}
```

## All learners should be able to reason about nested for loops.

```
for n in [0,1,2]:
    for m in [0,1,2]:
        print(n,m)   # this executes 9 times. Why? What gets printed?
    print("here")    # this one only executes 3 times. Why?
```

## All learners should be able to reason about continue and break in a single for loop.

E.g.:
```
for (let i = 0; i < 5; i++){
    print(i)
    print("a")
    if (i <2) continue; // what does this do?
    print("b")
    if (i>4) break;     // how about this?
    print("c")
}
```

## All learners should be able to reason about `continue` and `break` within a nested for loop.

```
for (let n=0; n<3; n++){
    print(n)
    for (let i = 0; i < 5; i++){
        print(i)
        print("a")
        if (i <2) continue; // what does this do?
        print("b")
        if (i>4) break;     // how about this?
        print("c")
    }
}
```

## All learners should be able to iterate over strings and arrays.

Some people think you need to turn strings into arrays before you can start iterating over them. This is not the case!

## All learners should understand the basics of while loops.

- Can you convert a for loop into a while loop?
- How do `break` and `continue` statements work in while loops versus for loops?