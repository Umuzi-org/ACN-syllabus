---
_db_id: 642
content_type: topic
tags:
- sql
- postgres
title: Getting ready to write some SQL
---

Before we can get into any project work it would be good to get a database up and running that you can play with. There are 2 options here:

## Option 1: Use an online service

[ElephantSQL](https://www.elephantsql.com/) has a free service where you can spin up a teeny weeny database server for free.

Just sign up for the free plan.

You'll be asked what region you want to run your db in. Basically the way we make this choice is by choosing the data center that's closest to where you are. This is probably Google compute engine Europe west 2. 

Once you've confirmed everything and you've created your instance, you can click on the name of your instance to see a whole lot of options. Click on "Browser". You will now be able to see a text box where you can edit and execute some sql queries.

Now you can execute the world's most boring query to make sure things actually work `select 1;`.

## Option 2: Install Postgres on your computer

For this option, the best thing is really to use Docker. This is hard mode so if you are currently taking part in one of our selection bootcamps please go with option 1.

To learn how to use Docker to run a Postgres instance please follow these instructions:

{{< contentlink path="docker/intro-to-docker" >}}

If you are on Windows and are having trouble with Docker Desktop, please view this topic:

{{< contentlink path="docker/docker-desktop-troubleshooting" >}}