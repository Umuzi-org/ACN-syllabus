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
3. Add a new button to clear the selected image and selected sticker/emoji.
4. Make sure that you use `const` wherever appropriate. The tutorial uses `let` for everything, it's not always the best option. Most things are actually constant.

## Common problems

### Section: Sharing the image

If you get the error: `Uncaught (in promise) ReferenceError: Platform is not defined` then double check that your imports include `Platform`. Eg:

```
import { Image, StyleSheet, Text, TouchableOpacity, View , Platform} from 'react-native';
```

### Section: Handling platform differences

The tutorial makes use of a service called `anonomousfiles`. This service does go down from time to time. If you get an error that looks like this:

```
Access to fetch at 'https://api.anonymousfiles.io/' from origin 'http://localhost:19006' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
```

Then you probably did everything right. The anonomous files service is a web api that accepts an image and responds with a sharable url. If this isn't working then just hard-code a url for now.

Eg:

```
    if (Platform.OS === 'web') {
      // let remoteUri = await uploadToAnonymousFilesAsync(pickerResult.uri);
      const remoteUri = "https://nerdist.com/wp-content/uploads/2020/07/maxresdefault.jpg"
      setSelectedImage({ localUri: pickerResult.uri, remoteUri });
    } else {
      setSelectedImage({ localUri: pickerResult.uri, remoteUri: null });
    }
```

This is ok because the aim of this tutorial is just to understand how ReactNative works.

### Configuring a splash screen and app icon

If your splash screen doesn't show up in your web browser, don't panic, it's normal.

If you are using the Expo go app on your phone then you might notice that even after updating your splash screen, nothing changes in the app. You need to close Expo Go completely and re-open it. When you reload your app then the new splash screen will show up.

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

If you are using a physical device for a project then it would likely be necessary to mirror your screen. That is, get your phone's display to show up on your computer. There are many excellent tools that you can use for this:

https://fossbytes.com/android-screen-mirroring-apps-pc/
