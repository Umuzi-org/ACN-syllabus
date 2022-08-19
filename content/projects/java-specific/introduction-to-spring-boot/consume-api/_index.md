---
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

In this project we will consume a REST API and a SOAP web service as a new project.

## REST API

#### Step 1

Create a java application and import 'org.springframework.boot:spring-boot-starter-web' into your build.gradle file to convert it to a Web Spring Boot application or use https://start.spring.io/

Familiarize yourself with the git api found here https://developer.github.com/v3/ learn which endpoint to get your repo, commits maybe branches etc. Try it out on postman or curl on the terminal

#### Step 2

Now we are going to consume the api in our spring boot application using restTemplates as per topic work.

We would like to see:

1. v3 version of the api implemented

2. A list of all your repos - output on the console

3. A list of commits in 1 repo of your choice - output on the console

## SOAP WEB SERVICES

#### Step 1

Project Setup and configuration:

1. Make your machine run jdk version 8, the correct install is from this link https://www.oracle.com/za/java/technologies/javase/javase8-archive-downloads.html
2. Set up your $JAVA_HOME to point to this jdk version
3. You will know that you have set this up correctly when you run

 ```
 javac -version
 // output  jdk 1.8 or jdk 8
 ```

**Why do you need to change your jdk version for this project**

1. Peace of mine, dependency hell is a thing of nightmares
2. wsimport comes out of the box in jdk 8, jdk > 9 removed wsimport and open sourced it
3. avoid the famous ```Implementation of JAXB-API has not been found on module path or classpath``` error

#### Step 2

Clone the repo found here https://github.com/spring-guides/gs-producing-web-service and open the `complete` folder not the entire repo. Review it on a high level this will be the wsdl project we are going to use to learn how to consume a wsdl application. **DO NOT ADD THIS PROJECT AS PART OF YOUR SUBMISSION(this is so that you can generate the files)**

Change the application to run on port 9090 by adding this to the properties file

Run the application, if everything is set up properly you should be able to go to the url below,

```
http://localhost:9090/ws/countries.wsdl

```

and see this

```
<wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:sch="http://spring.io/guides/gs-producing-web-service" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://spring.io/guides/gs-producing-web-service" targetNamespace="http://spring.io/guides/gs-producing-web-service">
    <wsdl:types>
        <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" targetNamespace="http://spring.io/guides/gs-producing-web-service">
        <xs:element name="getCountryRequest">
            <xs:complexType>
            <xs:sequence>

// ....

```

keep this project running in the background

#### Step 3

In your terminal navigate to `[YourProjectName]/src/main/java` and run this command

```
wsimport -keep -p [package].wsdl http://localhost:9090/ws/countries.wsdl

// e.g wsimport -keep -p com.example.soap.wsdl http://localhost:9090/ws/countries.wsdl

```

#### Step 4

To get the generated class to stop showing errors you would need these dependencies

```
	implementation group: 'jakarta.xml.ws', name: 'jakarta.xml.ws-api', version: '2.3.3'
	implementation group: 'org.glassfish.main.javaee-api', name: 'javax.jws', version: '3.1.2.2'
```

#### Step 5

Now we start to do the real work

**Expose an endpoint that will print the following in the browser**

1 Get the currency for United Kingdom: Output

```
Currency: GBP

```

2 Get the capital of United Kingdom: Output

```
Capital: London

```

3 Get the population of United Kingdom: Output

```
Population: 63705000

```

### Happy Hacking!!!