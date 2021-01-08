---
_db_id: 85
content_type: topic
ready: true
title: Clean Code for Python
prerequisites:
  hard:
    - topics/clean-code/general
---

Please bookmark this page. If you submit a project and the code is not clean then you will be asked to go clean up your work. This isn't all going to make 100% perfect sense to you right now, but as you move forward in your course more and more will make sense.
## Tabs or Spaces

Python is about whitespace and if you are working on a team then your whitespace better line up otherwise you'll just make errors.

If you are running vscode then set it up so that whenever you hit the Tab key it makes 4 spaces.

Your code should always use 4 spaces to indent:
```
for i in range(5):
    print("see those 4 spaces at the start of this line")
```

## Cheat codes

If you are running vscode then you can set it up to autoformat your code whenever you hit save. You'll be asked what formatter to use. We recommend using [Black](https://github.com/psf/black). Once you go black you never go back. 


## Naming Conventions

### Function and Variable Names

Function names should be `lowercase`, with words separated by underscores as necessary to improve readability.
Variable names follow the same convention as function names.

`they_are_named_like_this`, `NotLikeThis`, and `definately_Not_Like_This`.

### Class Names

Class names should normally use the `CapitalizedWords` convention.

### Package and Module Names

Python packages should have short `lowercase` names.

### Constants

Constants are usually defined on a module level and written in `UPPERCASE` with underscores separating words. Examples include `MAX_OVERFLOW` and `TOTAL`.

### Names to Avoid

Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
In some fonts, these characters are indistinguishable from the numerals one and zero. 

### When to break the rules

If you are working with someone else's code and there is a different convention in place then follow that convention. It's really imnportant to stay consistent. Inconsistent code leaves people guessing, and guesses make bugs. 


## Comments

### Block Comments

Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a `#` and a single space (unless it is indented text inside the comment).
Paragraphs inside a block comment are separated by a line containing a single `#`.

### Inline Comments

Use inline comments sparingly.

An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.
Inline comments are unnecessary and in fact distracting if they state the obvious. Don't do this:

```
    x = x + 1                 # Increment x
```
But sometimes, this is useful:
```
    x = x + 1                 # Compensate for border
```
Why? Because coders read code. If your comments just rewrite the code in English then that's just a waste. 
## Imports

Imports should usually be on separate lines:

```
# Yes: 
import os
import sys

# No: 
import sys, os
```

It's okay to say this though:

```
from subprocess import Popen, PIPE
```

Absolute imports are recommended, as they are usually more readable and tend to be better behaved (or at least give better error messages) if the import system is incorrectly configured (such as when a directory inside a package ends up on sys.path):

```
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```

However, explicit relative imports are an acceptable alternative to absolute imports, especially when dealing with complex package layouts where using absolute imports would be unnecessarily verbose:

      from . import sibling
      from .sibling import example

  Standard library code should avoid complex package layouts and always use absolute imports. Implicit relative imports should never be used and have been removed in Python 3.

When importing a class from a class-containing module, it's usually okay to spell this:

    from myclass import MyClass
    from foo.bar.yourclass import YourClass

If this spelling causes local name clashes, then spell them explicitly:

    import myclass
    import foo.bar.yourclass

and use `myclass.MyClass` and `foo.bar.yourclass.YourClass`.

- Wildcard imports (from <module> import \*) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools. There is one defensible use case for a wildcard import, which is to republish an internal interface as part of a public API (for example, overwriting a pure Python implementation of an interface with the definitions from an optional accelerator module and exactly which definitions will be overwritten isn't known in advance).

When republishing names this way, the guidelines below regarding public and internal interfaces still apply.

## Strings

In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this. The recommended way of writing strings is by using f strings. They allow you to add variables into a string without using `+` to concatenate. That improves readability.

Normal Strings:

    "Hi my name is " + name + " " + surname + " and I am part of " + company

F strings:

    f"Hi my name is {name} {surname} and I am part of {company}"

PEP 257 describes good docstring conventions. Note that most importantly, the """ that ends a multiline docstring should be on a line by itself:


### Documentation Strings

Conventions for writing good documentation strings (a.k.a. "docstrings") are immortalized in [PEP 257](https://www.python.org/dev/peps/pep-0257).

- Write docstrings for all non-obvious public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods
- PEP 257 describes good docstring conventions. Note that most importantly, the """ that ends a multiline docstring should be on a line by itself:

`module.py`:

```
""" this is the docstring for the module
"""

""" this is not a docstring, this is a mistake
"""

class Whatever:
    """classes can have docstrings too
    """

    def stuff( ...):
        """functions can have docstrings
        """

def moar_stuff():
    """module level functions too
    """
```