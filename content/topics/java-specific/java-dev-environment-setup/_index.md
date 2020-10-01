---
_db_id: 111
content_type: topic
ready: true
title: Java Dev environment setup
---

In this little tutorial we'll walk through the process of getting your dev environment ready for Java. We use a number of different tools, you'll need to get them all set up.

## Java SDK

First install openJDK

```
sudo apt install openjdk-11-jdk
```

## Try it out

Now let's take it for a spin.

Make a file called `HelloWorld.java` that looks like this:

```
public class HelloWorld
{
   public static void main(String[] args)
   {
      String greeting = "Hello World!";
      System.out.println(greeting);
   }
}
```

Now open up a terminal and cd into the directory containing your new file. Now do this:

```
ls | grep HelloWorld
javac HelloWorld.java
ls | grep HelloWorld
```

You should notice a new file called `Java.class`. The `javac` command compiles the java source code into bytecode.

Now run the following command in your terminal:

```
java HelloWorld
```

It should print `Hello World!` to the terminal. You just ran the bytecode.

## jshell

This is another way of interacting with Java. It gets installed automatically when you install the JDK (JDK == Java Development Kit). Type the following at the command line:

```
jshell
```

Now you can type in Java statements and they'll just get executed immediately.

```
|  Welcome to JShell -- Version 11.0.4
|  For an introduction type: /help intro

jshell> "Can I get a whoop whoop!".length()
$1 ==> 24

jshell> $1 * 2
$2 ==> 48

jshell> int foo=42
foo ==> 42
```

- use the Tab key to access auto-completion. Eg: Type "Ti" then press Tab and see what happens
- You can press Ctrl+d to exit the shell.

## IntelliJ

This will be your Integrated Development Environment (IDE). Anything you can do with IntelliJ you can also do from the command line and a plain ol text editer. The reason we us an IDE is because most of industry uses one.

If you are running Ubuntu or Mint you can just install it like this:

```
sudo snap install intellij-idea-community --classic
```

Otherwise take a look here for full installation instructions: https://www.jetbrains.com/help/idea/installation-guide.html. Please note, we will be using the "community" version.

## Try it out

- Open IntelliJ
- select File -> New Project
- Select Java
- press Next a couple of times, give your project a sensible name (eg `HelloWorld`)
- click 'Finish'

Now let's make a class file:

- select File > New > Java Class
- name yuor class `HelloWorld` and select `Class`
- edit the new file so it looks like this (this should seem very familiar)

```
public class HelloWorld
{
   public static void main(String[] args)
   {
      String greeting = "Hello World!";
      System.out.println(greeting);
   }
}
```

- save your changes (Ctrl+s). On a side note, keyboard shortcuts are your friend. Learn them.

Now let's run the code:
select Run > Run > HelloWorld

You should see something like this appear on the bottom of the screen:

```
/usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/java -javaagent:/snap/intellij-idea-community/177/lib/idea_rt.jar=32781:/snap/intellij-idea-community/177/bin -Dfile.encoding=UTF-8 -classpath /home/sheena/IdeaProjects/HelloWorld/out/production/HelloWorld HelloWorld
Hello World!

Process finished with exit code 0
```