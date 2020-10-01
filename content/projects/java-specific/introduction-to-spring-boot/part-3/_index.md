---
_db_id: 214
available_flavours:
- java
content_type: project
from_repo: projects/java-specific/introduction-to-spring-boot/part-1
prerequisites:
  hard:
  - projects/java-specific/introduction-to-spring-boot/part-1
  - projects/java-specific/introduction-to-spring-boot/part-2
  - topics/java-specific/introduction-to-spring-boot/part-3
  soft: []
ready: true
submission_type: continue_repo
title: Introduction to Spring Boot - part 3
---

We are going to focus on creating a REST api that will serve as a end point to our sping boot java application.

## Service

Continuing with {{% contentlink path="projects/java-specific/introduction-to-spring-boot/part-1" %}} for the **User** we are going to expose a **REST endpoint** to the application and we will use test to see if the application does what we want it to.

**Step 1**

Create a Controller Class based on the spring MVC infrastructure. This will be used to expose the endpoint.

```
package controller;

public class UserController {
}
```

**Step 2**

Add two spring annotations to indicate:
1 - The REST Controller above the class declaration.
2 - The route URL extension to reach this controller.

```
package controller;

//add here.
//add your specified route as input parameter to your annotation.
public class UserController {
}
```

**Step 3**

Add the annotation to your UserServiceImpl that indicated class previously created in {{% contentlink path="projects/java-specific/introduction-to-spring-boot/part-1" %}} is a service.

```
//add annotation here.

public class UserServiceImpl{
    addUser(name, surname) // should call insert(name, surname) from FakeRepo and print to console '[name] entered'

	removeUser(Id) // should call delete(id) from FakeRepo and print to console '[name] removed'

	getUser(Id) // should call find(id) from FakeRepo and print to console 'hello [name]'

	[name] - replaced with actual name
    }
}

```

**Step 4**

Specify all your methods inside the UserServiceInterface then implement all methods in the UserServiceImpl.

**Step 5**

1 - Do the following in the UserController.

2 - Use the Put, Delete, Get spring annotations to map the respective services.

3 - Do not forget to mark the input parameter as a Request Body if you are receiving data in the body of the object.

4 - If you are receiving the data as url parameter - mark variable as a Path Variable.

5 - If you are receiving the data as a query parameter - mark variable as a query parameter.

Example

```
	@PutMapping
    public ResponseEntity<String> update(@RequestBody Customer customer)
    {
        customerService.update(customer);
        ResponseEntity<String> responseEntity = new ResponseEntity("Success!", HttpStatus.NO_CONTENT);
        return responseEntity;
    }

```

**Step 5**

Do not forget to write integration tests for the endpoints(addUser, getUserById, removeUser) in your controller using MockMVC or TestRestTemplate.

- All CRUD operations defined in your services should be accompanied by corresponding unit test,
  using the relevant spring annotations as in {{% contentlink path="projects/java-specific/introduction-to-spring-boot/part-1" %}}.

**Side Notes**
1 - Please remember to test your end points using postman. If you need help with using postman access the using postman link.

2 - Add at least one image of a successful request using postman.
3 - The first resource link shows you everything you need to do to complete this project from start to finish if you struggle with any step.
4 - This project assumes you have set up your Postgress connection as it is an extension of part1 and part2 of the Spring Boot Series.
5 - Please create a new branch labeled **part3**
**Happy Coding...**

## Resources

https://dzone.com/articles/expose-restful-apis-using-spring-boot-in-7-minutes
https://www.google.com/search?q=using+postman&oq=using+postman&aqs=chrome..69i57j0l7.2559j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_WISeXrbFAZaY1fAPp6eFmA449
https://dzone.com/articles/creating-a-rest-api-with-java-and-spring
https://github.com/nikeshpathak/customer-demo-webservice/blob/master/src/main/java/com/example/customer/demo/controller/CustomerCtrl.java