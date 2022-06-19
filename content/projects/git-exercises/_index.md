---
_db_id: 288
content_type: project
flavours:
- none
learning_outcomes:
- git_create_a_repository
- git_make_commits
- git_create_branches
- git_use_gitignore
- git_merge_branches
prerequisites:
  hard:
  - environment-setup/git
  - projects/bash-for-bootcamp
  - topics/git
  - topics/bootcamp/git-for-bootcamp
  - topics/github/helloworld
  soft: []
ready: true
story_points: 1
submission_type: link
tags:
- git
title: Git Basic Exercises
---

## Introduction

From this point forward, you will be expected to work with git like a real developer. This exercise exists to teach you the necessary skills. This stuff will serve you for your whole career. Git is critical to professional developers.

Professionals are comfortable using git from the command line. Let us get cracking :)

## Skills you'll learn

By the end of this you are expected to know:

- How to set up a repository on GitHub
- How to make commits
- How to make branches and switch between them
- How to use gitignore files
- How to merge branches
- How to overcome merge conflicts

When you are finished with these exercises come re-read this section and make sure you know what all these things mean.

## Creating and managing your own repo

Note: you can do all of this stuff from the command line! You should be using Linux. Open up a terminal and do the following:

### Your initial commit

1. Create a directory named `git-basic-exercises`
2. cd into your new directory
3. Look at what's inside using `ls -a`. It should be empty
4. Initialise your git repo using `git init`. Then check `ls -a` again. Can you spot the difference?
5. Check the status of your repo by typing `git status`
6. Type in `touch README.md`. This creates a new blank file. Then check `ls -a` and `git status` again
7. Type in `git log`. The output should make sense to you
8. Now add your readme file to your git staging area. Hint: use the `git add` command
9. Then check your `git status` again. Can you see the difference?
10. Try to unstage your file and check your `git status` again
11. Ok, now for your first commit: make sure your readme file is staged then type in `git commit -m "initial commit"`
    Your output should be something like this:

```
 [main (root-commit) 2103b64] initial commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
```

12. Type in `git log` isn't that nice? press `q` to exit

### More commits!

1. Type in `nano README.md`. This will open a text editor. Type in some stuff and then press `ctrl x` to exit. Then `y` then `enter`. This will save your changes
2. Type in `cat README.md`. This will print your file to the console
3. Take a look at the `git status` again and make sure you understand it
4. Commit your changes to your repo. Your commit should have the message `"second commit"`
5. Make some more changes to your readme and make a `"third commit"`

### Check this out

1. Type in `git log`. You should see all your commits there. It should look something like this:

```
commit a57585d3cf93e64c04e62e58dfe8151d191503cf (HEAD -> main)
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
3. Press q to exit the log view. You should now be back at the terminal
4. Type in `git checkout` and then paste in the commit hash and press enter
5. `cat README.md` It's like going back in time...
6. `git checkout main`
7. `cat README.md` Now we are up to date

You can jump to any commit using `git checkout`. You can checkout a branch, a commit hash, or a tag. We haven't explored tags here.

When you checkout a branch, you checkout the latest commit on that branch.

Why would you want to do this? Well, it's very useful to be able to go back and look at an old version of your code. Maybe you made a mistake and there is a bug, you may want to go back to when there was no bug.

### Branching

The real power of git is in branching. Branching is what allows big teams of developers to work on the same code base. Basically, different developers make branches for different things and then those branches can be merged together into one mighty application.

**Please Note** At some point during this exercise you will get an error message! It will say something about a merge conflict. DON'T PANIC! Merge conflicts are a fact of life and you will need to figure out how to fix it. [This](https://opensource.com/article/20/4/git-merge-conflict) should help.

Let's explore branching a little bit:

1. `git branch` This lists all your branches. Git makes a branch named `main` by default
2. Now create a new branch called `milkshake-flavours`. Git is not too restrictive when it comes to naming our branches. It's generally best to choose a name that has something to do with what the branch is for. Our branch is about milkshakes
3. Type in `git branch`. Notice the little `*`
4. Check out your new branch. type in `git branch` again and look at the `*`. Can you see what it means? Try switching between the different branches and see how things change.
5. Make sure you are on the `milkshake-flavours` branch then type in `nano milkshakes.md` and fill in a few flavours. Mmmm, save and exit
6. What does `git status` tell you?
7. Commit your new file with the message `"added initial flavours"`
8. Take a look at your git log again. It should make sense
9. Checkout your main branch. It'll look a little different. Can you see why?
10. From your main branch, create a new branch called `history` and check it out. If you say `git log` it should only have three commits. And if you use `git branch` you should see 3 branches! **This is important!**
11. Type in `history > history.txt`. Can you guess what it does?
12. Commit your changes with the message `"added history"`. Take a look at the `git log`
13. Now checkout your milkshake branch and look at the `git log`. it should have your three main commits and your one milkshake commit
14. Make some arbitrary changes to the readme file and make a new commit with the message `"random readme changes"`
15. Checkout `history` again and `cat README.md`
16. Now on your history branch do the following:

```
rm README.md
echo "booya" > README.md
```

You should know what these lines do.

17. Commit your changes. Use the commit message `"rewrote readme"`
18. Checkout main again

### Just make sure we are still on track

If you have followed along up until this point then your branches should look like this:

Type in:

```
git checkout main
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
commit a57585d3cf93e64c04e62e58dfe8151d191503cf (HEAD -> main)
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

Now let's look at milkshake-flavours:

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

    random readme changes

commit l8543u7648f3ec0f7928f6cbef705c6fagv78dsb
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:25:07 2019 +0200

    added initial flavours

commit a57585d3cf93e64c04e62e58dfe8151d191503cf (main)
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

Finally, history:

```
git checkout history
ls
```

There should be two files:

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

commit a57585d3cf93e64c04e62e58dfe8151d191503cf (main)
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

### Merging

Now we want to get the main up to date with all our changes. Let's start with the milkshake branch:

1. Merge milkshake-flavours into main

```
git checkout main
git merge milkshake-flavours
```

2. Use `ls` and `git log` to see what this did
3. Merge history into main
4. Use `ls` and `git log` to see what this did
   As you can see a whole lot of changes have been made to the main branch
5. Now lets take a look at the other branches

```
git checkout history
git log
...
git checkout milkshake-flavours
git log
```

These branches were not impacted by the merge!

In general, if we want to merge branch X into branch Y:

```
git checkout Y
git merge X
```

This adds a commit to branch Y and doesn't change branch X

6. Merge the main branch into `history`. Use `git log` to see whats up
7. Checkout main again. git log again. Can you spot any differences?

### GitHub

1. Go to Github.com (using your browser of choice) and create a new public repository using the user interface. Name it `git-basic-exercises`

2. You will see a bunch of weird looking things. There is a section entitled "… or push an existing repository from the command line". We have an existing repository and a command line. So, this seems appropriate. Copy the commands from there and paste them into your terminal. this will push your changes to GitHub.

3. Refresh your browser. Cool eh? The URL you are looking at should look like this: https://github.com/[YOUR_USERNAME]/git-basic-exercises

Now you should see a little dropdown box on GitHub that says "Branch: main". Click there. Your other branches aren't available.

4. Push your other branches to GitHub. We want all branches to be listed

**A cool trick we use all the time: the network page!**:

If your repo is available at https://github.com/[YOUR_USERNAME]/git-basic-exercises then take a look at https://github.com/[YOUR_USERNAME]/git-basic-exercises/network. I just added `/network` on the end there. You'll be able to see all the individual commits and all the different branches you've made and how they relate to each other.

Go look at your network page. Each of the dots there represent commits that you made. Can you see how they relate to what you did? Can you see the individual branches?

### Pulling and remotes

1. You should still be inside the `git-basic-exercises` directory. Let's get out of there. `cd ../`
2. Now let's clone a repo. Point your browser here: https://github.com/Umuzi-org/a-repo-to-clone
3. Now there is a friendly green button that says "Clone or download". Click on it
4. You will see a URL come up. Copy it. You will need to paste it into the terminal in a moment
5. In your terminal type in `git clone $THE_URL_YOU_JUST_COPIED`. It should look something like this: `git clone https://github.com/Umuzi-org/a-repo-to-clone`
6. `cd` into the `a-repo-to-clone` directory that was just created
7. Explore a little using `git branch` and `git log`
8. Type in `git branch -a`. This shows the remote branches
9. Try to checkout the branch called `a-branch-with-a-few-commits` on your local computer. You can do it, you will need to figure out how
10. Type in `git remote -v`

### Multiple repos

1. While still in your newly created branch `project/git-basic-exercises` use `git log` to see the history.
2. From your new branch called `project/git-basic-exercises` navigate back to your `git-basic-exercises` repo, use `git log` again to see the difference.
3. Let's go back to our home directory `cd` and make a new folder `mkdir this-will-be-another-repo`
4. cd into this folder now use `git init` to initialise a new git repo here, you should get a message in terminal that says 'Initialised empty Git repository in /home/\$specific-path/this-will-be-another-repo/.git/'
5. Type in `touch README.md`. This creates a new blank file. Stage then commit.
6. Go back to your `git-basic-exercises` repo and use `git log` to check that you are in the right place and repo.

### gitignore

1. Create a new file `touch ignore-me.db`
2. Now use `git status` to see what is going on in your repo, you will see ignore-me.db as an unstaged file.
3. Now let's create a .gitignore file type `nano .gitignore`
4. In this file type `ignore-me.db` save and exit your .gitignore file
5. Now use `git status` you will notice that `ignore-me.db` is no longer an unstaged file and is no longer being tracked by GitHub and .gitignore is being tracked.
6. Create a new directory `mkdir large-directory-that-should-be-local-only`
7. `cd` into this directory and create a readme.md file with some random text in
8. Use `cd ...` to go back to your main directory and `git status` to see what is going on, you should now see your new folder as an unstaged change
9. Let's add this folder to .gitignore `nano .gitignore` and add `/large-directory-that-should-be-local-only` on a new line, save, and close .gitignore
10. Check `git status` again, .gitignore is going to be super useful later when you are submitting projects and need to keep your repos small and free from junk and irrelevant files
11. Next, use `git add .gitignore` to add .gitignore into the staging area
12. After adding the file you can commit it by using `git commit -m "added .gitignore"`
13. Lastly, push all the changes to the GitHub repo through `git push`

#### gitignore best practices

You should always gitignore the items in the below list:

- secrets like passwords and keys
- databases
- pycache/
- node_modules/
- temporary files and editor settings files eg .vscode/

### Repo best practices

Your repo should be all the following:

1. Files and folders in your repo should be named appropriately
2. Use names that make sense and relate to your projects i.e. simple-calculator
3. Each project should be in its own repo
4. There should be no junk/unnecessary file in your repos
5. Your repos should be small (remember the use of .gitignore)

## Going forward

We just covered the basics here. Please make sure you understand this stuff. It's super important. Git might seem like a weird theoretical thing to a lot of you. It might seem completely unrelated to the actual job of writing code. But it's not. Git makes teamwork on dev teams possible. Without it we would spend more time shouting at each other than writing useful code. So, learn it. Be comfortable with it. When we start working in teams later on all will be made clear.

If you are curious now, spend some time googling git branching strategies. We use the feature branching strategy here. We'll cover it in depth later on in the course.

## Instructions For reviewers

- Check if multiple branches exist, to ensure learners understand how to create branches
- Check if the learner understands how merging works, by ensuring that the main branch has files merged into it. You can also take a look at the network diagram to check for merging
- Check the commit messages to see if a learner actually knows how to add, commit or push using the terminal or command line. If the commit message is `Add files via upload`, it indicates that the command line was not used
- Ensure that there are no merge conflicts. If this kind of text `<<<<<<< HEAD` or `=======` appears on the README.md file, it indicates that merge conflicts were not resolved