---
_db_id: 366
content_type: topic
nqf: ncit
ready: false
tags:
- git
title: Version Control
unit_standards:
- 115362
---

## 1. Libraries and organising projects

### Working with libraries

In your life as a coder, you will use external libraries to help make your software development easier and faster. A JavaScript library is pre-written JavaScript code (functions, objects, definitions) which allows for easier development of JavaScript-based applications and websites. If you haven’t discovered already, there are thousands of libraries available for you to use and the developers of these libraries are updating them all the time. It’s up to you to figure out where to find the most up-to-date version of this library is and how to use it.

Where to look
When you hear about a new library or framework, the first step is to go to the website for the library. For well-used libraries, you will find information about what projects that library is good for, examples of things built with that library, and tutorials on how to use it. Most importantly, you will also find instructions on how to download and use the latest version of the library in your own projects.


Some libraries host all of their code online, so you can simply include a link to the source file in your project. For example, if you want to use jQuery in a website you could include this line of code inside the `<head>` tag:


`<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>`


For some libraries, it may be better to download the library source code to your local machine and store it within your project folder (more on this in the next section). This is especially useful if you are developing an app or site while you are not connected to the Internet.


In either case, the best resource is to visit the website for the framework or library to retrieve the latest information on how to use that library.

### Documentation

Some libraries are huge. They have so many built in functions and tools that you could spend years trying to learn them all. And by the time you learn them, the library will be updated with new functionality. This isn’t a good use of your time. In most cases, you will only need to use a small fraction of the built-in functionality of an external library.


To find out how to use a particular function, it’s best to look on the Documentation page of the library. Depending on the library, it may be called “Documentation”, “Resources”, “API Docs”, etc. Whatever they call it, you’ll soon discover these pages will be your best friend. For well-documented libraries you’ll find in-depth explanations and several examples for each function.


Take a look at the jQuery documentation page as an example:

http://api.jquery.com/


Documentation for Phaser can be found at this link:

https://phaser.io/docs/2.6.2/index


It’s also recommended that you check out some tutorials on Phaser. Those will be the best way to learn how the library works.



### Organising your project files

As your software and web development projects become more complex you will create more and more files. Even for for a basic website, you have multiple HTML files, a CSS file, images, and maybe some JavaScript files. Following common industry standards on keeping your project organised will make your life as a developer so much easier. Plus, it will enable you to share your code and work with other coders more easily.


#### Naming conventions

Regardless of the type of project you are working on, the first step is to create a project folder. This folder will contain all of the other folders and files associated with the project. What should you call your folder? Every name you give to your folders and files should be completely in lowercase with no spaces. Why?


 - Many computers, particularly web servers, are case-sensitive. So for example, if you put an image on your website at `test-site/MyImage.jpg`, and then in a different file you try to invoke the image as `test-site/myimage.jpg`, it may not work.

 - Browsers, web servers, and programming languages do not handle spaces consistently. For example, if you use spaces in your filename, some systems may treat the filename as two filenames. Some servers will replace the spaces in your filenames with `%20` (the character code for spaces in URIs), resulting in all your links being broken. It's better to separate words with dashes, rather than underscores: `my-file.html` vs. `my_file.html`.


So, you should use a hyphen for your file names. The Google search engine treats a hyphen as a word separator, but does not treat an underscore that way. For these reasons, it is best to get into the habit of writing your folder and file names lowercase with no spaces and with words separated by dashes, at least until you know what you're doing. That way you'll bump into fewer problems later down the road.


#### Files and folders
Within your main project folder, you should organise the rest of your files in a logical manner. In general, this means have a folder for images, styles, and scripts (for a basic website).

![](1.png)


For apps and other projects, you’ll want to organise your files in a similar way. Perhaps you’ll have a “lib” folder for any external libraries used in your project.


Different people have different preferences about how to organise project files. The main point to remember is to keep things organised, thoughtfully named (all lowercase with no spaces), and easy to find. This will make it easy for you and your team to work together. Generally you’ll be creating these files and folders directly in your text editor, like Atom, so it will be easy to keep things organised.

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