---
_db_id: 781
content_type: project
flavours:
- javascript
- typescript
- react
ready: true
submission_type: repo
title: Simple variometer
---

In this project you'll learn:

- How to make use of Expo APIs to get sensor data from your device
- How to make noises
- A little bit about aviation. As in flying

## What is a vario

A variometer (or vario for short) is a flight instrument. They are pretty complicated and expensive. You can learn a little bit about them [here](https://en.wikipedia.org/wiki/Variometer) if you are interested.

Varios are used by all sorts of pilots. We'll be building a very simple vario that would be suitable for use by noob paragliders without any money.

## How does a vario help a pilot?

The main function of the vario is to make different beeping noises depending on if the pilot is accelerating upwards or downwards. This is useful because the pilot will often be quite high up so there isn't an easy way for them to just sense if they are accelerating upwards or downwards, they don't have a frame of reverence. The vario's beeping aims to give the pilot a 6th sense about their vertical acceleration.

This is useful because the paragliding pilot needs to be able to find air that's rising so that they can catch some lift and stay airborne for longer. If a pilot cant find any lift then they have to land.

## System requirements

Please create a vario that does the following:

- it should have two different sounds, one sound should indicate that the pilot is accelerating upwards, and another sound should tell the pilot that they are accelerating downwards
- the vario should be sensitive to 5m/s^2 (about 0.5G). Is if the pilot is accelerating upwards or downwards at a rate of at least 5m/s^2 then the vario should make the appropriate sound
- It's common practice for the pilot to strap their phone to their leg above their knee, so the screen will be facing upwards
- there are currently no requirements about what will get displayed on the screen. So you can show whatever info you want. We'll be covering UI in the next part of this project.

## Resources

### Apis

One of the really cool things about Expo is that it supports many device apis. All the crazy stuff mentioned above can be accessed using regular JavaScript.

You'll need to make use of the following:

- https://docs.expo.dev/versions/v45.0.0/sdk/audio/
- https://docs.expo.dev/versions/v45.0.0/sdk/accelerometer/

### You'll also need some noises

Take a look here:

https://freesound.org/search/?q=beep

Find two different sounds you like and download them. You can just make a free account. If you want to get your noises from somewhere else then that's totally fine as well.

## If I were you...

This is going to take a bit of experimentation to get right. It would be useful to work on one thing at a time. And then once you have figured out each piece, bring it all together.

### Noises

First, get the sounds to work. It might be useful to make two buttons, clicking the first button should make the "up" noise, and clicking the second button should play the "down" noise. Make sure that you can play the up noise multiple times by clicking the up button multiple times.

### Acceleration

Once you have the sounds down then start figuring out the accelerometer. To do this you'll need to make use of the expo-go app on your phone.

When you start your app with`yarn start` then you will see a QR code come up in your terminal. Make sure that your phone and computer are connected to the same wifi network and then scan the QR code with your expo-go app. When you do this then expo will open a page in your web browser, you can use this page to control the app that is running on your phone.

Open up the devtools (F12 in chrome) and make sur you can see the console.

Now update your code so that whenever you get a reading from the accelerator, you console log it. You'll be able to wave your phone around and see how the acceleration data changes by watching the console.

### Bringing it together

Once you understand how acceleration works, you'll just need to trigger your noises at the right time. That's it.