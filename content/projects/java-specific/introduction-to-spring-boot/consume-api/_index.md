---
_db_id: 792
content_type: project
flavours:
- java
prerequisites:
  hard:
  - topics/java-specific/introduction-to-spring-boot/consume-api
  soft: []
ready: true
submission_type: repo
tags:
- spring-boot
- rest-api
- soap
- github-api
- rest-templates
title: Spring Boot - Consume REST API and SOAP Service
---

In this project, we will consume a REST API and a SOAP web service as a new project.

## REST API

### Step 1

Create a Java application and import 'org.springframework.boot:spring-boot-starter-web' into your build.gradle file to convert it to a Web Spring Boot application or use https://start.spring.io/

Familiarize yourself with the git API found here https://developer.github.com/v3/. Learn which endpoint to use to get your repo, commits, and branches. Try it out on Postman or curl on the terminal.

### Step 2

Now we are going to consume the API in our spring boot application using restTemplates.

We would like to see:

1. v3 version of the API implemented
2. A list of all your repos - output on the console
3. A list of commits in 1 repo of your choice - output on the console

## SOAP WEB SERVICES

### Step 1: Project setup and configuration:

1. Make your machine run JDK version 8, the correct install is from this link https://www.oracle.com/za/java/technologies/javase/javase8-archive-downloads.html
2. Set up your `$JAVA_HOME` to point to this JDK version
3. You will know that you have set this up correctly when you run

 ```
 javac -version
 // output  jdk 1.8 or jdk 8
 ```

**Why do you need to change your JDK version for this project**

1. Peace of mind, dependency hell is a thing of nightmares
2. wsimport comes out of the box in jdk 8, jdk > 9 removed wsimport and open sourced it
3. avoid the famous `Implementation of JAXB-API has not been found on module path or classpath` error

### Step 2

Clone the repo found here: https://github.com/spring-guides/gs-producing-web-service.  Then open the `complete` folder in your IDE (do not open the entire repo, just the directory). Read through it on a high level and make sure you understand it, your goal here is to learn how to consume a wsdl application. 

**IMPORTANT:** DO NOT ADD THIS PROJECT AS PART OF YOUR SUBMISSION - this is so that you can generate the files.

Change the application to run on port 9090 by adding this to the properties file.

Run the application, if everything is set up properly you should be able to go to the URL below:

```
http://localhost:9090/ws/countries.wsdl
```

You'll see something like this:

```
<wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:sch="http://spring.io/guides/gs-producing-web-service" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://spring.io/guides/gs-producing-web-service" targetNamespace="http://spring.io/guides/gs-producing-web-service">
    <wsdl:types>
        <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" targetNamespace="http://spring.io/guides/gs-producing-web-service">
        <xs:element name="getCountryRequest">
            <xs:complexType>
            <xs:sequence>

// ....
```

Keep this project running in the background, you'll need it later in your project.

### Step 3

In your terminal navigate to `[YourProjectName]/src/main/java` and run this command:

```
wsimport -keep -p [package].wsdl http://localhost:9090/ws/countries.wsdl

// e.g wsimport -keep -p com.example.soap.wsdl http://localhost:9090/ws/countries.wsdl
```

### Step 4

Add the following dependencies to get the generated class to stop showing errors:

```
implementation group: 'jakarta.xml.ws', name: 'jakarta.xml.ws-api', version: '2.3.3'
implementation group: 'org.glassfish.main.javaee-api', name: 'javax.jws', version: '3.1.2.2'
```

### Step 5. Expose an endpoint that will print the following in the browser

Now we start to do the real work :)

1. Get the currency for the United Kingdom. The output should look like: 

```
Currency: GBP
```

2. Get the capital of the United Kingdom.The output should look like: 

```
Capital: London
```

3. Get the population of the United Kingdom. The output should look like: 

```
Population: 63705000
```