---
_db_id: 606
content_type: project
flavours:
- none
prerequisites:
  hard:
  - environment-setup
  - topics/github/intro
ready: true
submission_type: repo
title: 'Tilde project tutorial: How Repo projects work'
---

There are a few kinds of projects you can do and they can be submitted in different ways. In this tutorial, you'll see how to get a repository project to complete.

## Start the project

If you have not yet clicked the "start project" button for this card, do so now. You'll see the card move to In Progress.

It might take a few seconds to move. The reason for this is that a whole lot of things are happening in the background.

- A Github repository is created for you to work on. This is a private repository, so only certain people can see it
- The `main` branch is protected. We'll talk more about what this means a little bit later
- You are added as a "collaborator" on the repo so you have access

Now explore the card. Click on the Details button and see what's there.

## FREQUENTLY ASKED QUESTIONS

### I can't access my repo!

When you are added to a repository as a collaborator, then Github sends you an invitation via personal email. Your GitHub account is associated with your email address. You must monitor that email address.

Also, note that you will get invitations to collaborate on other people's repositories from time to time. You need to accept these invitations as they expire. They are for review purposes.

### Why can't I just give you a link to my work?

I'm going to tell you a little secret. Working with junior developers is annoying. Generally, when a junior developer gets their first job and has to interact with a serious code base and a team of mid and senior developers, they just bump their heads on Git for weeks. Even if they know how to write code, they don't know how to write code on a team. They don't know how to be useful.

We aim to create useful junior developers. Not annoying junior developers. When you get your first job, we want you to keep it. If you get fired because you can't use git then that would be pretty sad.

Generally, when you work on a serious project with a serious team, you'll need to incorporate your code into their repository. So we want you to start practising now.

I admit it might feel a little weird at first, but you'll get the hang of it :)

### Why can't I push to the main branch?

We "protect" the main branch to stop you from pushing to it. The reason we do this is that on a professional developer team, you won't be pushing straight to master. You'll be making your branches and getting those reviewed and merged into the main branch by interacting with your teammates. This keeps the main branch clean and shiny.

## Instructions

If you look at the project details you'll see that a repository has been created for you. Please click on the link and visit the repository page on Github.

For now, you can interact with Github using the user interface. You don't need to worry about using git from the command line. Not just yet anyway. In future projects, you'll become a Git command-line ninja. For now, we just need you to see how Tilde and Github play together.

### Super important note about adding reviewers to your Pull Request

Whenever you add a person to a pull request then they get an email. So if you randomly add absolutely everyone to your Pull Request then absolutely everyone gets an email.

That is called Spam. Nobody likes spam. Even Mother Theresa. So we, and Mother Theresa would appreciate it if you didn't spam people.

Who should you add to your PR as reviewers?  For now, don't add anyone.

Generally, it is best practice to only add people to your Pull Request if you know who they are and know that they are the correct people to perform a review.

**I repeat: For now you should not add any reviewers to any of your Pull Requests because we DISLIKE SPAMMERS A LOT.**

### 1. Make a file

Open up your text editor of choice and create a markdown file. This is a plain text file. Name it `important.md`.

Inside the text file please create a list of everyone you should be adding to your Pull Request as reviewers and why.

*Hint: The list should be empty. And the reasons are explained in this document if you scroll up a little.*

#### What is markdown?

It's a seriously useful way of writing text files. A lot of software projects use it for documentation. It's built into Github as well.

This website you are looking at is generated from markdown files. Now is a good time to get used to it.

Here are some links :)

- https://www.ultraedit.com/company/blog/community/what-is-markdown-why-use-it.html
- https://www.markdownguide.org/cheat-sheet/

To create a markdown file just create a file with the extension `.md`. That's it.

If you are using Acode on your android device, you can press the "play" button in the editor and your markdown will get rendered as a website.

If you are running VSCode you can right-click on a markdown file and select "open preview" to see what your work looks like.

If anything up until this point doesn't make sense please ask for help! Our staff are dedicated to setting you up for success.

### 2. Make a PR (Pull Request)

Now upload your file to Github and create a new branch.

Make a Pull Request to merge your stuff into the main branch. You'll notice that you can't merge it though. This is because the main branch is protected. You need to get a little help.

Now don't add any reviewers. Because it will make Mother Theresa sad.

#### Video Tutorial for parts 1 & 2 below

{{% youtube KyDxI7gOQbo %}}

### 3. Get your Pull Request merged

To get your stuff merged into master, you need 2 people to "Approve" your Pull Request. Don't add people to your Pull Request on Github. We'll handle it via Tilde.

Read more about Pull Request approvals here: https://docs.github.com/en/enterprise/2.13/user/articles/approving-a-pull-request-with-required-reviews

Remember that it is _YOUR JOB_ to get _YOUR CONTRIBUTIONS_ merged. If you need someone to review your stuff then poke them and nag them until it gets done. And of course, if someone asks you to review their stuff, do your best to review it quickly, accurately and completely.

If someone requests changes on your Pull Request then you'll need to act on those as quickly as possible. Always try to learn from feedback quickly. Otherwise, you'll just make repetitive mistakes.

If everyone does their best to review stuff quickly and respond quickly then nobody will be left waiting around. Rapid feedback is a very good skill to practice. Rapid feedback is one thing that makes a developer team rock.

If there aren't enough collaborators on your repo to get your stuff merged, please make a noise. A staff member will help out.

**Common problems:**

Sometimes people struggle to get their PRs merged because there aren't enough people on the repo, or because the people who are meant to review your work aren't moving quickly enough.

Please remember that it is **YOUR RESPONSIBILITY** to get stuff merged. There are people around who you need to work with to achieve your goals, but you need to remember that getting stuff merged is **YOUR JOB**.

1. If you don't have enough people on your repo so there is nobody to review your work: Ask a staff member to assign some reviewers to your work
2. Nag your reviewers to review your work. Be as annoying as you need to be. It's on you to chase reviews
3. If your reviewers are being too slow, please tell a staff member.

On the flip side, if someone asks you to review their work then treat that as your highest priority task. Do it as soon as possible. Get into the habit of supporting the people around you by giving them fast and accurate feedback. Then when you get your first serious dev job, your team will love you.

### 4. Move your card to the REVIEW column (AFTER YOUR PR IS MERGED! NOT BEFORE!)

**NOTE:** If your PR is not merged you will be marked as Not Yet Competent or Red Flag!!

Now that your main branch is totally up to date with all the things, you can ask for a final review by clicking on the "Request Review" button on your Tilde board.

This tells your peers and staff that you think your main branch is up to date and complete, and that you think your work is Competent or Excellent.

**DON'T DO THIS IF:**

- Your stuff isn't merged.
- You didn't complete the project, for example, if you skipped part 4 of a 5 part exercise then make a PR to complete your work first.

### 5. Double-check that your main branch is up to date!

If your main branch is empty at this point then cancel your review request, get your work merged, then put your card back into the review column.
