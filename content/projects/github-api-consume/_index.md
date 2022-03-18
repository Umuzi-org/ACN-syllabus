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

In this project you'll make use of Github's awesome API. We chose Github for this project because:

- you are already familiar with Github
- The api is really well documented
- the api is solidly built and a lot of people use it

## Instructions

First, get familiar with consuming apis from the command line. Play with this. [Getting started with the Github API V3](https://developer.github.com/v3/guides/getting-started/).

Remember, `curl` is your friend. And so is `man`. (try typing in `man curl` at the command line)

Now, in your language of choice (not bash, use Java, Python or Js) write a function (get_pull_requests) with the input arguments:

- owner
- repository name
- start date
- end date

The function should output a list or array of pull requests on the repo such that the PRs were created, updated, merged or closed between the given two dates.
For each PR include the `id`, `user` (who opened the PR), `title`, `state`, and when it was created.
While for private repos a token will be required, the function should be able to work on public repos (eg. [ACN-syllabus](https://github.com/Umuzi-org/ACN-syllabus)) without needing a token.

Please be sure to follow the standard naming conventions for your language.

Make sure the output matches the following example structure:
```
# input
get_pull_requests("Umuzi-org", "ACN-syllabus", "22-03-01", "22-03-10")

# output
[
  {"id":"874927260", "user":"ry-oc", "title":"update sololearn python and all contentlinks etc", "state":"closed"},
  {"id":"872484561", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed"},
  {"id":"872481470", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed"},
  {"id":"872480774", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed"},
  {"id":"872480210", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed"}
]
```

## Resources

- [An introduction to curl using GitHub's API](https://gist.github.com/tazjel/8735770).

### Instructions for reviewers
- Ensure that the function works with any github User and repository name, meaning that the function should not only work with one User/repo name. 
- Ensure that the function prints for JavaScript and for python the function should return the output.
- Ensure that the correct error/exception messages are used when trying to handle errors, if an incorrect user or repo was passed in a function call then the error messages should be explicit e.g. `Error 404 User or Repo Not Found`.
- Ensure that the output is a list/array and depending on the dates passed in, If there were no open, closed, updated or merged PR's between the two dates an empty array/list should be printed out.