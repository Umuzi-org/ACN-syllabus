---
_db_id: 535
available_flavours:
- javascript
- react
content_type: project
ready: true
submission_type: repo
title: Public Profile
---

One exciting feature we want to build is a public profile page that recruits can use as a way to show off what they have learned with Tilde. We keep track of what people are learning and things like that on their boards.

Build a public profile page that can act as a kind of portfolio for a recruit. This page can be sent out to potential employers and make the job hunt easier.

You need to come up with a cool way of displaying the kinds of data we currently have access to, as well as some future stuff.

## What data do we currently keep?

Right now Tilde basically tracks cards. Cards have different tags associated with them.
By looking at the tags of cards and their statuses we can see how far people are with different areas of course work.

For example: Maybe a recruit has done 8/10 of the tdd cards on their board. And 1/10 of their OOP projects.

We also keep track of code reviews. So Another thing we can display is comments about excellent work and perhaps competent work.

Eg: let's say Shindi reviews someone's api development code, marks it as excellent and says something wonderful. It would be very cool to have that show up on a the recruit's public profile page.

We also keep track of what courses people registered for and when. A recruit can actually do multiple courses with us. For example one could do a full stack web dev course, then a course in React.

One thing we are also quite excited about is supporting our Alumni. Once someone graduates from their course with us, we want to keep offering them value through giving them access to courses on our network. And their public profiles should get more awesome over time and show what they have been working on.

## What data do we currenly not keep

There is still a lot to build and track. So you have a bit of freedom here.

What else would you like to see here?

What else do you think employers would want to see?

Here are a few ideas:

- a profile picture
- a "Hire me" button
- employment history
- testimonials from employers and staff
- the recruit's own words about who they are, what are their plans, etc. Take a look at this for inspiration: {{% contentlink path="topics/work/creating-a-statement" %}}
- Trophies and badges. One day we would like to build in some gamification features. For example a person might get a badge to say they are the fastest high quality code reviewer for the week
- You can use flair from different communities you are apart of. For example:

---

## <a href="https://stackoverflow.com/users/742082/sheena"><img src="https://stackoverflow.com/users/flair/742082.png" width="208" height="58" alt="profile for Sheena at Stack Overflow, Q&amp;A for professional and enthusiast programmers" title="profile for Sheena at Stack Overflow, Q&amp;A for professional and enthusiast programmers"></a>

## Your task

1. Draw some pictures of what you want to build. Nothing fancy. Show your ideas to a few other recruits so that they can help you improve your design
2. Show your work to @liezel.vorster on rocketchat. She is very involved in helping recruits get their portfolios up to scratch and getting things done
3. Build it in React