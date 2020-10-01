---
_db_id: 114
content_type: topic
ready: true
title: Environmental variables and secrets with gradle
---

Environment variables are global variables that are accessible from every system running in the OS (Operating System).

There are multiple forms of environmental variables that can be used in a java application.

Those accessible to any project in the operating system and those accessible to a specific java application

## Operating System Environment variables

The 2 links below describe what environment variables are and how to update them.

[Link 1](https://www.ntu.edu.sg/home/ehchua/programming/howto/environment_variables.html).

[Link 2](https://www.tutorialspoint.com/how-to-set-java-home-environment-variables-on-windows-os-in-java).

## Resources

You can read through the following [example](https://www.technicalkeeda.com/java-tutorials/read-environment-variables-in-java) to see how you can access the environment variables from a Java application.

## Note

A typical use case for environment variables is to store the paths to certain directories, such as paths to folders holding SDKs.


## Program specific environmental variables using java-dotenv

java-dotenv is a package that can be imported into a java project to assist with simplyfying using environment variables
in applications.

[Documentation](https://github.com/cdimascio/java-dotenv) for its use can be found here.

## Java deployment configurations with Gradle

deployment configurations refers to different build environments, each with their own set of variables that can be used when the
java application is built using those environments.

For example: If you have an Api for your development environment and an Api for Production, you can make use of gradle build types
to inform your application which Api it should communicate with in a specific build environment.

This automates the process of changing environments. So instead of having to manually change the Url of your Api to toggle
between development and production, you can create a debug and release build type. So changing the build environment will
automatically point to the correct version of the Api you are using.

[This](https://medium.com/@android2ee/playing-with-gradle-3-flavors-buildtypes-and-variants-ad5fe75158b9) documentation describles how to create different gradle files
for different situations in an Android project.

Android Apps can however be created using Java, so implementing gradle rules in a java application will follow the same format
as the documentation above describes.