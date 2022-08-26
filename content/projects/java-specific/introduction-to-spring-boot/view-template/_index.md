---
content_type: project
flavours:
- java
ready: true
submission_type: repo
tags:
- spring-boot
- rest-api
- rest-templates
title: Spring Boot - View Template with Thymeleaf and Upload Files
---

Java is mostly used for backend application but sometimes you might need to harnes javascript skill within java to run some front application that does something that mostly is backend heavy, this is what we are going to do here

In this project we are going to upload a file from the frontend and process it in the backend

### Step 1

Create a spring boot application and add the relevant dependencies

```
spring-boot-starter-web
spring-boot-starter-thymeleaf
```

### Step 2

Create an `UploadController` this will hold the rest request to handle the file upload UI, this controller should handle two request

1. Request to upload one file `uploadSingleFile`
2. Request to outpload multilple files `uploadMultipleFiles`

Note: You need a place to upload these files, and this will be another folder in your machine, create that directory such that if it does not already exist a new folder will be created.

### Step 3

Now you have to build the UI element using thymeleaf that will handle the files upload process. The UI component should have

-  A button to upload the single file and text next to the button that shows the size (KB, MB, TB) of the uploaded file and name of that file

```
// File size: 50 MB
// Name of file: MyNewFile.pdf
```

-  A button to upload multiple files and text next to the button that shows the total file size (KB, MB, TB) of all the uploaded files and the number of files uploaded

```
// Total file size: 500 MB
// Totals files: 3
```

### Happy Hacking!!!

## Resources
- https://www.thymeleaf.org/
- https://www.baeldung.com/thymeleaf-in-spring-mvc
- https://www.baeldung.com/sprint-boot-multipart-requests

