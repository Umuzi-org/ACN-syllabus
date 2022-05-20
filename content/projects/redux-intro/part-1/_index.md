---
_db_id: 469
content_type: project
flavours:
- javascript
- typescript
prerequisites:
  hard:
  - topics/redux-intro
ready: true
submission_type: repo
tags:
- redux
title: 'Intro to Redux for home automation: the basics'
---

Redux is generally explained in the context of frontend frameworks. Lots of people think that it is a React thing. Lots of people are wrong... Redux is quite a versatile tool. It can even be used in the absence of a frontend.

In this project we'll be thinking about how we could use redux for a little bit of Internet of things home automation. Fo shizzle. It's that awesome.

Once you have these foundations out of the way you can move onto integrating redux into a frontend. But let's get the foundations out of the way first.

## Instructions

Please note that this is a pure Redux project and doesn't have anything to do with React. When setting up the project, ensure that you separate things into multiple files, e.g. a separate file for the actions, etc. Group things that belong together and make your work clean. Have fun!

Take a little time to google IoT home automation and come up with a list of things you might want to automate in your home once you are a wealthy and successful professional coder.

Arrange all the different things you might want to automate into a state object. Here's an example:

```
state = {
    loungeLighting: "dim",
    discoBallOn: true,
    alarmClockTime : "07:00",
    nowPlaying: "https://www.youtube.com/watch?v=oHg5SJYRHA0",

}
```

Ok, run with it a little bit. What other things would you want to control? Maybe you want to automate your breakfast somehow? Or your garage door?

The next step is to try to figure out what actions a user could take in order to update the state, and then to create some action creators for those.

Eg:

```
function setNowPlaying(videoLink){
    return {
        type: SET_NOW_PLAYING,
        videoLink
    }
}
```

Now implement your reducers.

Make sure you can dispatch your actions in order to update the state.

## Some notes on git feature branching

As a professional coder you will need to use your tools wisely. Git is one such tool.

Try to make multiple small PRs instead of one giant PR when you are doing your work. If you invite rapid feedback then you unlock rapid learning. How can you set up your code reviewers so that they can review your stuff quickly and easily?