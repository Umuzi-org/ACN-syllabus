---
title: Getting set up to write Python on your computer
---

## Install the correct version of Python

A lot of operating systems come with Python2.7 installed. Python2.7 is commonly referred to as "legacy Python". In tech, "legacy" is a dirty word.

You need to install and use the latest version of Python that is available. It'll have a version number >= 3.9

RealPython has an installation guide [here](https://realpython.com/installing-python)

## Install VSCode and plugins

https://code.visualstudio.com/ 

This is a really wonderful code editer, it works on any operating system and has a few features we like a lot. [Here] (https://www.youtube.com/watch?v=liy7kSdLB7s) is a video that shows you some vscode features. The video talks about JavaScript but it is relevant to other languages as well.

VSCode has a rich ecosystem of plugins. There are a few that will make your life better:

- ms-python.vscode-pylance: This is an awesome bundle of python tools

When you start working with Python files then vscode will ask you what autoformatter you want to use. There are a few and some of them have pretty funny names. We use `black`.

## Try it out

You don't need to hand this in or anything. It's just for you to check that stuff is running correctly.

Use VSCode to create a new file.

Inside the file, type in

```
print("Winning")
```

Now save the file. You can just call it `winning.py` or something. The `.py` at the end is really important. Whenever you save a Python file you need to add .py to the end. 

You can open up a terminal right in VSCode using the menu at the top of the screen. Alternatively use the keyboard shortcut: "Ctrl+`".

Now if you type in `python3 winning.py` your code will run.

If you get the error `can't open file 'winning.py': [Errno 2] No such file or directory` then it just means you saved your file somewhere unexpected. Right click on your file name in vscode (the file name can be seen in the tab control at the top of the screen, and also in the file explorer on the left if you have it open). You'll see a context menu pop up. Choose to "Copy Path". Then use this command in the terminal:

```
python3 [the path you just copied]
```

For example this is how it would look on my computer:

```
python3 /home/sheena/workspace/temp/winning.py
```
