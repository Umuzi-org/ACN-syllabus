---
_db_id: 469
available_flavours:
- javascript
- typescript
content_type: project
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

Take a little time to google IoT home automation and come up with a list of things you might want to automate in your home once you are a wealthy and successful professional coder. Arrange all the different things you might want to automate into a state object. Here's an example:

```
state = {
    loungeLighting: "dim",
    discoBallOn: true,
    alarmClockTime : "07:00",
    nowPlaying: "https://www.youtube.com/watch?v=oHg5SJYRHA0",

}
```

Ok, run with it a little bit. What other things would you want to control?

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

Once you have this down. it would probably be wise to make a PR. Rapid feedback for the win!

## Did you know?

Did you know Tilde uses Redux? Open up the developer console (F12 usually) and you'll be able to see how your interactions dispatch actions and update the state. Most of the state looks quite intense, look for `Entities` inside the state and see if you can recognise what's going on in there and how it relates to what you are seeing on your board.