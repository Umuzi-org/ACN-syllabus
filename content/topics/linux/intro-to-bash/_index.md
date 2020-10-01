---
_db_id: 60
content_type: topic
ready: true
tags:
- bash
- linux
title: Introduction to Bash and the terminal
---

Knowing a bit about the terminal will help you a lot in your learning journey. If you haven't met the command line before then this is probably going to seem a little strange at first. But when you get used to it it's really useful.

## Why is it useful?

1. It will speed you up. Interacting with your computer via the keyboard can be very quick compared to using the mouse.
2. If you ever deploy your code to production (eg: host a website, or get a data-pipeline running on a cloud provider ), then chances are that you'll be using Linux. If you don't have physical access to a computer you can still control it using the command line! The internet runs on this stuff!

## What you need to know

### Conquering the command line

http://conqueringthecommandline.com/book/basics

- Chapter 1 is necessary
- `curl` is useful but it might not make a tonne of sense right now
- `grep` is useful

### Command-line bootcamp

http://korflab.ucdavis.edu/bootcamp.html

This covers some of the same material as "Conquoring the command line". If you understand all this then you are in a good place :)

## Next level Ninja stuff

One of the really awesome things about Linux is that it can be customized!

If you want to be even faster and more awesome then there are a few extra tools you'll need. If you install this stuff now and just get used to using it then it will save you time and impress your friends ;)

1. Use `Terminator` instead of terminal.

You can install it using `sudo apt-get install terminator`

This just gives you a few useful extra features. This Indian dude who likes shiney cars will tell you more about it: https://www.youtube.com/watch?v=mMak2VzRbmc

2. Set up your keyboard shortcuts so you can open a new terminal instantly whenever you want. See if you can figure this one out on your own.

3. Install zsh.

This one might be challenging to those of you who are new to Linux. Feel free to skip this for now but once you know a bit more then it's very worthwhile. Come back and get it set up when you are more confident.

Zsh is an alternative to bash and it just saves loads and loads of time! It also allows all sorts of theming and customisations.

Use oh-my-zsh if you want to get the most out of it: https://github.com/ohmyzsh/ohmyzsh . This comes with a number of plugins.

Here are some recommended plugins:

```
plugins=(git docker docker-compose per-directory-history alias-tips)
```

Most of these are included in oh-my-zsh but you have to install alias-tips seperately