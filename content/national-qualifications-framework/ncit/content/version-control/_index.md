---
_db_id: 366
content_type: topic
flavours:
- any_language
ncit_standards:
- 115362
prerequisites:
  hard:
  - projects/git-exercises
  - projects/tdd/simple-calculator-part1
ready: true
tags:
- git
- ncit
- clean code
title: Version Control
---

## 1. Libraries and organising projects

### Working with libraries

In your life as a coder, you will use external libraries to help make your software development easier and faster. A library is basically a bunch of code (functions, objects, definitions) that can be reused in other coding projects. Different languages use different words for this concept. For example in Python this would be called a Package.

Libraries allow for easier development applications and websites. If you haven’t discovered already, there are thousands of libraries available for you to use and the developers of these libraries are updating them all the time. It’s up to you to figure out where to find the most up-to-date version of this library is and how to use it.

#### Where to look

When you hear about a new library or framework, the first step is to go to the website for the library. For well-used libraries, you will find information about what projects that library is good for, examples of things built with that library, and tutorials on how to use it. Most importantly, you will also find instructions on how to download and use the latest version of the library in your own projects.

#### JavaScript Libraries

Some JavaScript libraries host all of their code online, so you can simply include a link to the source file in your project. For example, if you want to use jQuery in a website you could include this line of code inside the `<head>` tag:


`<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>`


For some libraries, it is better to download the library source code to your local machine and store it within your project folder (more on this in the next section). This is especially useful if you are developing an app or site while you are not connected to the Internet.

Most of the time, when working with Javascript libraries the best thing to do is use `npm` or a similar tool to manage your project dependencies for you.

In any case, the best resource is to visit the website for the framework or library to retrieve the latest information on how to use that library.

### Documentation

Some libraries are huge. They have so many built in functions and tools that you could spend years trying to learn them all. And by the time you learn them, the library will be updated with new functionality. This isn’t a good use of your time. In most cases, you will only need to use a small fraction of the built-in functionality of an external library.

To find out how to use a particular function, it’s best to look on the Documentation page of the library. Depending on the library, it may be called “Documentation”, “Resources”, “API Docs”, etc. Whatever they call it, you’ll soon discover these pages will be your best friend. For well-documented libraries you’ll find in-depth explanations and several examples for each function.

Take a look at the jQuery documentation page as an example:

http://api.jquery.com/

### Organising your project files

As your software and web development projects become more complex you will create more and more files. Even for for a basic website, you have multiple HTML files, a CSS file, images, and maybe some JavaScript files. Following common industry standards on keeping your project organised will make your life as a developer so much easier. Plus, it will enable you to share your code and work with other coders more easily.

There isn't really one standard to rule all standards. Different teams and organisations organise their code in different ways. Be consistent with conventioned that are already in place. And if you are starting a new project then be diligent about keeping oyur code tidy!

Please refer to this project to see a bit more about how you'll be excpected to organise your code during this course:

{{% contentlink path="projects/tdd/simple-calculator-part1" %}}

#### Naming conventions

Regardless of the type of project you are working on, the first step is to create a project folder. This folder will contain all of the other folders and files associated with the project. Dont just save your code onto your Desktop. 

What should you call your folder?

**1. Call it what it is**

Rule number one of naming things is: Choose meaningful descriptive names. Other people should be able to look at the name you chose and be able to figure out your intentions.

**2. Be sensitive to case**

Many computers, particularly web servers, are case-sensitive. So for example, if you put an image on your website at `test-site/MyImage.jpg`, and then in a different file you try to invoke the image as `test-site/myimage.jpg`, it may not work. So it's import to use consistent capitalisation. There should be one standard across your whole project.

The best thing is to use one capitalisation convention across your whole project. Inconsistencies lead to human error, if programmers make errors then those can cause expensive bugs.

**3. Dont use spaces** 

There are many reasons for this. Some are covered in the next point. Some languages simply don't hadle spaces well. So avoid them!

**4. Use dashes if you are exposing things to the web**

Browsers, web servers, and programming languages do not handle spaces consistently. For example, if you use spaces in your filename, some systems may treat the filename as two filenames. Some servers will replace the spaces in your filenames with `%20` (the character code for spaces in URIs), resulting in all your links being broken. Some programming languages can't handle spaces in file names at all. So DONT USE SPACES. Seriously!

In languages that support it, it's better to separate words with dashes, rather than underscores: `my-file.html` vs. `my_file.html`.

The Google search engine treats a hyphen as a word separator, but does not treat an underscore that way. For these reasons, it is best to get into the habit of writing your folder and file names lowercase with no spaces and with words separated by dashes, at least until you know what you're doing. That way you'll bump into fewer problems later down the road.

**5. Different strokes for different folks**

Different languages have different conventions and reasons for those conventions. Different organisations do things differently. 

To see an example of the file/folder naming conventions used in this course pelase see:

{{% contentlink path="projects/tdd/simple-calculator-part1" %}}

#### Files and folders

Within your main project folder, you should organise the rest of your files in a logical manner, you should group related things together. 


Different people have different preferences about how to organise project files. The main point to remember is to keep things organised, thoughtfully named, and easy to find. This will make it easy for you and your team to work together. Generally you’ll be creating these files and folders directly in your text editor, like VSCode, so it will be easy to keep things organised.

## 2. Version control with GIT

### Version Control

One of the most important concepts for a coder to understand is version control. Knowing what version control is and how to use a version control tool will be invaluable to you.

Version control software keeps track of every modification to the code in a special kind of database. It lets you save a snapshot of your complete project at any time you want. When you later take a look at an older snapshot (let's start calling it "version"), your VCS shows you exactly how it differed from the previous one. If a mistake (or “bug”) is discovered in your new version, developers can turn back the clock and compare earlier versions of the code to help fix the mistake while minimizing disruption to all team members.

Version control is independent of the kind of project or technology you're working with:


- It works just as well for an HTML website as it does for a design project or an Android app
- It lets you work with any tool you like; it doesn't care what kind of text editor, graphics program, file manager or other tool you use

### Using GIT in the terminal

The version control system you will use for this project (and every other project you do on a coding team) is GIT. Don’t confuse this with GitHub. GIT is the version control software that you can use anywhere. GitHub is a website where you can store your code and keep track of changes (it is a “hub” for all the updates you make in GIT).

To learn more about what GIT is and how to use it, you can watch the video below and follow the tutorials listed below.

{{< youtube 0fKg7e37bQE >}}

#### Install GIT

First you’ll need to install GIT. Full details are here: https://git-scm.com/downloads

#### Learn basic commands
This tutorial will outline how to create a repository (a new project), configure your account, and learn the basics of adding and updating files to the master branch.

https://www.sitepoint.com/git-for-beginners/