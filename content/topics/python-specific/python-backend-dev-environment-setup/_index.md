---
_db_id: 170
content_type: topic
ready: true
title: Python backend dev environment setup
---

### What you need

This page is here to help you get set up on your local machine. These are very important tools we use at Umuzi and eventually at the workplace.

#### Installations

Setting up your environment needs you to to install a bunch of stuff. A good programmer knows their stuff, knows what they are installing and doesn't just jump into code. You will need the following:

- [VScode](https://code.visualstudio.com/docs/setup/linux): Visual Studio Code is an IDE developed by Microsoft for Windows, Linux and macOS. An integrated development environment is a software application that provides comprehensive facilities to computer programmers for software development.</br>
An IDE normally consists of at least a source code editor, build automation tools, and a debugger. What makes an IDE so useful is the I: integrated. You could use just about anything for a development environment and many people use a variety of basic, individual programs in place of an IDE but an integrated environment gives you the ability to do everything in a single editor.  
- [python3.7](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/): You will need to install the latest version of python3.7.* . Why Python? because it's friggin awesome. You can use Python for developing desktop GUI applications, websites and web applications. Also, Python, as a high level programming language, allows you to focus on core functionality of the application by taking care of common programming tasks.


#### How to run things on the terminal

The terminal is an interface in which you can type and execute text based commands. It can be much faster to complete some tasks using a Terminal than with graphical applications and menus. Another benefit is allowing access to many more commands and scripts. A common terminal task of installing an application can be achieved within a single command, compared to navigating through the Software Centre or Synaptic Manager. Press *Ctrl + Alt + T* to open the terminal when using Ubuntu/Linux-mint

##### Running Python

There are 2 ways of running python that you should care about right now. The first way is pretty easy. Just open up a terminal end enter the command `python3`. This will open up a thing called a [REPL](https://codewith.mu/en/tutorials/1.0/repl). Basically it lets you just type in python commands and then it executes things. This is really useful if you just want to quickly calculate something or try out a piece of code.


Of course if you've written some awesome code you would want to save it somewhere so you can run it whenever you want. For now let's assume you don't know your way around linux (if you do, that's cool. But for now we'll keep it simple). Try this out:

- Open up a text editer and make a file that looks like this: `print("Welcome to Umuzi!")`
- Save the file as `hellp.py` in your home directory (directory means folder). Now open up a terminal and type in `python3.7 hello.py`


##### Running programs

- After installing from the terminal some programs can allow you to open them from the terminal. So instead of navigating everywhere in your computer you can just type the alias of that program. e.g. Since we installed VScode on our machines, a simple way to open it is to go into the terminal and type in `code`. code is an alias created by the terminal as a short cut for the program.
- You can also open up a terminal and type in `code hello.py`. This opens your file in VScode.

 You can also open up a whole directory in vscode (this is really useful when you start working on real stuff). Try this out in a terminal:

- `mkdir python_practice`    # this command makes a new directory
- `mv hello.py python_practice/hello.py` # this moves the file you made before

You could achieve the stuff above ^^ by using the graphical user interface (the file browser) but where's the fun in that?

Now execute this: `code python_practice`