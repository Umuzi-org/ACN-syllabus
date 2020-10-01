---
_db_id: 436
content_type: topic
ready: true
title: How to download youtube videos from the terminal
---

If you have night-time data to use up, and you want to conserve your day-time data then it would be wise to download all your youtube videos at night.

You have 2 options here:

## Option 1: Use the download_all_youtube.py script in this repo

1. Install python3.7 or later.
2. install python development headers. Eg: `sudo apt-get install -y python3.7-dev` If you installed Python3.8 then `sudo apt-get install -y python3.8-dev`
3. If you know your way around virtualenvs, make one. Otherwise don't worry
4. Clone [this repo](https://github.com/Umuzi-org/tech-department) if you haven't yet and `cd` in
5. `pip3 install -r requirements.txt`
6. `python download_all_youtube.py`

This script will then look for all the youtube links in our syllabus and download the lot. If a video file is already present it wont download it again.

**IMPORTANT** by default this script will terminate after 1 hour. If you want to allow your downloads to run while you are sleeping you might want to increase this number. You can set the number of hours from the command line like so:

`python download_all_youtube.py --cutoff_after_n_hours=5`

The above command will download as much as it can for the next 5 hours.

## Option 2: Just use python your way :)

1. follow the steps from the above section in order to install all the goodies.
2. Open a python shell and type in the following (or save this to a script and run it):

```
import youtube_dl
with youtube_dl.YoutubeDL({}) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=RleN-6uMF04"])
```

The url there is any youtube video or playlist url. Nice eh?