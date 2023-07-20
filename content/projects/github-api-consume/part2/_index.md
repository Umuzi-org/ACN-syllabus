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

If you do anything that looks like the following pseudocode then you are doing it wrong:

```
spyOn(myFunction)   // mock a function
myFunction()        // call the mocked function
assert myFunction.wasCalledOnce  // expect that the mocked function was called
```

The above adds no confidence in the code under test since the code under test wasn't even used.


