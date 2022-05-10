---
_db_id: 709
content_type: project
flavours:
- any_language
ready: true
submission_type: link
tags:
- technical-assessment
title: 'Assessment: Functions, return statements and printing to the terminal'
---

Students should 100% understand the following concepts. Note that simply memorizing this stuff will be insufficient. In the final test, the different concepts will be combined in complex ways.

Make use of print statements to check that the student knows what order things will happen in.

## Note about submission format

On Tilde you will notice that this card is asking for a link submission. **Please don't worry about submitting a link**. You will be assessed according to {{% contentlink path="specific-skill-success-criteria/introduction-to-assessments" %}}

## Return and print are different things

A lot of people get this wrong because they learn to code using a REPL. Java folks are less likely to fall into this trap.

Here are some basic code examples. It is in Python but easy to translate to other languages.

```
def foo():
    print("hi")

x = foo()
print(f"x = {x}")
```

Many think that the code will print `x = hi`. It does not.

## Multiple different return statements inside a single function

For example:

```
def foo(colour):
    if colour == "blue":
        return 1
    return 2
```

## Multiple function calls

```
x = foo("blue")
x = foo("red")
print(f"x = {x}")
```

Many people think that the final print statement gets executed multiple times but it does not.

## Return statements inside for loops

```
def foo():
    for i in range(10):
        return i

x = foo()
print(f"x = {x}")
```