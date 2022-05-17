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

When thinking about how to name files in JavaScript, think of the file as an entity within the code. This means, if you have a file with a class called `Calculator`, then it also makes sense to name the file `Calculator.js` ; notice that the naming convention utilizes _PascalCase_. The same thing should be done if a file contains a function - if you have a file containing a single function called `calculateDateOfBirth`, it should live inside a _camelCased_ file called `calculateDateOfBirth.js` . The same logic should apply for naming directories that live inside your **src** directory. Remember to be always consistent.

If you have a file containing a number of helper functions, It makes sense to name the file `utilities.js` or `utils.js` and if you have a file containing configurations, then name the file as `configuration.js` or `config.js`.

The same thing should be done for files inside your **spec** folder(tests), with the small difference that the file name should end with `.spec`. if you want to test a function called inside a file called `login.js`, then name the test file like so: `login.spec.js`.

### Bad file and directory naming in JavaScript:

To find out if you have badly named a file, think of how you would name a JavaScript variable, function or class. If the file does not follow the same rule, then it is probably badly named. Below are examples of badly named files:

- my-file-name.js
- my.file.name.js
- myfilename.js
- my-file_name.js

Here are examples of badly named directories:

- my-directory-name
- my directory named
- mydirectoryname
- my.directory.named
- my-directory_name

### Advantages of good naming convention:

- Your code becomes easier to search. This comes in handy once you start working on a big project and where searching for things will consume most of your time.

- Self documentation. The same way your code should be easily readable - so should your files. This saves you and your team loads of time.

- Cleaner import/exports. Good naming makes importing/exporting modules and creating variables inside your your files easier and more intuitive.

- Consistency. This is the key to maintainability.

### Resources:

The following resources should help you get a good idea about general naming conventions in JavaScript:

<https://google.github.io/styleguide/jsguide.html#file-name>

<https://javascript.plainenglish.io/javascript-naming-convention-best-practices-b2065694b7d>

<https://www.fool.com/the-blueprint/file-naming-conventions/>
