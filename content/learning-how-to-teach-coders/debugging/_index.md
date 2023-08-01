---
_db_id: 651
content_type: topic
title: Debugging some broken code
---

The focus of this session can be _refactoring_ or _debugging_. The leader guides the follower, but the follower should be doing the actual coding.

## Refactoring

This will be most effective early in the program. Get a piece of working code that is not DRY. It should have a whole bunch of things we don't want learners to do in it. The goal of the session should be to have the follower identify and fix as many of these issues as possible.

Here is a simple example;

```py
def my_Function(x):
    if x % 2 == 0:
        print("True")
    elif x % 2 != 0:
        print("False")
```
As the session progress the leader can direct the follower to deeper levels of refactoring. Say the follower cleaned up the function and has something like this;

```py
def is_even(integer):
    if integer % 2 == 0:
        return True
    elif integer % 2 != 0:
        return False
```

The leader can then point out that by definition if a number isn't even it's odd. So we don't actually need that second condition.

```py
def is_even(integer):
    if integer % 2 == 0:
        return True
    else:
        return False
```

As learners progress through the programme this second type of refactoring should be the main focus. You can cover things like what data structures to use for a given problem/operation, flat vs nested, etc.

## Debugging

Get a piece of code that either has a bug or isn't working at all. The goal is for the follower to identify and fix the bug. The leader should clearly explain what the code is meant to do and give some input/output examples.

Once the follower clearly understands what the code is meant to do, get them to run it. Obviously it shouldn't work. Now guide the follower through the debugging process;
- if there's an error explain what it means or better have the follower look it up
- maybe some function is meant to do something with integers but it fails when they are negative, suggest test cases that show this

Once learners are familiar with TDD this session should basically follow the RGR process.