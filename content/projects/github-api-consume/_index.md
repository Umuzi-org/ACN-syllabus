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
  soft: []
ready: true
story_points: 3
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

### JavaScript

Your directory structure should look like this:

```
├── src
|   └── consume_github_api.js
└── package.json
```

### Java

Your directory structure should look like this:

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

## Instructions

First, get familiar with consuming APIs from the command line. Play with this. [Getting started with the Github API V3](https://developer.github.com/v3/guides/getting-started/).

Remember, `curl` is your friend. And so is `man`. (try typing in `man curl` at the command line)

Now, in your language of choice (not bash, use Java, Python or Javascript) write a function (`get_pull_requests` in Python, `getPullRequests` in Java and Javascript) with the input arguments:

- owner
- repository name
- start date (yyyy-mm-dd)
- end date (yyyy-mm-dd)

The function should return a list or array of pull requests on the repo such that the PRs were created, updated, merged or closed between the given two dates.

For each PR include the `id`, `user` (who opened the PR), `title`, `state`, and when it was created.
While for private repos a token will be required, the function should be able to work on public repos (eg. [ACN-syllabus](https://github.com/Umuzi-org/ACN-syllabus)) without needing a token.

Use this url: `https://api.github.com/repos/{repoOwner}/{repoName}/pulls`. Learn more about it [here](https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-pull-requests)

**For those using javaScript**, please use [the axios library](https://axios-http.com/) for making the API calls.

Export the `get pull request` function from a file named `consume_github_api.js`

Please be sure to follow the standard naming conventions for your language. As usual.

Make sure the output matches the following when called with the arguments below:

```bash
# input
get_pull_requests("Umuzi-org", "ACN-syllabus", "2022-03-01", "2022-03-10")

# output
[
  {"id":"876359209", "user":"FaithMo", "title":"added data sci and eng info", "state":"open", "created_at":"2022-03-10"},
  {"id":"874927260", "user":"ry-oc", "title":"update sololearn python and all contentlinks etc", "state":"closed", "created_at": "2022-03-09"},
  {"id":"872630389", "user":"Andy-Nkumane", "title":"added clarity on python error raising", "state":"open", "created_at":"2022-03-07"},
  {"id":"872484561", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed", "created_at":"2022-03-06"},
  {"id":"872482562", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"open", "created_at":"2022-03-06"},
  {"id":"872481470", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed", "created_at":"2022-03-06"},
  {"id":"872480774", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed", "created_at":"2022-03-06"},
  {"id":"872480210", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed", "created_at":"2022-03-06"},
  ...
]
```

**Note:** the `state` and `title` properties may not be exactly the same because things change. The PR may have been closed and the title may have been updated for many reasons.

### Pagination

**Pagination** is a process that is used to divide a large dataset into smaller chunks (pages).

It is there to allow us to efficiently query through large data one page at a time.
This means we are able to gradually fetch the data we need with little to no performance issues on both the client and server.
For example, without pagination you would have to load an entire chat history just to see the latest message sent to you.

Please implement pagination. Your `get_pull_requests` function should return a list/array of ALL the matching pull requests, not just the first page.

Please fetch the maximum number of PRs per page(100) to avoid making too many api calls.

## Resources

- [An introduction to curl using GitHub's API](https://gist.github.com/tazjel/8735770).
- [Traversing with pagination](https://docs.github.com/en/rest/guides/traversing-with-pagination#basics-of-pagination).
- [Crash course video tutorial on Github's API](https://www.youtube.com/watch?v=5QlE6o-iYcE)

## Instructions for reviewers

- Ensure that the list of PRs matches the one in the instructions above when called with those arguments(the `state` and `title` property may not be the exact same).
- Ensure that the function works with any GitHub user and repository name, meaning that the function should not only work with one user/repo name.
- Ensure that the function returns the output. Printing the output is insufficient
- Ensure that the output is a list/array and depending on the dates passed in, if there were no open, closed, updated or merged PR's between the two dates an empty array/list should be printed out.
- Ensure that the correct error/exception messages are used when trying to handle errors, if an incorrect user was passed in a function call then the error messages should be explicit to let us know that it was the username specifically that was passed into the function that is incorrect. This also applies to when incorrect repo is passed into the function. Explicit error messages helps us know where exactly issues are coming from and to quickly resolve them without having to guess what we did wrong that triggered the error.