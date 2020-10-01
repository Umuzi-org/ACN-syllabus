---
_db_id: 113
content_type: topic
ready: true
title: Introduction to Gradle
---

## What is gradle
According to Gradle Inc, Gradle is an open-source build automation tool that is designed to be flexible enough to build almost any type of software.[Here](https://docs.gradle.org/current/userguide/what_is_gradle.html) are the five things you need to know about gradle.

Gradle was chosen by Google as the official build tool for Android. [Find out why.](https://medium.com/jay-tillu/what-is-gradle-why-google-choose-it-as-official-build-tool-for-android-adafbff4034)

## Why we need a build tool
Build tools are programs that automate the creation of executable applications from source code. Building incorporates compiling, linking and packaging the code into a usable or executable form. In small projects, developers will often manually invoke the build process. 


## Java Build Tools
- Ant 
- Gradle
- Maven

Read up on the major differences between the following Java Build Tools [Gradle vs Maven](https://gradle.org/ maven-vs-gradle/)


## Your first Gradle application
1. Open Project Wizard, in the    left-hand pane select Gradle.
2. In the right-hand pane,        IntelliJ IDEA automatically    adds a project SDK (JDK) and   a default option Java in the  Additional Libraries and       Frameworks area. Click next.
3. On the next page of the wizard let's specify ArtifactId as test.project which basically is the name of our project. We can use the default information in the version field. Unless we plan to deploy our project in some Maven repository we don't need to specify a GroupId. Click next.
4. In the Project tool window open the src folder.
5. Right-click the main directory then the java subdirectory and from the list select New | Java Class.
6. In the Create New Class dialog specify the name of your Java Class as Gradle and click OK.
7. Add the following code in your Java Class

```
public class Gradle{
   public static void main(String[] args){
      String gradle = "Introduction to Gradle!";
      System.out.println(gradle);
   }
}
```
8. In the editor, in the left gutter, press icons toolwindows toolWindowRun svg and select Run 'HelloGradle.main()'.