---
content_type: topic
prerequisites:
  hard:
    - topics/file-and-directory-naming/general # This is currently missing. It is still here: Umuzi-org/ACN-syllabus#314

ready: true
tags:
  - File and directory naming
title: File and directory naming in JavaScript
---

## How should I name my JavaScript files and directories?

When thinking about how to name files in JavaScript, think of the file as an entity within the code. Meaning, if you have a file with a class called `MyClass`, then it also makes sense to name the file `MyClass.js` ; notice that the naming convention utilizes _PascalCase_. The same thing for a file containing a function. `myFunction` should live inside a _camelCased_ file called `myFunction.js` . The same logic should apply for naming directories that live inside your **src** directory. Remember to be always consistent.

The same thing should be done for files inside your **spec** folder(Tests), with the small difference that the file name should end with `.spec`. if you want to test a function called `login.js`, then name the test file like so: `login.spec.js`.

### Advantages of good naming convention:

- Your code becomes easier to search. This comes in handy once you start working on a big project and where searching for things will consume most of your time.

- Self documentation. The same way your code should be easily readable - so should your files. This saves you and your team loads of time.

- cleaner import/exports. Good naming makes importing/exporting modules and creating variables inside your your files easier and more intuitive.

- Consistency. This is the key to maintainability.

### Resources:

The following resources should help you get a good idea about general naming conventions in JavaScript:

<https://google.github.io/styleguide/jsguide.html#file-name>

<https://javascript.plainenglish.io/javascript-naming-convention-best-practices-b2065694b7d>

<https://www.fool.com/the-blueprint/file-naming-conventions/>
