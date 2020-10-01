---
_db_id: 255
available_flavours:
- python
content_type: project
submission_type: repo
title: Getting to know Python
---

This little project aims to introduce you to some of the most important aspects of Python.

First make sure that you have Python3.7 installed. There is a nice guide [here](https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/)

## Note

You'll need to submit your work as a git repo. Make sure your latest submission is in the master branch. And make sure your repo is public.

You will be expected to unit test your code. You can choose whichever test framework you like best. Pytest is quite nice and clean.

If you feel that you need extra resources or instruction to pull this off please just ask :)

Please do one step at a time, resist the temptation to read ahead.

## Step 1

Make this function work:

```
def list_all_js_function_names(path_to_js_file):
    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then return a list of js function names as strings
    """

```

Here is an example of a javascript file: https://github.com/MihlaliNelana/CardGame/blob/master/CardGame/script/script.js

Example:

Given

```
// script.js

function promptUser() {  // line 2
  var num = prompt("Please enter number of squares...");
  if (num != null) {
    document.getElementById("demo").innerHTML =
    "You want " + num + " number of squares...";
  }
} // line 8

Array.prototype.memory_card_shuffle = function(){ // line 9
    var i = this.length, j, temp;
    while(--i > 0){
        j = Math.floor(Math.random() * (i+1));
        temp = this[j];
        this[j] = this[i];
        this[i] = temp;
    }
} // line 17
```

Then:

```
list_all_js_function_names("/path/to/script.js")

# this should return

['promptUser','Array.prototype.memory_card_shuffle']
```

### What you should get out of this

- practice unit testing
- get familiar with how functions work
- get familiar with file inputs
- practice (very) basic looping

### Hints :)

There is a lot to this function. It should be broken down a bit instead of doing everything in one go. Remember that we are doing TDD here, that's test driven development. In TDD you try to write the most trivial test possible, then you make that test pass, then you refactor. Then repeat. Try to make sure that each test you write is as small and self-contained as possible while still being useful.

Here are some ideas for some tests:

- test that given a one-line string, your function can detect whether or not it contains a function definition. eg:

  - "function fooo(bar){" is a function definition
  - "a = foo('hi there')" is not a function definition
  - "foo.bar = function something(){" is a function definition

- test that you can return the correct function name. Eg:
  - "function fooo(bar){" the function name is `fooo`
  - "a = foo('hi there')" there is no function defined here
  - "foo.bar = function something(){" the function name is `foo.bar`

Then you'll need to extend your code so that it can take a javascript file as input.

### Resources

- https://docs.python.org/3/howto/regex.html#using-regular-expressions
- https://www.w3schools.com/python/python_regex.asp

You'll need to understand `re.search` to get this right

And here is some file input/output (file io) documentation:

- https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

## Step 2

Upgrade the `list_all_js_function_names` function so that it also returns the start line number and end line number for the functions. Functions in Js are defined with the use of curly brackets.

Instead of returning a list of strings, return a list of dicts.

Now the function should work more like this:

```
list_all_js_function_names("/path/to/script.js")

# this should return

[
    {'name':'promptUser', 'start_row':2, 'end_row':8},
    {'name':'Array.prototype.memory_card_shuffle', 'start_row':9, 'end_row':17}
]
```

Note that functions can be defined inside functions.

### What you should get out of this

- more advanced algorithmic thinking
- a little bit of practice with dictionaries

### Step 3

TBA TODO