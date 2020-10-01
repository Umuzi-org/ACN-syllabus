---
_db_id: 187
available_flavours:
- bash
content_type: project
ready: false
submission_type: repo
title: Advanced Linux challenges
todo: 2.4 doesn't make sense
---

## Task 1 User environment

1. Use `echo` to display `Hello` followed by your username. (use a bash variable!)
2. Create a variable `myName` with a value containing your full name.
3. Copy the value of `$LANG` to a new variable called `$MyLANG`.
4. List all current shell variables.
5. Create a nodejs/python script that fetch all created variable and prints/logs them out

### Resources

1. https://dzone.com/articles/linux-environment-variables
2. https://codeburst.io/how-to-create-shortcut-commands-in-the-terminal-for-your-mac-9e016e25e4d7

## Task 2 Bash and basic scripting

1. Write a bash script that prints `Welcome to my world!` on the screen
2. Modify the shell script from point (1) to include a variable. The variable will hold this valuee `Welcome to my world!`
3. Store the output of the command `hostname` in a variable. Display `This script is running on _.` where `_` is the output of the `hostname` command.
4. Write a shell script to check to see if the file “file_path” exists. If it does exist, display “file_path passwords are enabled.” Next, check to see if you can write to the file. If you can, display “You have permissions to edit “file_path.””If you cannot, display “You do NOT have permissions to edit “file_path””
5. Write a shell script that displays `man`, `bear`, `pig`, `dog`, `cat` and `sheep` on the screen with each appearing on a separate line. Try to do this in as few lines as possible.
6. Write a shell script that prompts the user for a name of a file or directory and reports if it is a regular file, a directory, or another type of file. Also perform an `ls` command against the file or directory with the long listing option. If that doesn't make sense please try these on: `ls --help` and `man ls`
7. Modify the previous script to that it accepts the file or directory name as an argument instead of prompting the user to enter it.
8. Write a shell script that displays, `This script will exit status 0`. Be sure that the script does indeed exit with a 0 exit status.
9. Write a shell script that accepts a file or directory name as an argument. Have the script report if it is reguler file, a directory, or another type of file. If it is a directory, exit with a 1 exit status. If it is some other type of file, exit with a 2 exit status.

### Resources

1. https://ryanstutorials.net/bash-scripting-tutorial/bash-script.php
2. https://www.taniarascia.com/how-to-create-and-use-bash-scripts/