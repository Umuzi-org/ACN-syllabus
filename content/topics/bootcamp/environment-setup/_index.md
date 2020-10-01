---
_db_id: 396
content_type: topic
ready: true
title: Getting set up to write code on your device
---

You'll need to be set up so that you can write and run code on your own device.

## If you have a computer

You'll need a couple of things:

- https://code.visualstudio.com/ This is a really wonderful code editer, it works on any operating system and has a few features we like a lot. [Here] (https://www.youtube.com/watch?v=liy7kSdLB7s) is a video that shows you some vscode features. The video talks about JavaScript but it is relevent to Python people as well.
- https://git-scm.com/downloads

- Optional: The internet runs on Linux so if you can install Linux that would be useful. If you earn certain bursaries with us then we'll hook you up with a Linux computer. There are a few options here if you want to set yourself up:
  - [Ubuntu](https://ubuntu.com/) is great
  - [Mint](https://linuxmint.com/) is like Ubuntu but your computer doesn't need to be as powerful to run it
  - [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) lets you run Linux inside Windows.

### If you are a data scientist or data engineer

You'll need to run your code using Python. Ideally you should be using a modern version of Python. Python2.7 is commonly referred to as "legacy Python". In tech, "legacy" is a dirty word.

### If you are doing data science

Optional: You can also start practicing to use Anaconda and use its Integrated Development Environment, but all the the pre-bootcamp learning resources can be done on any Python-friendly IDE like Visual studio above.

Follow latest installation instruction from the official Anaconda website - https://www.anaconda.com/download/

### If you are doing web dev

Optional: Install [Node](https://nodejs.org/en/download/). Node gives you a way to run JavaScript code without having to use a web page.

In a command line you can then do things like `node my_script.js`. This can be quite convenient.

## If you have an Android device

If you don't have a computer you can use then you can use your phone. Here's how to get set up on an Android.

You'll need to install 2 things:

- Acode: This is where you will edit your code: https://play.google.com/store/apps/details?id=com.foxdebug.acodefree&hl=en_ZA
- Termux: https://play.google.com/store/apps/details?id=com.termux&hl=en_ZA

Have some videos:

- Using ACode: https://www.youtube.com/watch?v=XZAc-imlq88 This vdeo focuses on JavaScript, but dont panic if you are a python person. We'll talk about python a bit later.
- Setting up Git on Termux: https://www.youtube.com/watch?v=DG3l9sxFVnY

Termux takes a little bit of setup before you can use it for all the stuff we need. Also, it might seem really weird and confusing at first. If this stuff kicks your a\$\$ then rather come back to this page when you feel ready. But you do need to get comfortable with this stuff before bootcamp.

When you open termux up for the first time please do the following:

```
pkg update
pkg upgrade
pkg install git
git config --global user.email "your@email.whatevs"
git config --global user.name "your name"
termux-setup-storage
cd storage/shared
# now you can cd into your folders and interact with git
```

Note:

- If any of these commands ask you if you want to continue, then type in `Y` then enter.
- At some point Termux will ask you for a github password. When you type in a password then it looks like nothing is being typed. This is normal. Just type out your password like you normally would and press enter.

### If you are a data scientist or data engineer

You can use ACode to write python code too. Just be sure to save your files with the `.py` extension.

To run your python files, you need to use Termux.

First install python like so:

```
pkg install python
```

Then you can open a python interpreter at any point with the command `python`.

You can also run your python scripts like so:

```
cd /path/to/wherever/you/stored/your/goodies
python my_script.py
```

Try it out and remember to ask for help if you get stuck

## If you have an iPhone

Eish, we haven't managed to find anything good here. If you have any suggestions please bring them up.

## If you don't have the gear you need

Do your best to find a solution on your own

- ask your friends and family if you can borrow something
- see if you can find an internet cafe and try make a deal
- see if there are any co-working spaces near you that have computers available
- see if you can make a plan with someone who refurbishes computers for a living, sometimes you can pick up gear very cheaply
