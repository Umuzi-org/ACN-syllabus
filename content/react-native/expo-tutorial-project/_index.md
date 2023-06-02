---
_db_id: 785
content_type: project
flavours:
  - javascript
  - typescript
ready: true
submission_type: repo
title: Expo tutorial project
---

Alrighty, time to get your hands dirty.

Start off by doing [this tutorial](https://docs.expo.dev/tutorial/planning/). Make sure that you understand what you are doing, we'll be doing much harder stuff soon.

## More requirements

Once you have finished the basic tutorial, improve it by doing the following:

1. Include a `.nvmrc` file in your project submission. If you don't know what that means then go read about NVM.
2. Refactor your code so that each component is in a separate file.
3. Add a new button to clear the selected image and the selected emoji sticker.
4. Make sure that you use `const` wherever appropriate. The tutorial uses `let` for everything, it's not always the best option. Most things are actually constant.

## Common problems

### Configuring a splash screen and app icon

If your splash screen doesn't show up in your web browser, don't panic, it's normal.

If you are using the Expo go app on your phone then you might notice that even after updating your splash screen, nothing changes in the app. You need to close Expo Go completely and re-open it. When you reload your app then the new splash screen will show up.

### Emoji sticker not showing up on Chrome in Linux

If the select an emoji sticker doesn't show up on the web version in chrome, but it works on an Android or IOS simulator/device, try:

- clear your browser cookies, this works sometimes.
- use a different browser for testing the web version, Firefox seems to work fine.

## Video please

Going forward, we will require a video demo of all the apps you create during this course. If there is a multi-part project then we will always want to be able to access videos of any part of the project.

Please make sure that your video:

- demonstrates all functionality
- if a voice-over is needed then talk your talk

Include all video links on your README page.

### How to record a video

There are a few different ways:

You can install a screen-recorder app such as [Simple Screen Recorder](https://github.com/MaartenBaert/ssr) or [OBS](https://obsproject.com/). Once you have a recording you can upload it to Youtube. OBS does also allow you to stream straight to Youtube but you don't really need to get fancy here. Unless you want to, you wonderful nerd.

You can also make use of a service such as [StreamYard](https://streamyard.com/) to record straight to Youtube.

Make sure your video is marked as UNLISTED or PUBLIC, then link to the video in your README.

### Screen mirroring

If you are using a physical device for a project then it would likely be necessary to mirror your screen. That is, get your phone's display to show up on your computer. There are many excellent tools that you can use for this: [6 Methods To Mirror Android Screen To PC (No Root Apps) In 2022](https://fossbytes.com/android-screen-mirroring-apps-pc/)
