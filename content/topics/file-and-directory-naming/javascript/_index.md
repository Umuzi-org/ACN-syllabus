---
content_type: topic
prerequisites:
  hard:
    - topics/file-and-directory-naming/general 

ready: true
tags:
  - File and directory naming
title: File and directory naming in JavaScript
---

## How should I name my JavaScript files and directories?

When thinking about how to name files in JavaScript, think of the file as an entity within the code. That is to say - try to think of the file name as a normal camelCased variable. The same logic should apply for naming directories that live inside your **src** directory - The directory name should reflect what is inside it. Remember to be always consistent.

If you have a file containing a number of helper functions, it makes sense to name the file `utilities.js` (A utility is a piece of code that that is too small to be considered a separate application) or `utils.js`. If you have a file containing configuration code, then name the file `configuration.js` or `config.js`. If you want to create a program called morse code, then please name the file `morseCode.js`. Notice that these names represent exactly what is inside the files and reads much like the language convention.

The same thing should be done for files inside your **spec** (test) folder, with the small difference that the file name should end with `_spec.js` to indicate that this is a spec file. I.e. If you want to write tests for a program called `morseCode.js`, then name the test file like so: `morseCode_spec.js`.

To get a very basic idea, please see: {{% contentlink path="projects/oop/animals/part2" %}}

### Bad file and directory naming in JavaScript

To find out if you have badly named a file, think of how you would name a normal JavaScript variable or function. If the file name does not follow the same rule, then it is probably badly named. Below are examples of badly named files:

```
my-file-name.js
my.file.name.js
myfilename.js
my-file_name.js
my_file_name.js
```

Here are examples of badly named directories

```
my-directory-name
my directory named
mydirectoryname
my.directory.name
my-directory_name
my_direcroty_name
```

### Advantages of well named files

- Your code becomes easier to search. This comes in handy once you start working on a big project, where searching for things will consume most of your time.
- Self documentation. The same way your code should be easily readable - so should your files. This saves you and your team loads of time.
- Cleaner import/exports. Good naming makes importing/exporting modules and creating variables inside your your files easier and more intuitive.
- Debugging becomes easier.
