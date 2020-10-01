---
_db_id: 534
available_flavours:
- javascript
- react
content_type: project
ready: true
submission_type: repo
title: Code Review Performance Dashboard mockup
---

As you should know by now, code review is the cornerstone of a successful dev team.

Rapid feedback cycles lead to rapid learning and rapid adaptation. Effective code review is GOLDEN! It keeps everyone's brains fed :)

But even though it is increadibly important and it should be a high priority for devs, code review is often left until the last possible moment.

There are a few reasons for this. One reason is that recruits/students just dont know what "good" looks like. And even if they knew what good looked like, they dont get easy clear access to metrics about their own performance or the performance of their group. They don't know what we are even measuring or why.

So what we need is a dashboard. Colours, dials, graphs... all that good stuff.

A recruit needs to be able to look at their code review dashboard and clearly see if they are doing well or badly, and they need to see how they are doing in comparison to their group.

## The data

Basically we keep track of:

1. Cards and their statusess. and who is assigned as a reviewer
2. If a card is in the review column, we can see how long it has been chilling there by looking at when the review was requested
3. We can see what reviews were done when and by who
4. We also keep track of how many times a staff member disagrees with a review made by a recruit.

## And what does good look like?

We need to be able to show cool visuals that tell a person if they are doing a good job or not.

Here are a few guidelines on what good looks like:

- Generally, the more reviews a person does, the better
- If a single card has lots of reviews by a single person then it means that the quality of the review might be low. It could be that
  - the reviewer is trying to trying to cheat the system or
  - they didn't do a thorough review the last time so there is some back and forth card movements. The better the review the fewer reviews are needed
- The faster someone reviews code the better. So if someone requests a review and then the card just chills in the review column getting ignored for ages then that's bad

On top of those basics, it's good to know that staff members have the final say about if a project is competent (or excellent) or not. So another thing we keep track of is disagreements.
Eg: if a reviewer says that some code is excellent, then a staff member says it's a red flag, then it means that the reviewer did a really bad job. Really seriously bad.

So we count "disagreements" and keep track of when they happen, and on what cards/projects.

Why do "disagreement"s happen? There are 2 main reasons:

- junior coders make mistakes because they are still learning! So we expect some disagreements. But as the coder learns, they'll do a better job.
- some people rush through code reviews and do a bad job. Or just always mark their friends as competent and other such nonesense. These people need to know that that's not how life works.

## And the other side of the review coin

If a recruit gets feedback on one of their projects, it's their job to react to it quickly and sort things out. A good coder works to get things finished! Responding to feedback as quickly as possible means that learnings can be better applied to future projects.

People who delay on learning from feedback tend to make the same mistakes over and over again and just end up annoying the reviewers.

Acting quickly when someone gives you a thoughtful review is really a good thing to do.

So the things that are worth displaying here are:

1. How quickly a card moves from "review feedback" back into review
2. How many times a card moves back and forward between the "in review" and "review feedback" columns. If it's just getting kicked back and forth it might be the coder who is at fault

## Your task

1. Draw out what you would want to build before you build anything! Show it to at least 3 users (recruits) and get their feedack on your design.
2. build your mockup in React