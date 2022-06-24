---
content_type: topic
title: Introduction to React Native
---

React Native has a really catchy catch-line: Learn once, write anywhere.

That sounds pretty cool. But what does it mean? And what can't it do?

## Getting aquatinted

At this point in your learning journey you should be pretty familiar with React and modern JavaScript.  If you aren't yet familiar, or if you want a little re-introduction please revisit this link:

{{% contentlink path="topics/web-frontend/react/intro-to-react" %}}

Next up, read through this and watch all the introductory videos:

[React Native home page](https://reactnative.dev/)

You don't need to be a super-expert just yet, we'll get there 🤓

## Ok, but what is it really - Native versus hybrid dev

React Native is primarily about making mobile apps (although you can even run RN apps on certain TVs these days. PRetty cool...).

Now when it comes to mobile dev you generally have 2 options: You can go native or you can go hybrid.

Native mobile development means writing code that is specific to a device. So if you wanted to write an iPhone app then you would need to use Swift, and maybe ObjectiveC. And if you were writing for Android then you'd be using Kotlin, and maybe Java.

That's a whole lotta languages right there.

Now imagine you owned a business and you wanted to build a mobile app. If you went native then the code your crew produced would be really "close to the machine". It would be quick and you would have easy access to hardware functionality. This is kiff (yes, kiff is back. Tell your friends).

The downside is that if you wanted to support only Android and iPhones then you would basically need two teams of devs with very different specialized skillets. And they would have 2 separate bug lists. Because bugs happen. Sounds expensive.

The other option is hybrid dev. Now a hybrid app is one that uses one code base to support multiple platforms. One codebase, one team, one language... Now that sounds pretty slick, but what about accessing the hardware?

Now any serious hybrid app framework (such as ReactNative) has the ability to access the hardware. It would have a bunch of apis available that let you, for example, talk to the gps, accelerometer or file system. And, you should be able to drop into native code when you need to in case there isn't an api that's already easily available.

## ReactNative versus other hybrid dev

It's useful for professional developers to understand how the tools they use stack up against competitors. Ever tool has its downsides, even ReactNative.

[Here](https://techdayhq.com/community/articles/top-5-frameworks-for-hybrid-mobile-app-development) is a non-biased comparison of the top hybrid mobile dev tools. Give it a read.

## Why we think ReactNative is worthwhile

Here is a little list of why React Native is a good thing to learn:

- It works
- It makes good use of web dev skills. So that means that:
  - It's easy to build ReactNative teams from people who already know web development
  - Any skill learned in ReactNative is fairly transferrable
- It's backed by a very solid company - Meta (formally known as Facebook) has a damn fine engineering team
- It is fast on the device - it "compiles" into native components so it works well everywhere

If you want more, take a look at these resources:

- https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-web-frameworks
- https://spyro-soft.com/blog/is-it-still-worth-learning-react-native-in-2021
- https://medium.com/@SilentHackz/top-10-reasons-why-you-should-learn-react-right-now-f7b0add7ec0d


## Learn once, write anywhere? Really?

Well...no

It's more like: Write once, debug everywhere 😆

When you build simple apps then life will be pretty smooth, but every hybrid platform can and does bump up against platform specific weirdness.

Just make sure you are emotionally prepared.
