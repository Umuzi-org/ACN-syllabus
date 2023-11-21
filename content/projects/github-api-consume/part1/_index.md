---
_db_id: 186
content_type: project
flavours:
- any_language
learning_outcomes:
- web_dev_http_requests
- web_dev_api_call_tools
- web_dev_restful_apis
- web_dev_json_data_representation
- web_dev_api_consumption
prerequisites:
  hard:
  - topics/apis/basics/
  - topics/linux/os-environmental-variables
  soft: []
ready: true
submission_type: repo
tags:
- api
- github
- logical-operators
title: Consume Github API
---

In this project, you'll make use of Github's awesome API. We chose Github for this project because:

- You are already familiar with Github
- The API is really well documented
- The API is solidly built and a lot of people use it

## Set up your environment

### Python

Your directory structure should look like this:

```
├── requirements.txt
└── src
    └── consume_github_api.py
```

### JavaScript

Your directory structure should look like this:

```
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
    └── main
        └── java
            └── ConsumeGithubAPI.java       <-------- names are important
```

## Start by exploring the api

First, get familiar with consuming APIs from the command line. Play with this. [Getting started with the Github API V3](https://developer.github.com/v3/guides/getting-started/).

Remember, `curl` is your friend. And so is `man`. (try typing in `man curl` at the command line)

### API exploration resources

- [An introduction to curl using GitHub's API](https://gist.github.com/tazjel/8735770).
- [Crash course video tutorial on Github's API](https://www.youtube.com/watch?v=5QlE6o-iYcE)

## Project instructions

Write a function called "get pull requests". Make sure you are making use of the appropriate naming convention for the language you are working in.

The function should take in the following arguments:

- owner
- repository name
- start date (yyyy-mm-dd)
- end date (yyyy-mm-dd)

The function should return a list or array of pull requests on the repo such that the PRs were created, updated, merged or closed between the given two dates.

Play around with [this public repo](https://github.com/Umuzi-org/ACN-syllabus) and see if you can make it work.

Example usage:

**If you are working in JavaScript** we should be able to call your function like this: `getPullRequests({ owner, repo, startDate, endDate})`. Take note of those curly brackets.

```js
// Javascript

getPullRequests({
  owner: "Umuzi-org",
  repo: "ACN-syllabus",
  startDate: "2022-03-01",
  endDate: "2022-03-10",
});
```

```py
# Python

get_pull_requests(
  owner="Umuzi-org",
  repo="ACN-syllabus",
  startDate="2022-03-01",
  endDate="2022-03-10"
)

```

```java
// Java

getPullRequests(
  "Umuzi-org",
  "ACN-syllabus",
  "2022-03-01",
  "2022-03-10"
);
```

Here is an example of what the final data structure should look like if it was converted into JSON. This isn't the exact data you should expect, just pay close attention to the structure:

```bash
[
  {"id": 876359209, "user":"FaithMo", "title":"added data sci and eng info", "state":"open", "created_at":"2022-03-10"},
  {"id": 874927260, "user":"ry-oc", "title":"update sololearn python and all contentlinks etc", "state":"closed", "created_at": "2022-03-09"},
  {"id": 872630389, "user":"Andy-Nkumane", "title":"added clarity on python error raising", "state":"open", "created_at":"2022-03-07"},
  {"id": 872484561, "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed", "created_at":"2022-03-06"},
  {"id": 872482562, "user":"Kate-bit-dev", "title":"Update _index.md", "state":"open", "created_at":"2022-03-06"},
  {"id": 872481470, "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed", "created_at":"2022-03-06"},
  {"id": 872480774, "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed", "created_at":"2022-03-06"},
  {"id": 872480210, "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed", "created_at":"2022-03-06"},
  ...
]
```

Note that:

- The id is an integer
- the user is the person who created the pr

### Error messages

If the function is called with an "owner" that does not exist then the function should raise/throw and error. The error should include the following info:

- the value of the `owner` argument
- the fact that the owner was not found

For example "repository owner snoopdoggiedog not found".

If the owner is found but the repo seems to not exist then raise or throw an appropriate error.

#### A note on errors

Errors have been implemented in every modern language (even [this one](https://esolangs.org/wiki/COW)) because they are really useful. An error/exception is great because it tells a programmer:

1. Exactly what line of code caused the problem
2. The details of the problem

A good error message tells a programmer exactly what is wrong and how to fix it.

A good programmer doesn't just catch errors and squash them thoughtlessly. And a good programmer puts effort into writing good error messages.

### Pagination

**Pagination** is a process that is used to divide a large dataset into smaller chunks (pages).

It is there to allow us to efficiently query through large data one page at a time.
This means we are able to gradually fetch the data we need with little to no performance issues on both the client and server.
For example, without pagination you would have to load an entire chat history just to see the latest message sent to you.

Please implement pagination. Your `get_pull_requests` function should return a list/array of ALL the matching pull requests, not just the first page.

Please fetch the maximum number of PRs per page(100) to avoid making too many api calls.

#### Pagination resources

[Traversing with pagination](https://docs.github.com/en/rest/guides/traversing-with-pagination#basics-of-pagination).

### Public and private repos

Repos on Github can either be public or private. If you are trying to access a private repository then you'll need to authenticate using a token. Kindly generate the **classic token** and not the **fine-grained token** for this project authentication.

Upgrade your code so that It makes use of an environmental variable called `GITHUB_TOKEN`.

If the token is provided then it should ALWAYS be included in the header of requests sent to Github. If it is not provided then it should not be included.

## Instructions for reviewers

- Ensure that the list of PRs matches the one in the instructions above when called with those arguments(the `state` and `title` property may not be the exact same).
- Ensure that the function works with any GitHub user and repository name, meaning that the function should not only work with one user/repo name.
- Ensure that the function returns the output as a data structure. Printing the output is insufficient.
- Ensure that the output is a list/array and depending on the dates passed in, if there were no open, closed, updated or merged PR's between the two dates an empty array/list should be returned.
- Ensure that the correct error/exception messages are used when trying to handle errors, if an incorrect user was passed in a function call then the error messages should be explicit to let us know that it was the username specifically that was passed into the function that is incorrect. This also applies to when incorrect repo is passed into the function. Explicit error messages helps us know where exactly issues are coming from and to quickly resolve them without having to guess what we did wrong that triggered the error.