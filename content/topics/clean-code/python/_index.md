---
_db_id: 85
content_type: topic
ready: true
title: Clean Code for Python
---

## Tabs or Spaces

`4 spaces == 1 tab`

Spaces are the preferred indentation method.
There are not many serious open source project uses tabs in Python code, so it is recommended that use spaces.
Python 3 **DISALLOWS** mixing the use of tabs and spaces for indentation. Using a code formatter will make your life way easier.
We recommend using [Black](https://github.com/psf/black).

## Imports

- Imports should usually be on separate lines:

```
  Yes: import os
  import sys

  No: import sys, os
```

It's okay to say this though:

```
from subprocess import Popen, PIPE
```

- Absolute imports are recommended, as they are usually more readable and tend to be better behaved (or at least give better error messages) if the import system is incorrectly configured (such as when a directory inside a package ends up on sys.path):

        import mypkg.sibling
        from mypkg import sibling
        from mypkg.sibling import example

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

## Naming Conventions

The naming conventions of Python's library are a bit of a mess, so we'll never get this completely consistent -- nevertheless, here are the currently recommended naming standards. New modules and packages (including third party frameworks) should be written to these standards, but where an existing library has a different style, internal consistency is preferred.

### Class Names

Class names should normally use the `CapitalizedWords` convention.
The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.
Note that there is a separate convention for builtin names: most builtin names are single words (or two words run together), with the `CapitalizedWords` convention used only for exception names and builtin constants.

### Package and Module Names

Python packages should have short, all-`lowercase` names, although the use of \_underscores\_ is discouraged.
When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. \_socket).

### Function and Variable Names

Function names should be `lowercase`, with words separated by underscores as necessary to improve readability.
Variable names follow the same convention as function names.
`mixedCase` is allowed only in contexts where that's already the prevailing style (e.g. `threading.py`), to retain backwards compatibility.

### Constants

Constants are usually defined on a module level and written in `UPPERCASE` with underscores separating words. Examples include `MAX_OVERFLOW` and `TOTAL`.

### Names to Avoid

Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use 'l', use 'L' instead.

## Comments

### Block Comments

Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a `#` and a single space (unless it is indented text inside the comment).
Paragraphs inside a block comment are separated by a line containing a single `#`.

### Inline Comments

Use inline comments sparingly.

An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.
Inline comments are unnecessary and in fact distracting if they state the obvious. Don't do this:

    x = x + 1                 # Increment x

But sometimes, this is useful:

    x = x + 1                 # Compensate for border

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