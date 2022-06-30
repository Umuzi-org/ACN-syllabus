---
_db_id: 214
content_type: project
flavours:
- java
from_repo: projects/java-specific/introduction-to-spring-boot/part1
prerequisites:
  hard:
  - projects/java-specific/introduction-to-spring-boot/part1
  - topics/java-specific/introduction-to-spring-boot/part2
  soft: []
ready: true
submission_type: continue_repo
tags:
- spring-boot
- rest-api
- mvc
- annotations
title: Introduction to Spring Boot - Part 2
---

We are going to focus on creating a REST api that will serve as a end point to our spring boot java application.

## Service

Continuing with {{% contentlink path="projects/java-specific/introduction-to-spring-boot/part1" %}} for the **User** we are going to expose a **REST endpoint** to the application and we will use test to see if the application does what we want it to.

**Step 1**

Create a Controller Class based on the spring MVC infrastructure. This will be used to expose the endpoint.

```
package controller;

public class UserController {
}
```

**Step 2**

Make sure the service created here {{% contentlink path="projects/java-specific/introduction-to-spring-boot/part1" %}} is marked as a service.

```
?
public class UserServiceImpl{
    addUser(name, surname) // should call insert(name, surname) from FakeRepo and print to console '[name] entered'

	removeUser(Id) // should call delete(id) from FakeRepo and print to console '[name] removed'

	getUser(Id) // should call find(id) from FakeRepo and print to console 'hello [name]'

	[name] - replaced with actual name
    }
}

```

**Step 3**

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

**Step 4**

Do not forget to write integration tests for the endpoints(addUser, getUserById, removeUser) in your controller using MockMVC or TestRestTemplate.

- All CRUD operations defined in your services should be accompanied by corresponding unit test,
  using the relevant spring annotations as in {{% contentlink path="projects/java-specific/introduction-to-spring-boot/part1" %}}.

**Side Notes**
1 - Please remember to test your end points using postman. If you need help with using postman access the using postman link.

2 - Add at least one image of a successful request using postman.
3 - Pay attention to resources provided below
4 - This project assumes you have set up your Postgress connection as it is an extension of part1 and part2 of the Spring Boot Series.
5 - Please create a new branch labeled **part3**
**Happy Coding...**

## Resources

https://dzone.com/articles/expose-restful-apis-using-spring-boot-in-7-minutes
https://www.google.com/search?q=using+postman&oq=using+postman&aqs=chrome..69i57j0l7.2559j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_WISeXrbFAZaY1fAPp6eFmA449
https://dzone.com/articles/creating-a-rest-api-with-java-and-spring
https://github.com/nikeshpathak/customer-demo-webservice/blob/master/src/main/java/com/example/customer/demo/controller/CustomerCtrl.java