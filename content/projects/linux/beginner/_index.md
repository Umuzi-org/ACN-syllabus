---
_db_id: 188
available_flavours:
- bash
content_type: project
prerequisites:
  hard:
  - topics/linux/intro-to-linux
  - topics/linux/intro-to-bash
  soft:
  - workshops/intro-to-linux
story_points: 1
submission_type: repo
tags:
- bash
title: Beginner Linux challenges
---

### Submission guidelines

While you work through this project you will save your script commands in a number of files called shell scripts, name them by task and sub task number i.e. 1-2, they have the extension .sh. You'll be handing those in later. In general we use a tool called Git and a platform called Github for project submissions but this will be covered later in the course.

### Task 1 : Basic Task

Open a linux terminal. Now do the following from the command line.

1. type in `ls` and press enter. What do you see? What does this mean?
2. type in `pwd` and press enter. What do you see? What does this mean?
3. Make a new directory called `workspace` then `cd` into your new directory
4. type in `ls` and press enter. What do you see? What does this mean?
5. Make a new file called `README.md` (you can use the `touch` command to do this)
6. Make a copy of `README.md`, name your copy `CHANGELOG.md`

#### Resources

1. [Linux basic commands](https://www.makeuseof.com/tag/an-a-z-of-linux-40-essential-commands-you-should-know/)

### Task 2 : Absolute and Relative Paths

Create an empty file named `exercise.md` and move this file to the `/tmp` directory, using a relative pathname. Then, delete this file using an absolute pathname.

### Resources

1. [Paths in linux](http://www.linfo.org/path.html)
2. [Absolute and Relative Paths (video)](https://www.youtube.com/watch?v=ephId3mYu9o)

### Task 3 : cat commands

1. Create 3 files namely `umuzi.md`, `recruits.md` and `cohort.md`.
2. Fill all 3 files with contents of your choice. Maybe some nice poems about you MUB experience.
3. Write a script that concatenates the content of `umuzi.md`, `recruit.md`, `cohort.md` and displays the result on the screen.
4. Write a script that takes the content of `umuzi.md`, `cohort.md` and `recruits.md` to print/store the output into a new file named `summary.md`.
5. use the command line to append the words "The End" to `summary.md`. Be careful not to overwrite the exiting contend

#### Resources

1. [Standard File Streams (video)](https://www.youtube.com/watch?v=shFMEJJ_fpU)
2. [The cat commands](http://www.linfo.org/cat.html)

### Task 7 Text editor

1. Using `nano` text editor create a file named `my_bio.md`
2. Save the file and close the editor
3. Create a folder named `my_files` and move `my_bio.md` within.

#### Resources

1. https://www.lifewire.com/beginners-guide-to-nano-editor-3859002

### Task 8 Update and Upgrade

1. Update your system with `sudo apt update`.
2. Use the `sudo apt upgrade` to apply the updates downloaded and select Y for Yes.
3. When installing a package you use `sudo apt install` package_name.
4. Install a specific package called tree; using `sudo apt install tree`.
   You might ask what is sudo? Sudo allows you to run programs with the security privileges of another user, it is also referred to as a superuser. It is often used to install, start and stop applications that require root priviledges.
5. `dpkg` is a tool to install, build remove and manage Debian Packages.
   This is how you use `dpkg`, we will install VS Code in this example.
   Firstly download VS Code [VS Code Download](https://code.visualstudio.com/download)
   then open your terminal in the current folder of the item you just downloaded, type in
   `sudo dpkg -i` filename.deb, you will then enter your password and the package will install.

### Resources

1. https://www.youtube.com/watch?v=o2JyzCH8tlM