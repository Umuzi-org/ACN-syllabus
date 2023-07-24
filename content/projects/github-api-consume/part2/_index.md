---
title: Consume Github API - add some tests
content_type: project
flavours:
- any_language
prerequisites:
  hard:
  - projects/github-api-consume/part1
  - topics/unit-testing-mocks-and-spies
ready: true
submission_type: continue_repo
from_repo: projects/github-api-consume/part1
---

## Set up your environment

### Python

Your directory structure should look like this:

```
├── requirements.txt
└── consume_github_api
│   └── consume_github_api.py
└── tests
    └── ...?
```

### JavaScript

Your directory structure should look like this:

```
├── spec
|   ├── support
|   |   └── jasmine.json
|   └── ???
├── src
|   └── consume_github_api.js
└── package.json
```

Remember to export your function:

```
module.exports = { YOUR_FUNCTION_NAME };
```

### Java

Please make use of IntelliJ and Gradle to create your project. The directory structure should look like this:

```
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    ├── main
    |   └── java
    |       └── ConsumeGithubAPI.java       <-------- names are important
    └── test
        └── java
            └── ???.java             <-------- names are important
```

## Instructions 

Your mission is to test your project. But it is important that your tests don't actually make any api calls. If you are not connected to the internet at all then your tests should still be useful.

A useful test gives us confidence that the code does what it is meant to do. 

If you do anything that looks like the following pseudocode then you are doing it **wrong**

```
spyOn(myFunction)   // mock a function
myFunction()        // call the mocked function
assert myFunction.wasCalledOnce  // expect that the mocked function was called. Because you just called it this will always pass. So the test is useless.
```

The above adds no confidence in the code under test since the code under test wasn't even used.


Here is a useful way to think about mocks and spies:

Making API calls is considered "expensive". Why? Because 

- API calls take time
- some APIs cost money 
- APIs tend to have rate limits, so if you call them too often they start to fail. If your tests start to fail because you run them too often that would be bad

You also want to make sure that your tests can pass even if there ius no internet connection.

You need to test that when you want to make an api call then:

1. the function that makes the api call is called with the right url, headers, etc
2. it gets called once, not twice
3. if it returns data of a specific format then that data is processed correctly

You don't want your unit tests to make api calls. You just want them to prove that the part of your machine that makes those calls is being used correctly.

As another example, if you were developing a "forgot password" or "confirm email address" function for a website then you would test pretty much the same thing. You need to make sure that the correct functionality gets evoked, without actually sending any emails.


