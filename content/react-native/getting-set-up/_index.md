---
title: React Native setup
---

When writing ReactNative apps, it's pretty common to use a thing called Expo. It's basically a library that sits on top of ReactNative. It includes a bunch of APIs and components that you'll probably need; and it helps with things like deploying to app stores.

To see a full list of all the goodies included in Expo, you can take a look [here](https://docs.expo.dev/versions/latest/). Poke around a little bit. Think of the possibilities...

## Ok let's get started

Expo and ReactNative are pretty particular about what Node version is supported. And even if you have the right Node version installed then things can go haywire.

If you are running Linux and you installed Node with a Snap, go ahead and uninstall it. Really. It just falls over.

[Here is one error](https://stackoverflow.com/questions/71183795/expo-error-while-choosing-template-could-not-get-npm-url-for-package/71635470#71635470) you might come across if you installed Node in a non-standard way.

## Introducing NVM

NVM === Node Version Manager. It does a lot of cool stuff that we don't need to know about at this point. The main things to know are that:

1. It allows you to quickly and easily install the right version of Node in the right way
2. It allows you to make use of multiple versions of Node. So if you have lots of different Node projects on your computer, you can use different versions of Node for each of your projects if you wanted to.

Please install NVM and make sure you know how to:
- install the latest stable version of Node (do that now 😄 )
- install different Node versions
- switch between Node versions
- make use of `.nvmrc` files

You can find the NVM repo and documentation [here](https://github.com/nvm-sh/nvm)

At the time of writing (June 2022) the best version of Node to use was Node 16. To install Node 16 you would use the command `nvm install 16`. And to use that version of Node you would use the command `nvm use 16`.

## Install Expo

Now that you have the latest Node, you can install the Expo CLI. Read more [here](https://docs.expo.dev/get-started/installation/). You'll also want to install the Expo Go app on your phone if you can. It's not a requirement for this course, but it is kiff (there's that word again).

## Hello World

Now follow [this tutorial](https://docs.expo.dev/get-started/create-a-new-app/) to make a new app.

- Take note of the version of Node that is required and make use of NVM to run the right version.
- Make sure you can run it as a web app - you should be able to interact with the app in your browser
- Make sure you can edit your app. Can you get it to say "Hello World"?


## Check your understanding

The pages we linked to here have a lot of information. Double check that you can answer the following questions:

- What is the difference between a manages and a bare workflow?
- What workflow should you be using if you are new to ReactNative and Expo?
- Can you switch from a managed workflow to a bare workflow? Why would you want to do that?
