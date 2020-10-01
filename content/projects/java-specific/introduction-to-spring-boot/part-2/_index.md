---
_db_id: 218
available_flavours:
- java
content_type: project
from_repo: projects/java-specific/introduction-to-spring-boot/part-1
prerequisites:
  hard:
  - projects/java-specific/introduction-to-spring-boot/part-1
  - topics/java-specific/introduction-to-spring-boot/part-2
  soft: []
ready: true
submission_type: continue_repo
title: Introduction to Spring Boot - part 2
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

because we don't have a REST API for now (will be covered in Part3) we are going to use Tests to simulate a REST API call.

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

Add the following class and provide implementation for the **configure** function where you see **// COMPLETE CODE HERE** specify your password and username.

```
@Configuration
public class WebSecurityConfigurer extends WebSecurityConfigurerAdapter {
    // TODO: Read more about this extension WebSecurityConfigurerAdapter

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        // COMPLETE CODE HERE
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
                .antMatchers("/user")
                .authenticated()
                .antMatchers("/user")
                .permitAll()
                .and()
                .httpBasic();
    }
}

```

**Step 2**

Add a test to show that your username and password actually work by using the following

```
  @Autowired
    private TestRestTemplate template;

    ResponseEntity<String> response = template.withBasicAuth(?).getForEntity(?)
```

## Resource 😉

https://howtodoinjava.com/spring-boot2/spring-boot-cache-example/

https://www.baeldung.com/spring-security-integration-tests