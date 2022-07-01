---
_db_id: 215
content_type: project
flavours:
- java
from_repo: projects/java-specific/introduction-to-spring-boot/part1
prerequisites:
  hard:
  - projects/java-specific/introduction-to-spring-boot/part1
  - projects/java-specific/introduction-to-spring-boot/part2
  - topics/java-specific/introduction-to-spring-boot/part3
  soft: []
ready: true
submission_type: continue_repo
tags:
- spring-boot
- rest-api
- soap
- github-api
- rest-templates
title: Introduction to Spring Boot - Part 3
---

In this project we will consume a REST API and a SOAP web service in our User service repository.

## REST API

**Step 1**

Create a java application and import 'org.springframework.boot:spring-boot-starter-web' into your build.gradle file to convert it to a Web Spring Boot application or use https://start.spring.io/

Familiarize yourself with the git api found here https://developer.github.com/v3/ learn which endpoint to get your repo, commits maybe branches etc. Try it out on postman or curl on the terminal

**Step 2**

Now we are going to consume the api in our spring boot application using restTemplates as per topic work.

1. v3 version of the api implemented
2. A list of all your repos - output on the console
3. A list of commits in 1 repo of your choice - output on the console

## SOAP WEB SERVICES

**Step 1**

To make your life a bit easier I would suggest you run this project using jdk 8 you can find the install here https://www.oracle.com/za/java/technologies/javase/javase8-archive-downloads.html reason being

1. wsimport comes out of the box in jdk 8, jdk >9 removed wsimport and open sourced it
2. avoid the famous ```Implementation of JAXB-API has not been found on module path or classpath``` error

Clone the repo found here https://github.com/spring-guides/gs-producing-web-service and open the `complete` folder not the entire repo. Review it on a high level this will be the wsdl project we are going to use to learn how to consume a wsdl application. **DO NOT ADD THIS PROJECT AS PART OF YOUR SUBMISSION(this is so that you can generate the files)**

Change the application to run on port 9090 by adding this to the properties file

Run the application, you should be able to do to the below url,

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

**Step 2**
In your terminal navigate to `YourUserServiceRepo/src/main/java` and run this command

```
wsimport -keep -p com.nameOfYourPackage.wsdl http://localhost:9090/ws/countries.wsdl

```

**Step 4**
To get the generated class to stop showing errors you would need these dependencies

```
jakarta.xml.ws-api

javax.jws
```

**Step 3**

Now we start to do the real work

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