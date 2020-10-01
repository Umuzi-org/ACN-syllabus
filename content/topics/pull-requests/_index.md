---
_db_id: 468
content_type: topic
ready: true
title: Pull Requests
---

If any professional software development team, code review is very very important. It's part of the day-to-day life of a coder. The way a team generally works is something like this:

1. There are a bunch of coders and they each have a task to do
2. Each coder makes a new git branch for their task
3. When a coder thinks their work is worthy of getting pulled into the master branch, they make a thing called a pull request (PR)
4. The other coders on the team then look at the PR and give feedback if they think it's not quite there yet. Once a coder thinks that the PR is cool then they "approve" it
5. Once enough people have approved the PR then the code gets merged into master

## Some resources on how to make and use pull requests

- https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests

- https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request

This video is a nice demonstration. It gets good at 6min 30 seconds: https://www.youtube.com/watch?v=oFYyTZwMyAg.
If you watch it from the beginning there might be some confusing things.

1. Making a new branch DOES NOT make a copy of your entire repo
2. The dude in the video uses a tool balled bashit. It's pretty cool. An alternative is zsh.

Play around with it a little bit. Github doesn't bite.

**A possible confusion**

## What does this mean for you?

Since PRs are part of the day to day life of professional techies, we expect you to start practicing good habits now.

If you follow these simple guidelines you'll be good to go:

**1. if someone asks you fr a review, then review as soon as you can**

- Dont leave people waiting and then they wont leave you waiting
- If you think the code is good enough to be merged, then you need to click the "Approve" button. Github counts how many approvals a piece of code has, so this is a very important button to press.
- If you think that the code is not up to scratch, then leave some comments on the code and submit your review. Click the button that says "Request Changes".

**2. If someone has given you a review, act on it quickly**

You need other people to `Approve` of your code. If people are requesting changes then work through all the problems until it is ready for merge.

Once you have 2 `Approvals` you'll be able to click on the `merge` button on Github.

**3. If you need to merge some code into master**

Make a pull request. You can use Github's ui to request that specific people review your code. The people who should review it are the "reviewers" on your Tilde card.

Don't add people to your PR as ASSIGNEES. Add them as REVIEWERS. Lots of people get this wrong. Be precise.

If there are not enough reviewers available for whatever reason, make some noise! Ask a staff member that you need a different reviewer.

REMEMBER: It is YOUR JOB to get your stuff merged. Your reviewers and the staff are there to help you to do your job. But it's still YOUR JOB.

**How to make this efficient**

1. Smaller PRs are easier to review than bigger ones. You don't need to do an entire project all in one go. You can start getting feedback on a piece of work as you build another piece

2. Prioritise feedback over writing new stuff. There are lots of reasons for this. It basically just makes the team faster as a whole

3. If you have a choice between finishing a thing, or starting a new thing: finish. Always bias your actions towards moving things to complete.