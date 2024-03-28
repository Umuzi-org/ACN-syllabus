---
content_type: topic
title: "Introduction to Git and GitHub Part: 2"
ready: True
---

## Navigating Through Git Commands

Git commands are the magic spells you cast on your repository to perform a wide array of tasks, from creating copies of a repository to tracking changes and collaborating with others. Let's focus on the most frequently used commands:

### 1. `git clone`

`git clone` is your first step into the world of an existing project. This command is used to create a local copy of a remote repository. It's like downloading a folder from the internet, except this folder is a Git repository.

```
git clone <repository-url>
```

### 2. `git status`

`git status` is the command you'll use to get a quick overview of what's happening in your repository. It tells you which changes have been staged, which haven't, and which files aren't being tracked by Git.

```
git status
```

### 3. `git branch`

Branching is one of Git's standout features, allowing you to diverge from the main line of development and work independently. `git branch` lets you create, list, and delete branches.

```
git branch <branch-name> # Create a new branch
git branch               # List all branches
```

### 4. `git pull`

`git pull` updates your local repository to the newest commit from the remote repository. It's a way of synchronising your work with others, ensuring you're all building on the latest version.

```
git pull origin <branch-name>
```

### 5. `git push`

After you've made changes and committed them, `git push` sends your commits to the remote repository. This shares your work with the team, contributing to the collective project.

```
git push origin <branch-name>
```

### 6. `git commit -m`

`git commit` is how you save your changes. Think of it as taking a snapshot of your project at a specific point in time. The `-m` flag allows you to attach a message to your commit, explaining what you've done.

```
git commit -m "Your message here"
```

## Understanding 'origin' and Basic Branching

### What Does 'origin' Refer To?

In Git, `origin` is the default name given to the remote repository from which your local repository was cloned. It's like a nickname for the URL of the remote repository, making it easier to reference.

### How Does Branching Work?

Branching allows you to create separate lines of development. Imagine it as having a main storyline (`master` or `main` branch) and several side stories (other branches). You can work on new features, bug fixes, or experiments in branches without affecting the main project. Once you're satisfied with the changes in a branch, you can merge it back into the main storyline.

## Testing Your Commit

To check whether your commit works as intended, you can use:

1. **Local Testing**: Before pushing your changes, test them thoroughly in your local environment. Run your application or code to ensure it behaves as expected.
2. **`git diff`**: This command shows the differences between your working directory and the index (the area where changes are staged), helping you review what changes you've made.

```
git diff
```