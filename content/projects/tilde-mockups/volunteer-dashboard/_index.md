---
_db_id: 536
available_flavours:
- javascript
- react
content_type: project
ready: true
submission_type: repo
title: Volunteer Pair-programming Dashboard
---

We have a growing number of volunteers getting involved with Umuzi in different ways. This is kiff. We have a bunch of awesome, experienced, senior developers and they want to help!

Right now there isn't a really easy way to co-ordinate our volunteers. Basically we have a staff member who acts as our offical volunteer wrangler. But it's a big job and it keeps getting bigger.

We want to set up a system so that volunteers can connect directly to individal students/recruits and share technical support and knowledge, without needing staff members to be involved. We need a process that is smooth, fun and meaningful.

And we really really believe that pair programming adds a tonne of value to everyone.

## Here is the idea

Volunteers need to be able to say what projects and languages they are keen on. For example Frank might be keen to help people with the Python version of the password checker project. And Bearded Ryan might be keen to help with the Javascript version.

Volunteers need to be able to see recruit project submissions for the projects that they are interested in.

Volunteers need to see previous code reviews for the projects, they also need to be able to add their own reviews.

Basically the reviewer will need to have access to relevent info and actions across a bunch of ccards that belong to different recruits.

Volunteers will also need to reach out to recruits to organise pair programming sessions (of course we can use RocketChat for that though) and they'll need to give us some feedback on how the sessions went and what was covered (and we can test this process with a simple google form). So this part initially needs no build.

## Prioritising pairing sessions

Then we also need to be able to help the volunteers make good decisions about who to help, and how to help:

### Getting people over the line

If a project has been marked as competent by recruits, but a staff member thinks it is not yet competent then that means:

- the recruit has already put in good effort so the pairing session will be fun and smooth
- there is a knowledge gap that needs to be filled, the recruit in question and the reviewers all dont know what competent looks like and could use some support.

In these cases it is good to have a pairing session where:

- the volunteer is the navigator
- the coder who submitted the work is the driver
- the reviewers are also present so they can see what went wrong. They can observe the session or help with "driving"

### People who are clearly struggling

If someone is working on a project and it keeps moving back and forth between the review and feedback columns in Tilde then it means something is going wrong.

Whether the reviewer is doing a bad job of explaining things. Or the person writing the code is misunderstanding things or not being careful. Maybe the project specification is confusing.

The volunteer can look at these and try and figure out what is going on and what the next move shoud be.

### Help the helpers

If someone is doing a great job at code review then it means that if we give them knowledge they'll spread it. Helping someone who suports others is the best way to help as many people as possible.

If someone is useless at code review then they should be at the bottom of the list beause the knowledge wont spread from this person.

so basically if there is a list of tasks for a volunteer to do, tasks that help helpful people should be higher in the list.

## Who sould be excluded from this

For now if someone is getting RED FLAG reviews then we would rather keep them away from the technical volunteers. These recruits will rather be coached by our wellness team.

## The procedure

1. Draw some pictures of what you want to build. Nothing fancy. Show your ideas to a few other recruits so that they can help you improve your design
2. Show your work to a staff member involved in mentorship and volunteering in order to get feeback and improve your work.
3. Build it in React