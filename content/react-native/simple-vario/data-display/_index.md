---
title: Simple variometer - data display
submission_type: continue_repo
flavours:
- javascript
- typescript
prerequisites:
  hard:
  - react-native/simple-vario/intro
from_repo: react-native/simple-vario/intro
ready: true
content_type: project
---

Now that you have made the vario beep, it's time to add a bit more functionality:

## Requirements

The pilot should be able to glance at their phone and quickly see information about their position, speed and heading. The display should be very easy to read and it should be high contrast because the pilot will likely be outside in the sun. The phone will be on the plot's lap so the display will need to be easy to read from that distance.

You should also get the display to show if the pilot is accelerating upwards or downwards. You can do this by displaying the acceleration in either red (for down) or green (for up).

Note that the pilot will be using both their hands to control their paraglider at all times (because, as mentioned, the pilot is a noob) and they will likely be wearing gloves. This means that the phone screen should remain on at all times. If the screen turns off then the pilot will need to let go of the paraglider controls and fiddle with their phone which can be dangerous.

## More apis

Here are some APIs that will help you with this.

https://docs.expo.dev/versions/v45.0.0/sdk/location/
https://docs.expo.dev/versions/v45.0.0/sdk/keep-awake/

## UI

Please don't make use of any component libraries at this point. Just use whatever Expo and ReactNative give you, and style those appropriately.

