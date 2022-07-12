---
title: Simple variometer - part 1
---

In this project you'll learn:

- How to make use of Expo APIs to get sensor data from your device
- How to make noises
- A little bit about aviation

## What is a vario

A variometer (or vario for short) is a flight instrument. They are pretty complicated and expensive. You can learn a little bit about them [here](https://en.wikipedia.org/wiki/Variometer) if you are interested.

Varios are used by all sorts of pilots. We'll be building a simple vario that would be suitable for use by noob paragliders without any money.

## How it will be used

The main function of the vario is to make different beeping noises depending on if the pilot is accelerating upwards or downwards. This is useful because the pilot will often be quite high up so there isn't an easy way for them to just sense if they are accelerating upwards or downwards. The beeping aims to give the pilot a 6th sense about their vertical acceleration.

Note:
- there should be different sounds depending on if the pilot is accelerating upwards or downwards
- the orientation of the phone matters: the phone will be placed with it's screen facing upwards
- it should be sensitive to 5m/s^2 (about 0.5G). Is if the pilot is accelerating upwards at a rate of at least 5m/s^2 then the vario should beep

## That's a whole lot of apis

One of the really cool things about Expo is that it supports many device apis. All the crazy stuff mentioned above can be accessed using regular JavaScript.

You'll need to make use of the following:

- https://docs.expo.dev/versions/v45.0.0/sdk/audio/
- https://docs.expo.dev/versions/v45.0.0/sdk/accelerometer/

You'll also need some noises. Take a look here:

https://freesound.org/search/?q=beep

## Next up

In part 2 of this project we'll be displaying some info on the screen. For now you can make use of visual components if it helps you with your debugging but your frontend wont be judged.

## Hints

This is going to take a bit of experimentation to get right. It would be useful to work on one thing at a time.

First, get the sounds to work. It might be useful to make two buttons, clicking the first button should make the "up" noise, and clicking the second button should play the "down" noise. Make sure that you can play the up noise three times by clicking the up button three times.

Once you have the sounds down then start figuring out the accelerometer. To do this you'll need to make use of the expo-go app on your phone.

When you start your app with`yarn start` then you will see a QR code come up in your terminal. Make sure that your phone and computer are connected to the same wifi network and then scan the QR code with your expo-go app.



The easiest way to do this is with `console.log` If you log the acceleration every half second or so then you should be able to access those logs and get an idea of how the movement of your phone changes the numbers.

