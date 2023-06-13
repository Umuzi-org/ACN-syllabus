---
content_type: topic
ready: true
title: What is software?
---

Before we talk about software, let's talk about hamburgers.

## What is a programming language?

Let's say you go out to a restaurant for lunch. When you arrive at the restaurant then someone will greet you and take you to a table, then they'll ask you if you would like to order a drink, then they'll bring a drink and ask you what food you would like to order, and so on. The whole process if pretty predictable. This is an example of an algorithm. 

An algorithm is a sequence of steps that achieve a certain goal.

Now, let's say the waitron asks you what you want to eat and you say "I'd like a hamburger". 

The waitron would then go give that information to the person cooking the food. The cook or chef would then execute an algorithm to prepare the hamburger. 

As a customer, you don't need to think about all the steps in the hamburger-preparation algorithm. You can just give a polite instruction, and then a whole lot of stuff happens, and then you get fed. 

Computer programming is a way to write down instructions that a computer can execute. So instead of telling a waitron what you want, you tell a machine what you want. 

A computer programming language is just a language (like English is a language). It just happens to be very strict on structure. And instead of speaking it out loud you generally write it down. 

## Hiding the details

Now, imagine you ordered your hamburger like this: "Please get a bread roll, slice it in half. Add a piece of lettuce and a slice of tomato. Then prepare a burger patty by first... etc".  You would get a hamburger that is prepared exactly as you want it, but it would be time consuming. And it's good to leave hamburger construction to the experts. 

In computer programming terms we can say that the details of hamburger construction are "abstracted away". There are many details of the process that you just don't need to care about. You just care about the end result.

Back when computers were first invented, programming them was really a lot of work. You needed to enter your computer instructions as a bunch of 1s and 0s, you needed to write code to manage how the hardware was used, you needed to 100% understand the underlying physical machine. 

These days, those "low level" details are "abstracted away". You can just tell a computer program to make a beeping noise, or save a file and it'll do that. The "low level" stuff (hardware management) still happens, but it's behind the scenes. 

## Resources

Here are a few articles you should read:

- https://www.khanacademy.org/computing/computer-programming/programming/intro-to-programming/v/programming-intro
- https://hackr.io/blog/what-is-programming
- https://www.ibm.com/topics/software-development
- https://www.youtube.com/watch?v=pquPUX1EihM

## So what is software

At this point you should know what the following words mean:

- algorithm
- programming language
- abstraction 

So how do these tie together to make software?

Software can be considered to be a collection of interrelated algorithms, specified in programming languages.  That's it.

It sound's easy but it's not. A wise man once said "Writing code is easy, writing software is hard".

Let's give an example... you've heard of Facebook, right? The Facebook application is a piece of software. 

If you open up the Facebook website and write a post then a whole lot of things need to happen under the hood. The details are abstracted away so that you, the end user, don't need to care about them.  Here is some of what needs to happen:

- authentication: the software needs to know who you are. There are all sorts of security algorithms in place to do that
- authorization: the software needs to check if you are allowed to post where you are posting, eg maybe you don't have permission to make a post on a certain group
- networking: The post would be a collection of text and images, this information needs to travel from your computer, over the Internet, to the computers that belong to Facebook
- storage: The post would need to be saved somewhere (we'll talk about databases later)
- notification: if you posted on a group then certain people will need to be notified. And in order for that to happen the software needs to:
    - find out who should be notified
    - check those people's notification settings
    - maybe send an email? 

And there's more. Like a LOT more.

If a person knows how to write code then it really doesn't mean that they are a software developer. 

You can get an idea about the breadth of the field and the challenges involved by reading the following:

- https://en.wikipedia.org/wiki/Computer_science
- https://en.wikipedia.org/wiki/Software_development