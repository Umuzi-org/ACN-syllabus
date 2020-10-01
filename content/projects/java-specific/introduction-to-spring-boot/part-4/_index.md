---
_db_id: 215
available_flavours:
- java
content_type: project
from_repo: projects/java-specific/introduction-to-spring-boot/part-1
prerequisites:
  hard:
  - projects/java-specific/introduction-to-spring-boot/part-1
  - projects/java-specific/introduction-to-spring-boot/part-3
  - topics/java-specific/introduction-to-spring-boot/part-4
  soft: []
ready: true
submission_type: continue_repo
title: Introduction to Spring Boot - part 4
---

In this project we will consume a REST API and a SOAP web service in our User service repository.

## REST API

**Step 1**

Familiarize yourself with the git api found here https://developer.github.com/v3/ learn which endpoint to get your repo, commits maybe branches etc. Try it out or postman or curl on the terminal

**Step 2**

Now we are going to consume the api in our spring boot application using restTemplates as per topic work. I would like to se

1. I would like you to specifically return the v3 version of the api **(Hint: Read more on how to set headers in RestTemplate)**
2. A list of all your repos - output on the console
3. A list of commits in 1 repo of your choice - output on teh console

## SOAP WEB SERVICE

**Step 1**

Clone the repo found here https://github.com/spring-guides/gs-producing-web-service and open the `complete` folder not the entire repo. Review it on a high level this will be the wsdl project we are going to use to learn how to consume a wsdl application. **DO NOT ADD THIS PROJECT AS PART OF YOUR SUBMISSION(this is so that you can generate the files)**

Change the application to sun on port 9090 by adding this to the properties file

```
server.port=9090

```

Run the application you should be able to do to the below url,

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

**Step 3**

Now we start to do the real work

1. Get the currency for United Kingdom: Output

```
Currency: GBP

```

2. Get the capital of United Kingdom: Output

```
Capital: London

```

3. Get the population of United Kingdom: Output

```
Population: 63705000

```

### Happy Hacking!!!