---
_db_id: 634
content_type: topic
ready: true
title: Getting Git set up
---

Git is a critical tool for any kind of coder. We'll get git set up before you do anything else. You'll need to get comfortable using git from the command line.

## If you have a computer

**Optional:** The Internet runs on Linux so if you can install Linux that would be useful. There are a few options here if you want to set yourself up:

- [Ubuntu](https://ubuntu.com/) is great
- [Mint](https://linuxmint.com/) is like Ubuntu but your computer doesn't need to be as powerful to run it
- [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) lets you run Linux inside Windows.

**Not Optional:** Please download and install git. You can find out more [here](https://git-scm.com/).

## If you have an Android device

Start by installing Termux: https://play.google.com/store/apps/details?id=com.termux&hl=en_ZA

It's a terminal application that lets you execute bash commands.

Now you need to set Git up on Termux:

Type in the following commands:

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

This video walks you through the process:  https://www.youtube.com/watch?v=DG3l9sxFVnY

Note:

- If any of these commands ask you if you want to continue, then type in `Y` then enter.
- At some point, Termux will ask you for a GitHub password. When you type in a password then it looks like nothing is being typed. This is normal. Just type out your password like you normally would and press enter.
- you can use the tab key for autocompletion, and the up arrow to get the previous command. This should speed you up a little bit.

## If you have an iPhone

Eish, we haven't managed to find anything good here. If you have any suggestions please bring them up. You can even submit a PR, we'll all be very impressed.

## If you don't have the gear you need

Do your best to find a solution on your own

- ask your friends and family if you can borrow something
- see if you can find an Internet cafe and try to make a deal
- see if any co-working spaces near you have computers available
- see if you can make a plan with someone who refurbishes computers for a living, sometimes you can pick up the gear very cheaply