---
_db_id: 709
content_type: topic
ready: true
title: 'Assessment: Functions, return statements and printing to the terminal'
topic_needs_review: true
---

Students should 100% understand the following concepts. Note that simply memorizing this stuff will be insufficient. In the final test the different concepts will be combined in complex ways.

Make use of print statements in order to check that the student knows what order things will happen in.

## return and print are different things

A lot of people get this wrong because they learn to code using a repl. Java folks are less likely to fall into this trap.

Here are some basic code examples. It is in Python by easy to translate to other languages.

```
def foo():
    print("hi")

x = foo()
print(f"x = {x}")
```

Many think that the code will print `x = hi`. It does not.

## multiple different return statements inside a single function

eg:

```
def foo(colour):
    if colour == "blue":
        return 1
    return 2
```

## multiple function calls

```
x = foo("blue")
x = foo("red")
print(f"x = {x}")
```

Many people think that the final print statement gets executed multiple times. It does not.

## return statements inside for loops

```
def foo():
    for i in range(10):
        return i

x = foo()
print(f"x = {x}")
```