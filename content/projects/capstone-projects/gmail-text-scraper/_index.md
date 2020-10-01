---
_db_id: 418
content_type: project
ready: true
submission_type: nosubmit
title: Gmail Text Scraper
---

## Who should do this?

Anyone interested in backend logic and scripting, and accessing external apis. This isn’t specific to one of our product teams, but the skills you prove here will be useful for the rest of your life.

## Spec

Write a script in Python or Node (or whatever really) that:

- Uses the gmail api to access all emails tagged with a specific tag for a specific person
- Reads the text inside each email and used regular expressions to extract useful data
- Takes all the data and saves it to a csv file

The data we are interested in seeing in the csv:

- Podcast title
- Episode title
- Duration
- Email data/time
- Link to episode

Lindelani/Sheena will send you a few emails that you can use

## Resources

https://developers.google.com/gmail/api/guides

First get the “quickstart” to run using your chosen language. Then make it work for your problem.

## Email sample Text

```
Far Away   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< this is a link
Episode: "Mjolnir" | Podcast: Star Wars Minute | 24m31s  <<<<<<<<< these are episode details

Daily conversational podcast that analyses the Star Wars films minute by minute. This episode is devoted to minute 114 of Revenge of the Sith, in which Yoda is mid battle with the Sith Lord. Although it's supposed to be a climactic point of the film, the quartet of reviewers here actually consider this dialogue-less sliver of a fight scene to be one of the most boring minutes of footage they have talked about. The discussion, though, is good natured and well structured, easily transcending the sub par material and adding intriguing tangents (24m31s)

True Crime
Episode: "The Murder Ballad Of Spade Cooley" | Podcast: Cocaine & Rhinestones | 60m16s

Country music history podcast hosted by the son of well known singer David Allan Coe. This episode comes with warnings for violent content, because it describes how musician Spade Cooley violently murdered his wife in 1961. But although this piece has that horrifying destination in mind throughout, the journey there through Cooley's musical career is worth the time. His role in popularising the country-jazz fusion known as "western swing" and the hustling he did to build a Hollywood profile in the 1940s is well covered (60m16s)

Hang Up
Episode: "Not A Phone Person" | Podcast: Anxious Machine | 24m56s

Moving, funny interview with a women who hated talking on the phone, yet has managed to maintain a long distance relationship over several decades. Andrea and Dave met in high school and then attended separate colleges. They are now married with three children but are still regularly parted for months at a time when Dave is deployed overseas as a naval officer. To avoid phone calls they have written thousands of letters, sent photographs, recorded cassettes and now have moved into video chats (24m56s)

This post is only for paying subscribers of The Listener, but it’s ok to forward every once in a while.

Caroline Crampton, Editor
Lindelani Mbatha, International Editor
Uri Bram, CEO [uri@thelistener.co]

Get The Listener's recommendations straight into your podcast app. Just copy this RSS feed and add it manually to your app:

https://www.listennotes.com/listen/the-listener-members-feed--oO1FZKwx6e/rss/

Further instructions here.

The Listener © 2020 – Unsubscribe

```