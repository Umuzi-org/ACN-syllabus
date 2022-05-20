---
_db_id: 218
content_type: project
flavours:
- java
from_repo: projects/java-specific/introduction-to-spring-boot/part-1
prerequisites:
  hard:
  - projects/java-specific/introduction-to-spring-boot/part-1
  - topics/java-specific/introduction-to-spring-boot/part-2
  - projects/java-specific/introduction-to-spring-boot/part-3
  
  soft: []
ready: true
submission_type: continue_repo
tags:
- spring-boot
- annotations
- unit-testing
- caching
- security
title: Introduction to Spring Boot - part 4
---

We are going to work on Spring boot **Caching** and **Security** for this project

## Caching

Continuing with {{% contentlink path="projects/java-specific/introduction-to-spring-boot/part-1" %}} for the **User** we are going to add **security** and **caching** on the application and we will use test to see if the application does what we want it to.

**Step 1**

Import the following dependency

```
dependencies {
    compile 'org.springframework.boot:spring-boot-starter-cache'
}
```

**Step 2**

Implement caching for the 'name' in the "getUser" method, use the right annotation to invoke this 😉, in order to see if something is being served from cache or not we are going to simulate our own delay.

Add this code on your getUser method just before the return statement

```
try
{
    System.out.println("Going to sleep for 5 Secs.. to simulate backend call.");
    Thread.sleep(1000*5);
}
catch (InterruptedException e)
{
    e.printStackTrace();
}
```

User the rest API you created in Part 2 to test your cache

Write a test that will call "getUser" four times

Expect output after running "getUser" four times

**Without Cache:**

```
Going to sleep for 5 Secs.. to simulate backend call.
Going to sleep for 5 Secs.. to simulate backend call.
Going to sleep for 5 Secs.. to simulate backend call.
Going to sleep for 5 Secs.. to simulate backend call.

```

**With Cache:**

```
Going to sleep for 5 Secs.. to simulate backend call.
...
...
...

```

## Security

Import the following dependency

```
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-security'
}
```

**Step 1**

Override the neccessary functions in the WebSecurityConfigurer class to configure your own username and password

**Step 2**

Add a test to show that your username and password actually work to override the default one

## Resource 😉

https://howtodoinjava.com/spring-boot2/spring-boot-cache-example/

https://www.baeldung.com/spring-security-integration-tests