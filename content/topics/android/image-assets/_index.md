---
_db_id: 98
content_type: topic
ready: true
title: Working with image assets
---

In every Android project there is a drawables folder. This folder is where image assets are uploaded to. The images in this folder are packaged with the
apk when it is built. The android app can access these images offline and at a much higher speed.

# Adding an image to an Android application

[Here](https://www.youtube.com/watch?v=Ab7U7lqikfU) is a video with a simple example of adding an image to the `drawable` folder and then displaying it in an imageview.

# Supporting the various pixel densities

As mentioned above, accounting for multiple screen resolutions plays a role in both `performance` and `overall user experience`.
Luckily though, Android has a simple way to handle this.

You can read more about it in the [documentation](https://developer.android.com/training/multiscreen/screendensities).

# Important Note

The size and quantity of the image assets directly affects the size of the apk file.

When adding image assets to the drawable folder, the names of the images are not allowed to contain `capital letters` or `spaces` between the words.

Example: Adding the following files will provide the following results

# Allowed image name examples

cars.jpg
toyota_corolla.png

# Not-allowed image names

Cars.png
Toyotal Corolla.png
Cars!.jpg