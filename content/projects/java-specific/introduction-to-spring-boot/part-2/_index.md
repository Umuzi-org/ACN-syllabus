---
_db_id: 214
content_type: project
flavours:
- java
from_repo: projects/java-specific/introduction-to-spring-boot/part-1
prerequisites:
  hard:
  - projects/java-specific/introduction-to-spring-boot/part-1
  - topics/java-specific/introduction-to-spring-boot/part2
  soft: []
ready: true
submission_type: continue_repo
tags:
- spring-boot
- rest-api
- mvc
- annotations
title: Intro to spring boot project - Part 2
---

We are going to focus on creating a REST api that will serve as an end point to our spring boot java application.

## Service

Continuing with {{< contentlink path="projects/java-specific/introduction-to-spring-boot/part-1" >}} for the **User** we are going to expose a **REST endpoint** to the application.

**Step 1**

Create a Controller Class based on the spring MVC infrastructure. This will be used to expose the endpoint.

```
package controller;

public class UserController {
}
```

**Step 2**

Do the following in the UserController.

1 - Implement an end point to add a user
```
// returns string "[Name] added"
```

2 - Implement an end point to GET a user, should returns the user name
```
// returns string "Hello [Name]"
```

3 - Implement an end point to REMOEVE a user, should return that
```
// returns string "[Name] removed"
```


Example

```
	@PutMapping
  public ResponseEntity<String> update(@RequestBody Customer customer)
  {
      // ... ResponseEntity
  }

```

**Step 3**

Make sure your rest Api layer is well tested


**Side Notes**

1. Please remember to test your end points using postman. If you need help with using postman please checkout resources below.
2. Add at least one image of a successful request using postman.
3. Pay attention to resources provided below
4. Please create a new branch labeled **part2**

**Happy Coding...**

## Resources

- https://dzone.com/articles/expose-restful-apis-using-spring-boot-in-7-minutes
- https://learning.postman.com/docs/getting-started/introduction/
- https://dzone.com/articles/creating-a-rest-api-with-java-and-spring
- https://github.com/nikeshpathak/customer-demo-webservice/blob/master/src/main/java/com/example/customer/demo/controller/CustomerCtrl.java