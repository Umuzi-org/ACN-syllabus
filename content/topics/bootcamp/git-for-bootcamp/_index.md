---
_db_id: 393
content_type: topic
ready: true
tags:
- skill/git
title: Useful Git commands
---

You are going to need to execute a few git commands in order to succeed at bootcamp. Here is a bit of a cheat-sheet. Make sure that you can use all of this stuff!

| git command                                    | Function                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `git clone` _repo url_                         | **Clones** the repo to your local machine.                                                                                                                                                                                                                                                                 |
| `git checkout -b`_name-of-your-new-branch_     | This creates a new branch from the branch you had and **checks that branch out** (meaning that you are now working on that branch).                                                                                                                                                                                   |
| `git status`                                   | Returns the current working branch. If a file is in the staging area, but not committed, it shows with **git status**. Or, if there are no changes it will return nothing to commit, working directory clean.                                                                                               |
| `git push`                                     | **Pushes** the changes you have made, saved, and committed locally to the remote repo.                                                                                                                                                                                                                      |
| `git push --set-upstream origin` _branch name_ | **Sets the upstream** and enables you to push to the correct branch using the `git push` command.                                                                                                                                                                                                          |
| `git add` _file name_                          | **Adds the specified file** to the staging area so that it is ready to be committed.                                                                                                                                                                                                                      |
| `git add .`                                    | Adds all files with saved changes to the staging area so they are ready to commit **NB! always check `git status` before using `git add .`**                                                                                                                                                                        |
| `git commit -m "*your commit message*"`        | Record the changes made to the files to a local repository. For easy reference, each commit has a unique ID. It is best practice to include a message with each commit explaining the changes made in the commit. Adding a commit message helps to find a particular change or to understand the change. |
| `git status`                                   | Shows what files were changed since your last commit.                                                                                                                                                                                                                                                  |
| `git diff`                                     | Shows how files changed since your last commit. This is like a very informative version of `git status`.                                                                                                                                                                                               |

[Common Git Commands with Explications and examples of usage](http://guides.beanstalkapp.com/version-control/common-git-commands.html#local)