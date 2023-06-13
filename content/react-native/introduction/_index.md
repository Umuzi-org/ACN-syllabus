---
_db_id: 783
content_type: topic
ready: true
title: Introduction to React Native
---

React Native has a really catchy catch-line: Learn once, write anywhere.

That sounds pretty cool. But what does it mean? And what can't it do?

## Getting acquainted

At this point in your learning journey you should be pretty familiar with React and modern JavaScript. If you aren't yet familiar, or if you want a little re-introduction please revisit this link:

{{< contentlink path="topics/web-frontend/react/intro-to-react" >}}

Next up, read through this and watch all the introductory videos:

[React Native home page](https://reactnative.dev/)

You don't need to be a super-expert just yet, we'll get there 🤓

## Ok, but what is it really - Native versus hybrid dev

React Native is primarily about making mobile apps (although you can even run React Native apps on certain TVs these days. Pretty cool...).

Now when it comes to mobile dev you generally have 2 options: You can go native or you can go hybrid.

Native mobile development means writing code that is specific to a device. So if you wanted to write an iPhone app then you would need to use Swift, and maybe Objective-C. And if you were writing for Android then you'd be using Kotlin, and maybe Java.

That's a whole lotta languages right there.

Now imagine you owned a business and you wanted to build a mobile app. If you went native then the code your crew produced would be really "close to the machine". It would be quick and you would have easy access to hardware functionality. This is kiff (yes, kiff is back. Tell your friends).

The downside is that if you wanted to support only Android and iPhones then you would basically need two teams of devs with very different specialized skillsets. And they would have 2 separate bug lists. Because bugs happen. Sounds expensive.

The other option is hybrid dev. Now a hybrid app is one that uses one code base to support multiple platforms. One codebase, one team, one language... Now that sounds pretty slick, but what about accessing the hardware?

Any serious hybrid app framework (such as React Native) has the ability to access the hardware. It would have a bunch of apis available that let you, for example, talk to the GPS, accelerometer or file system. And you should be able to drop into native code when you need to in case there isn't an api that's already easily available.

## React Native versus other hybrid dev

It's useful for professional developers to understand how the tools they use stack up against competitors. Every tool has its downsides, even React Native.

[Here](https://techdayhq.com/community/articles/top-5-frameworks-for-hybrid-mobile-app-development) is a non-biased comparison of the top hybrid mobile dev tools. Give it a read.

## Why we think React Native is worthwhile

Here is a little list of why React Native is a good thing to learn:

- It works
- It makes good use of web dev skills. So that means that:
  - It's easy to build React Native teams from people who already know web development
  - Any skill learned in React Native is fairly transferrable to web development as a whole
- It's backed by a very solid company - Meta (formally known as Facebook) has a damn fine engineering team
- It's fast on the device - it "compiles" into native components so it works well everywhere
- There is a lot of good content out there and a big community of people willing to help if you get stuck
- React is arguably the most popular web frontend framework around at the time of writing. Levelling up your React skillz is just good for you
- Really serious and amazing dev houses such as BBD have adopted React Native as a part of their stack

If you want more, take a look at these resources:

- [2022 Stack Overflow Developer Survey - Most popular technologies](https://survey.stackoverflow.co/2022/#most-popular-technologies-webframe)
- [Is it still worth learning React Native?](https://spyro-soft.com/blog/is-it-still-worth-learning-react-native-in-2021)
- [Top 10 reasons why you should learn React right now](https://medium.com/@SilentHackz/top-10-reasons-why-you-should-learn-react-right-now-f7b0add7ec0d)

## Learn once, write anywhere? Really?

Well...no

It's more like: Write once, debug everywhere 😆

When you build simple apps then life will be pretty smooth, but every hybrid platform can and does bump up against platform specific weirdness.

Just make sure you are emotionally prepared.