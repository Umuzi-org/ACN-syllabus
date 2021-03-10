---
_db_id: 651
content_type: topic
title: Debugging some broken code
---

The focus of this session can be _refactoring_ or _debugging_. The leader guides the follower, but the follower should be doing the actual coding.

## Refactoring

This will be most effective early in the program. Get a piece of working code that is not DRY. It should have a whole bunch of things we don't want recruits to do in it. The goal of the session should be to have the follower identify and fix as many of these issues as possible.

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

As recruits progress through the programme this second type of refactoring should be the main focus. You can cover things like what data structures to use for a given problem, flat vs nested, etc.
