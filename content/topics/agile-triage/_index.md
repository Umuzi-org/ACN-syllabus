---
_db_id: 377
content_type: topic
ready: true
title: Agile Triage
---

From this day forward you'll be expected to spend your workdays behaving like a professional on an agile team. Now we know you aren't an expert in agile just yet so what follows below is a little description of what is expected and why.

To start off with, here is a summary of how you should use your board to choose your next action. We'll go into detail on each of these points in the rest of this article.

## Steps to Success

1. Look at your "Review" column. Are there any cards in there that need a review from you? If yes, your first task is to review those cards. Try to start with cards that havent had feedback yet. And try get the easy stuff done first.
2. Look at Github. Does anyone need a review on a Pull Request? Do all the reviews anyone has asked you for.
3. Look at your "Review Feedback" column. Do you have any cards there that need to be fixed up? If yes, start from the top.
4. If you have any PRs and people have given you feedback, your next step is to address that feedback. When addressing your own feedback always try to work on the simplest project first.
5. Look at your "In Progress" column. As usual, start from the top. Finish all the things before moving on.
6. Look at your Backlog. What would you like to work on next? Move one of the available cards over to your "In Progress" column

So basically, you should work from right to left. The closer a card is to "complete" the more important it is. Easy enough.

## But why???

There are a few reasons for this:

First let's talk about the most obvious one. You are here to become a professional developer, and professional developers need to be able to read code and communicate about code. I mean...

<iframe src="https://giphy.com/embed/cjuEzuATSjW6BfwV2L" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/RobertEBlackmon-reactions-duh-obviously-cjuEzuATSjW6BfwV2L">via GIPHY</a></p>

It's actually a huge part of the job. Most of you will end up working on a team of developers and if the team can't communicate about the team's code then the team should probably all go work at MacDonalds or something and communicate about burger flipping instead. Yeah, it's that serious.

The second reason is a bit more subtle. And pretty cool in my opinion. It's basically the secret sauce to high functioning teams. Ok ok... one of the secret sauces, there are a few. And if you take these philosophies and apply them anywhere in your life things will just go better for you.

Alright, are you ready? A little curious?

Basically if you have a team of developers working on a thing they generally want success right? I mean, they want a working product. They want to deliver real world solutions. Again, this is obvious. So if you have a team of devs and they are all writing code then that's great and all, but if nothing ever gets completed they aren't creating any value in the world. They might as well be reading Harry Potter fan fiction instead of wasting their client's money.

To paraphrase:

**Your code is useless until it is complete. Your team's code is useless until it is complete.**

So your **TOP PRIORITY** is to get code to be complete!

Starting new things can be more fun. But that's just like running on a hamster wheel. Professionals complete their work.

So don't be a hamster, ok. You are not here to be adorable!

<iframe src="https://giphy.com/embed/jTkDNgIVpwMhfgk0uC" width="480" height="472" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/tiktok-hamster-wheel-spinning-jTkDNgIVpwMhfgk0uC">via GIPHY</a></p>

The idea of actually finishing your work instead of just starting a million useless things seems sort of obvious, doesn't it? But it hasn't always been so clear. There is a special flavour of agile called kanban that talks a lot about how wasteful it is to have stuff in progress instead of complete.

You can read more about kanban [here](https://kanbanize.com/kanban-resources/getting-started/what-is-kanban). Kanban is basically what you'll be doing for the duration of your learning journey.

**But how do we move cards from "Review" to "Complete"?**

Good question young Ravenclaw. The answer is: teamwork.

You'll notice that there is an "Add review" button on certain cards. You can click on that and give your opinion on the project. Basically you can say a project has one of 4 statuses. Whatever you say there cannot be edited and it will be visible to the person you are reviewing as well as staff members. So be careful.

If you review a project and say that it is "Not Yet Competent" or "RED FLAG" then the card will move backwards to the "Review Feedback" column so that any problems can be fixed. We'll talk more about that a bit later.

If you review a project and say it is "Competent" or "Excellent" then the card will actually stay still. If you see a Card in the "review" column that has already been reviewed by someone else, then add your review as well. In industry every piece of code is generally reviewed by a bunch of people.

Once there are enough positive reviews on a Project Card then a staff member will add a review. Now focus:

**THIS IS A TEST**

If you give a project a positive review ("competent" or "excellent"), and then a staff member gives it a negative review ("red flag" or "not yet competent") then this means one of two things:

- maybe you don't know what competent looks like, maybe you don't have the skills. Or
- maybe you are not a team player and don't care about giving good feedback to your peers

You will be measured on this stuff! So do a good job!

If you feel that you don't yet have the skills to give a review to a project then do what you can to level up before doing the review. Don't make guesses and don't take shortcuts. And on our side we will do our best to only assign you to projects that you should be ready to review.

### Getting code into the Review column

We need to get project cards to move into the Review column so that they can be marked as Complete.

On the frontend you'll see there is a "Request Review" button that you can use to put your own cards there. But when should this button be pressed? If you just press it without doing the right things first then you'll just get a "Not yet competent" or "Red flag" review and that'll just suck.

So the fist thing to do is get your code ready for the final review. Get it to a point where you personally believe that your code is at least competent.

How? By following the project instructions of course. But there is another part to it as well.

When working on a professional dev team one generally doesn't commit directly to the `master` branch. A dev will create a seperate branch, do some work there, and then make a PR (Pull Request). A PR basically asks the question:
"Will merging my branch into the master branch make the master branch better?". If enough people approve your PR then the answer is yes. Then the code is merged.

**Please Note** if your project code has not been merged into the master branch then putting it into the Review column will just be a waste of time. This is also a test and it will be recorded. Professionals know how to use PRs. If your master branch is empty then you have more work to do.

In order to get your code into your master branch you need to get your PR approved so that your code can be merged. If 2 of your peers approve your PR it can get merged.

This means that your **second highest** priority is giving people feedback on their PRs so that stuff can get merged. You will prioritise your peers, and your peers will prioritise you.

Of course by prioritising **FEEDBACK FIRST** we help things get closed as fast as possible, but it also helps you to learn as fast as possible! If you make a mistake or get something right then it's good to know where you stand.

By always setting up your peers for success, you will be set up for success.

## What does good feedback look like?

Code review is a tricky thing. Please remember that people have feelings. The first rule of good review is:

**Don't be an A55h0L3!**

Seriously. Be kind to each other. You are all here to grow. And you'll grow by helping each other. Code review can be frustrating and emotionally difficlt for a lot of people. If you ever start feeling annoyed try to be curious instead. It's a weird hack but it works for some people.

The second rule is:

**Minimise back and forth**

Do this by reviewing as much of the code as you can. Don't just stop at the first problem, talk about all the problems you see. That way when they ask for another review it will closer to Complete.

The third rule of a good review is:

**Help them to understand!**

You wont be doing anyone any favors by doing their homework for them. Sometimes cheating the system seems like the easy way out but in the long run it's pretty dumb. Here are some consequences to taking part in cheating:

- Your buddy will just struggle more on their next project
- Your buddy might just get fired from their very first job
- Cheating on your work is also of course a serious offence and if anyone gets caught then there are consequences. And it sucks for everyone. So just dont.

If there is someone who is struggling and you feel like they need a staff member to come help them, please reach out. The whole point of this organisation is to help people grow! And that means everytone should understand what they are doing.

## Enough squishy stuff! What else can you tell me?

Of course you aren't just here to help others with their work, you are also here to build your own stuff. So resist your inner-hamster - take on one project at a time. Trust your peers to help move your cards to Complete. If you ask for help or for a review and you feel ignored, ask again! As a professional you need to pursue success like it really matters to you. That sometimes means annoying your co-workers.

That's it really.

## Extra reading

Our methods are based heavily on Kanban and (weirly enough) lean manufacturing methods. Check this out, it might chnge how you think: [Waste in software development](https://www.solutionsiq.com/resource/blog-post/waste-in-software-development/)

Then if you want to know about how git really supports teamwork then you can learn about the [git feature branching](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) (you'll learn about this later) stratergy.