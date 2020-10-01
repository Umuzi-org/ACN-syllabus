---
_db_id: 288
available_flavours:
- none
content_type: project
prerequisites:
  hard:
  - topics/github/intro
  - topics/bootcamp/bash-for-bootcamp
  - topics/git
  soft: []
ready: true
story_points: 1
submission_type: link
tags:
- git
title: Git Basic Exercises
---

## Introduction

This little exercise will take you through the basic git mechanisms you need to know about in order to be productive. By the end of this exercise you'll be able to create and manage your own git repos.

**IMPORTANT** Make sure you go through the prerequisites listed above. Otherwise you'll be clueless!

## Skillz you'll learn

By the end of this you are expected to know:

- How to set up a repository on Github
- How to make commits
- How to make branches and switch between them
- How to use gitignore files
- How to merge branches
- How to overcome merge conflicts

When you are finished with these excercises come re-read this section and make sure you know what all these things mean.

## Creating and managing your own repo

Note: you can do all of this stuff from the command line! You should be using linux. Open up a terminal and do the following:

### Your initial commit

1. Create a directory named `git-basic-exercises`
2. cd into your new directory
3. look at what's inside using `ls -a`. It should be empty
4. initialize your git repo using `git init`. Then check `ls -a` again. Can you spot the difference?
5. check the status of your repo by typing `git status`
6. type in `touch README.md`. This creates a new blank file. Then check `ls -a` and `git status` again.
7. type in `git log`. The output should make sense to you
8. Now add your readme file to your git staging area. Hint: use the `git add` command
9. Then check your `git status` again. Can you see the difference?
10. Try to unstage your file and check your `git status` again
11. Ok, now for your first commit: Make sure your readme file is staged then type in `git commit -m "initial commit"`
    Your output should be something like this:

```
 [master (root-commit) 2103b64] initial commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
```

12. type in `git log` isn't that nice? press `q` to exit

### more commits!

1. type in `nano README.md`. This will open up a text editor. Type in some stuff and then press `ctrl x` to exit. Then `y` then `enter`. This will save your changes
2. type in `cat README.md`. This will print your file to the console
3. take a look at the `git stats` again and make sure you understand it
4. commit your changes to your repo. Your commit should have the message `"second commit"`
5. make some more changes to your readme and make a `"third commit"`

### check this out

1. type in `git log`. You should see all your commits there. It should look something like this:

```
commit a57585d3cf93e64c04e62e58dfe8151d191503cf (HEAD -> master)
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:07:40 2019 +0200

    third commit

commit a48c005c761902395cf9a50f13ddbffeee4f5537
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:07:12 2019 +0200

    second commit

commit 2103b6418ecf4f70effabb639cfad6ac9d57c089
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 14:43:51 2019 +0200

    initial commit
```

Each commit has a "hash". That's the weird alphanumeric string thingy, eg `2103b6418ecf4f70effabb639cfad6ac9d57c089`.

2. Copy the commit hash for your second commit. You can just select it with your mouse and right click and choose 'copy'
3. press q to exit the log view. You should now be back at the terminal
4. type in `git checkout` and then paste in the commit hash and press enter
5. `cat README.md` It's like going back in time...
6. `git checkout master`
7. `cat README.md` Now we are up to date

You can jump to any commit using `git checkout`. You can checkout a branch, a commit hash, or a tag. We didn't explore tags here.

When you checkout a branch, you checkout the latest commit on that branch.

Why would you want to do this? Well, it's very useful to be able to go back and look at an old version of your code. Maybe you made a mistake and there is a bug and you want to go back to when there was no bug.

### branching

The real power of git is in branching. Branching is what allows big teams of developers to work on the same code base. Basiclly differnt developers make branches for different things and then those branches can be merged together into one mighty application.

**Please Note** At some point during this excercise you'll get an error message! It'll say something about a merge conflict. DONT PANIC! Merge conflicts are a fact of life and you'll need to figure out how to fix it. (This)[https://opensource.com/article/20/4/git-merge-conflict] should help.

Let's explore branching a little bit.

1. `git branch` This lists all your branches. Git makes a branch named `master` by default
2. Now create a new branch called `milkshake-flavours`. git is not too restrictive when it comes to naming our branches. It's generally best to choose a name that has something to do with what the branch is for. Our branch is about milkshakes
3. type in `git branch`. Notice the little `*`.
4. check out your new branch. type in `git branch` again and look at the `*`. Can you see what it means? Try switching between the different branches and see how hings change.
5. Make sure you are on the `milkshake-flavours` branch then type in `nano milkshakes.md` and write fill in a few flavours. Mmmm. save and exit
6. what does `git status` tell you?
7. commit your new file with the message `"added initial flavours"`
8. take a look at your git log again. It should make sense
9. checkout your master branch. It'll look a little different. Can you see why?
10. from your master branch, create a new branch called `history` and check it out. If you say `git log` it should only have three commits. And if you use `git branch` you should see 3 branches! **This is important!**
11. type in `history > history.txt`. Can you guess what it does?
12. commit your changes with the message `"added history"`. Take a look at the `git log`
13. now checkout your milkshake branch and look at the `git log`. it should have your three master commits and your one milkshake commit
14. make some arbitrary changes to the readme file and make a new commit with the message `"random readme changes"`
15. checkout `history` again and `cat README.md`
16. now on your history branch do the following:

```
rm README.md
echo "booya" > README.md
```

You should know what these lines do.

17. commit your changes. Use the commit message `"rewrote readme"`
18. checkout master again

### Just make sure we are still on track

If you have followed along up until this point then your branches should look like this:

Type in:

```
git checkout master
ls
```

this outputs:

```
README.md
```

Check the log:

```
git log
```

this outputs something like:

```
commit a57585d3cf93e64c04e62e58dfe8151d191503cf (HEAD -> master)
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:07:40 2019 +0200

    third commit

commit a48c005c761902395cf9a50f13ddbffeee4f5537
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:07:12 2019 +0200

    second commit

commit 2103b6418ecf4f70effabb639cfad6ac9d57c089
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 14:43:51 2019 +0200

    initial commit
```

Now lets look at milkshake-flavours:

```
git checkout milkshake-flavours
ls
```

You will see two files:

```
milkshakes.md  README.md
```

And `git log` will look like:

```
commit d2559d9758f3ec0f7928f6cbef705c6fa9679edf (HEAD -> milkshake-flavours)
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:25:07 2019 +0200

    added initial flavours

commit a57585d3cf93e64c04e62e58dfe8151d191503cf (master)
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:07:40 2019 +0200

    third commit

commit a48c005c761902395cf9a50f13ddbffeee4f5537
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:07:12 2019 +0200

    second commit

commit 2103b6418ecf4f70effabb639cfad6ac9d57c089
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 14:43:51 2019 +0200

    initial commit
```

Finally history:

```
git checkout history
ls
```

there should be two files:

```
history.txt  README.md
```

and `git log` outputs

```
commit 34025ac2b26accb7c5c18ec048a4982d3bae8909 (HEAD -> history)
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:38:05 2019 +0200

    rewrote readme

commit b9e3c50fb65c7b2df0f09b921a15a7fc146e0bfb
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:36:04 2019 +0200

    added history

commit a57585d3cf93e64c04e62e58dfe8151d191503cf (master)
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:07:40 2019 +0200

    third commit

commit a48c005c761902395cf9a50f13ddbffeee4f5537
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:07:12 2019 +0200

    second commit

commit 2103b6418ecf4f70effabb639cfad6ac9d57c089
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 14:43:51 2019 +0200

    initial commit
```

### merging

Now we want to get the master up to date with all out changes. Let's start with the milkshake branch

1. merge milkshake-flavours into master

```
git checkout master
git merge milkshake-flavours
```

2. Use `ls` and `git log` to see what this did
3. merge history into master
4. Use `ls` and `git log` to see what this did
   As you can see a whole lot of changes have been made to the master branch
5. Now lets take a look at the other branches

```
git checkout history
git log
...
git checkout milkshake-flavours
git log
```

These branches were not effected by the merge!

In general if we want to merge branch X into branch Y:

```
git checkout Y
git merge X
```

This adds a commit to branch Y and doesn't change branch X

6. merge the master branch into `history`. Use `git log` to see whats up.
7. checkout master again. git log again. Can you spot any differences?

### GitHub

1. Go to Github.com (using your browser of choice) and create a new public repository using the user interface. Name it `git-basic-exercises`

2. You will see a bunch of weird looking things. There is a section entitled "…or push an existing repository from the command line". We have an existing repository and a command line. So this seems appropriate. Copy the commands from there and paste them into your terminal. this will push your changes to github.

3. Refresh your browser. Cool eh? The url you are looking at should look like this: https://github.com/[YOUR_USERNAME]/git-basic-exercises

Now you should see a little dropdown box on github that says "Branch: master". Click there. your other branches aren't available.

4. Push your other branches to github. We want all branches to be listed

**A cool trick we use all the time: the network page!**:

If your repo is available at https://github.com/[YOUR_USERNAME]/git-basic-exercises then take a look at https://github.com/[YOUR_USERNAME]/git-basic-exercises/network. I just added `/network` on the end there. You'll be able to see all the individual commits and all the different branches you've made and how they relate to each other.

Go look at your network page. each of the dots there represent commits you made. Can you see how they relate to what you did? Can you see the individual branches?

### Pulling and remotes

1. You should still be inside the `git-basic-exercises` directory. Let's get out of there. `cd ../`
2. Now let's clone a repo. point your browser here: https://github.com/Umuzi-org/tech-department
3. Now there is a friendly green button that says "Clone or download". Click on it.
4. You will see a url come up. Copy it. You will need to paste it into the terminal in a moment
5. In your terminal type in `git clone $THE_URL_YOU_JUST_COPIED`. It should look something like this: `git clone https://github.com/Umuzi-org/tech-department`
6. `cd` into the tech-department directory that was just created
7. explore a little using `git branch` and `git log`
8. type in `git branch -a`. This shows the remote branches
9. try to checkout the branch called `project/git-basic-exercises` on your local computer. You can do it, you'll need to figure out how
10. type in `git remote -v`

### Multiple Repos

1. While still in your newly created branch `project/git-basic-exercises` use `git log` to see the history.
2. From your new branch called `project/git-basic-exercises`navigate back to your `git-basic-exercises` repo, use `git log` again to see the difference.
3. Let's go back to our home directory `cd` and make a new folder `mkdir this-will-be-another-repo`
4. cd into this folder now use `git init` to initilise a new git repo here, you should get a message in terminal that says 'Initialized empty Git repository in /home/\$specific-path/this-will-be-another-repo/.git/'
5. Type in `touch README.md`. This creates a new blank file. Stage then commit.
6. Go back to your `git-basic-exercises` repo and use `git log` to check that you are in the right place and repo.

### gitignore

1. Create a new file `touch ignore-me.db`
2. Now use `git status` to see what is going on in your repo, you will see ignore-me.bd as an unstaged file.
3. Now lets create a .gitignore file type `nano .gitignore`
4. In this file type `ignore-me.db` save and exit your .gitignore file
5. Now use `git status` you will notice that `ignore-me.db` is no longer an unstaged file and is no longer being tracked by github and .gitignore is being tracked.
6. Create a new directory `mkdir large-directory-that-should-be-local-only`
7. `cd` into this directory and create a readme.md file with some random text in
8. Use `cd ..` to go back to your main directory and `git status` to see what is going on, you should now see your new folder as an unstaged change.
9. Lets add this folder to .gitignore `nano .gitignore` and add `/large-directory-that-should-be-local-only` on a new line, save and close .gitignore
10. Check `git status` again, .gitignore is going to be super useful later when you are submitting projects and need to keep your repos small and free from junk and irrelevant files.

#### gitignore best practices

You should always gitignore the items in the below list:

- secrets like passwords and keys
- databases
- pycache/
- node_modules/
- temporary files and editor settings files eg .vscode/

### Repo Best Practices

Your repo should be all of the following:

1. Files and folders in your repo should be named appropriately.
2. Use names that make sense and relate to your projects i.e. simple-calculator
3. Each project should be in its own repo
4. There should be no junk/unnecessary file in your repos
5. Your repos should be small (remember the use of .gitignore)

## Going forward

We just covered the basics here. Please make sure you understand this stuff. It's super important. Git might seem like a weird theoretical thing to a lot of you. It might seem completely unrelated to the actual job of writing code. But it's not. Git makes teamwork on dev teams possible. Without it we'd spend more time shouting at each other than writing useful code. So learn it. Be comfortable with it. When we start working in teams later on all will be made clear.

If you are curious now, spend some time googling git branching strategies. We use the feature branching strategy here. We'll cover it in depth later on in the course.