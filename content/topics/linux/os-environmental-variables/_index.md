---
_db_id: 57
content_type: topic
prerequisites:
  hard:
  - topics/linux/intro-to-bash
  soft: []
ready: true
tags: []
title: Environmental Variables
---

This tutorial assumes that you are using some kind of bash derived shell. Open up your linux command prompt :)

## Shell variables

You have dealt with variables in your programming language of choice many times. Bash also has variables. You can declare them like this:

```
FOO=BAR
```

To print your variable you can do this kind of thing:

```
echo $FOO
```

You can also use bash variables within other bash operations. Eg:

```
ROOT_DIR=/path/to/some/important/directory
mkdir $ROOT_DIR
nano $ROOT_DIR/something.yaml
```

Bash has a problem with whitespace. These wont work:

```
FOO = BAR
BAZ=The quick brown fox
```

But these work:

```
FOO=BAR
BAZ="The quick brown fox"
MEH='The quick brown fox'
```

### try this out

Open two terminals.

In terminal 1:

```
echo $HELLO   # when HELLO is not defined, this doesn't print anything

HELLO=BAR # we define the variable and give it a value

echo $HELLO # prints BAR

```

In termainal 2:

```
echo $HELLO # what does this do?
```

## Scope

Consider the following Python code.

```
a = 1
# at this point in the code: only `a` is available

def foo():
    b = 2
        # at this point in the code: `a` and `b` are available, but not `c`
    def bar():
        c = 3
        # at this point in the code: `a`,`b` and `c` are all available

# at this point in the code: only `a` is available
```

Or similarly, this is the JavaScript version:

```
a = 1
// at this point in the code: only `a` is available

function foo():
    b = 2
        // at this point in the code: `a` and `b` are available, but not `c`
    function bar():
        c = 3
        // at this point in the code: `a`,`b` and `c` are all available

// at this point in the code: only `a` is available
```

Look at where the different variables are allowed to be used. If a variable can be used then it is _in scope_. Otherwise it is _out of scope_.

## Environmental variables

Environmental variables are shell variables that have a larger scope.

Do this out in yout terminal:

```
# first we are going to make a new shell script:

echo "#\!/bin/sh\n" >> my_script.sh
echo "echo '--- start of my script ---'" >> my_script.sh
echo "echo FOO=\$FOO" >> my_script.sh
echo "echo BAR=\$BAR" >> my_script.sh
echo "echo '--- end of my script ---'" >> my_script.sh

# you can look at the new file you just created.
ls -l | grep my_script  # take note of the output. That -rw-rw-r-- part tells the operating system what actions are allowed. This file can be read and written
cat my_script.sh

# make the script executable

chmod +x my_script.sh
ls -l | grep my_script # the output is a little bit different now. x means executable
```

Great, now you can run the script like this:

```
./my_script.sh
```

Expected output:

```
--- start of my script ---
FOO=
BAR=
--- end of my script ---
```

Ok, now paste these lines into your terminal one by one. Make sure you understand the output of my_script.sh at each point:

```
FOO=1
./my_script.sh  # FOO is out of scope!

export FOO
./my_script.sh  # FOO is IN scope!

export BAR=winning
./my_script.sh

FOO=hello
./my_script.sh
```

### Takeaway

You can define variables in your shell (command prompt) and make those variables accessable from within programs that you run from that shell. Those programs could be bash scripts (like my_script.sh), or those programs can be written in Node or Python.

### storing your environmental variables somewhere nice

Open up a new shell. Make a new script called `my_config.sh`. Give it the following content:

```
#!/bin/sh

echo '--- setting up configurtion ---'
export FOO="/path/to/local/database/file.sqlite"
BAR="some other important configuration"
echo '--- finished setting up configurtion ---'
```

Make it executable and try this out:

```
export FOO=xxxxxxxxx
./my_config.sh
./my_script.sh
echo $FOO
```

Aaaand... my_config.sh seems to have had no effect on `FOO`.

Now try it this way:

```
export FOO=xxxxxxxxx
source my_config.sh   ###
./my_script.sh
echo $FOO
```

When we use the `source` command then any variables `export`ed by `my_config.sh` become environmental variables.

## `.bashrc`

The default linux shell is called bash. Every time you open up a new bash shell the bash automatically sources a file in your home directory called `.bashrc`.

Do the following in a terminal:

```
ls ~ -a | grep bashrc
cp ~/.bashrc ~/.bashrc.backup
ls ~ -a | grep bashrc
```

Now open .bashrc for editing however you want. You can just use nano if you dont want to leave the terminal.

```
nano ~/.bashrc
```

Now paste the following at the top of the file:

```
echo "--- start of custom bashrc content ---"
export FOO="/path/to/local/database/file.sqlite"
BAR="some other important configuration"
echo "--- end of custom bashrc content ---"
```

Save and exit. If you are using nano thenpress `Ctrl + X`, then `y` then enter

Now open a new terminal. And make sure you unserstand the output of each of these lines:

```
echo FOO=$FOO
echo BAR=$BAR
./my_script.sh
```

You can even put `source` commands within your `.bashrc`. Eg:

```
source /path/to/some/system/wide/configuration
```

Some of the more advanced python people might recognise this line:

```
source /usr/local/bin/virtualenvwrapper.sh
```