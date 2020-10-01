---
_db_id: 268
available_flavours:
- any_language
content_type: project
from_repo: projects/tdd/simple-calculator-part1
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - projects/tdd/simple-calculator-part1
  soft: []
ready: true
story_points: 8
submission_type: continue_repo
tags:
- tdd
title: simple-calculator part 2
---

This a continuation of {{% contentlink path="projects/tdd/simple-calculator-part1" %}}. If you haven't done that yet then please do. At this point you should have a well tested `add` and `multiply` function.

This exercise will require a little OOP knowledge. Brace yourself.

## Set up your environment

### Javascript

Please test your code using jasmine.

Your directory structure should look like this.

```
    >node_modules    <---- make sure this is in your .gitignore
    >spec
        > support
            - jasmine.json
        - string_calculator_spec.js
    >src
        - string_calculator.js
    - package.json
```

### Python

Your project is expected to be completed using pytest. You are expected to follow industry best practices in all things. This means that you need to have a directory structure that is in good shape. Please name your files and folders like this:

```
├── simple_calculator   the package under test
│   └── calculator.py
├── requirements.txt    installation requiremnts
├── setup.py            installation script for the package under test
└── tests               all package tests go in this directory
    └── test_calculator.py
```

Please take a look at this topic to see an explanation of the required directory structure.
{{%contentlink "topics/python-specific/automated-testing-with-pytest" %}}

## Introducing the calculator class

Update your tests so that they expect the `add` and `multiply` functions to be part of a class. Now make those tests pass.

For now on this document will just describe the features we need the Calculator to have. You need to figure out the tests and implementation yourself.

## Note

This is an extension of {{% contentlink path="projects/tdd/simple-calculator-part1" %}}. In other words, previously implemented functionality should still work.

```
# this should still work
calculator_instance.add(3,5) # should return 8
calculator_instance.multiply(30,2) # should return 60

# and multiple arguments should work too
calculator_instance.add(3,5,2) # should return 10
```

The `multiply` functionality should also still work.

## Remember the last result

The calculator should have a function called `last` that returns the last result. Example usage:

```
calculator_instance.add(1,2)
calculator_instance.last() # should return 3
```

## Use the last result in other calculations

The `add` and `multiply` functions should allow `"LAST"` as a parameter.

Example usage:

```
calculator_instance.add(1,2)
calculator_instance.multiply("LAST",5) # should return 15
```

## Memory Slots

Allow the calculator to remember more stuff by implementing a `set_slot` function. The `set_slot` function should take a single number as an argument. That argument is called the slot number. Also implement `get_slot` for getting the value from a memory slot. Neither get_slot or `set_slot` should effect the output of `last`.

Example usage:

```
calculator_instance.add(1,2)
calculator_instance.set_slot(1)
calculator_instance.get_slot(1) # should return 3
calculator_instance.add(10,20)

calculator_instance.set_slot(2)
calculator_instance.get_slot(2) # should return 30

calculator_instance.add(100,200) # returns 300. The "last" value is updated
calculator_instance.get_slot(1) # should return 3
calculator_instance.get_slot(2) # should return 30
calculator_instance.last() # should return 300
```

## Allow the use of memory slots and LAST as arguments

The `add` and `multiply` functions should allow memory slots as parameters. If we were using memory slot 5 as an argument then we would represent it like this `"SLOT_5"`.

Example usage:
Following from the previous example:

```
calculator_instance.add(100,200) # returns 300. The "last" value is updated
calculator_instance.get_slot(1) # should return 3
calculator_instance.get_slot(2) # should return 30
calculator_instance.last() # should return 300 (just like before)

# THE FOLLOWING FUNCTIONALITY SHOULD WORK

calculator_instance.add("LAST",10) # should return 310 (= 300 + 10)
calculator_instance.add("SLOT_1",5) # should return 8 (= 3 + 5)
calculator_instance.multiply("SLOT_2",2) # should return 60 (= 30 * 2)
```