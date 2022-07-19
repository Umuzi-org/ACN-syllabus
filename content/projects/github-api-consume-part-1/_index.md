---
_db_id: 186
content_type: project
flavours:
- any_language
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
- The api is really well documented
- The api is solidly built and a lot of people use it

## Instructions

First, get familiar with consuming APIs from the command line. Play with this. [Getting started with the Github API V3](https://developer.github.com/v3/guides/getting-started/).

Remember, `curl` is your friend. And so is `man`. (try typing in `man curl` at the command line)

Now, in your language of choice (not bash, use Java, Python or Js) write a function (get_pull_requests) with the input arguments:

- owner
- reporitory name
- start date (yyyy-mm-dd)
- end date (yyyy-mm-dd)

The URL should look like this:
```
https://api.github.com/repos/owner/repoName/pulls?state=all
```

JavaScript developers are encouraged to use [axios](https://axios-http.com/docs/intro) to make the http request.

The function should output a list or array of pull requests on the repo such that the PRs were created, updated, merged or closed between the given two dates.
For each PR include the `id`, `user` (who opened the PR), `title`, `state`, and when it was created.
While for private repos a token will be required, the function should be able to work on public repos (eg. [ACN-syllabus](https://github.com/Umuzi-org/ACN-syllabus)) without needing a token.

Please be sure to follow the standard naming conventions for your language.

Make sure the output matches the following example structure:
```
# input
get_pull_requests("Umuzi-org", "ACN-syllabus", "2022-03-01", "2022-03-10")

# output
[
  {"id":876359209, "user":"FaithMo", "title":"added data sci and eng info", "state":"open", "created_at":"2022-03-10"},
  {"id":"874927260", "user":"ry-oc", "title":"update sololearn python and all contentlinks etc", "state":"closed", "created_at": "2022-03-09"},
  {"id":872630389, "user":"Andy-Nkumane", "title":"added clarity on python error raising", "state":"open", "created_at":"2022-03-07"},
  {"id":"872484561", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed", "created_at":"2022-03-06"},
  {"id":"872482562", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"open", "created_at":"2022-03-06"},
  {"id":"872481470", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed", "created_at":"2022-03-06"},
  {"id":"872480774", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed", "created_at":"2022-03-06"},
  {"id":"872480210", "user":"Kate-bit-dev", "title":"Update _index.md", "state":"closed", "created_at":"2022-03-06"}
]
```

## Resources

- [An introduction to curl using GitHub's API](https://gist.github.com/tazjel/8735770).

### Instructions for reviewers
- Ensure that the function works with any GitHub User and repository name, meaning that the function should not only work with one User/repo name. 
- Ensure that for JavaScript the function prints the output, and for python the function returns the output
- Ensure that the correct error/exception messages are used when trying to handle errors, if an incorrect user or repo was passed in a function call then the error messages should be explicit e.g. `Error 404 User or Repo Not Found`.
- Ensure that the output is a list/array and depending on the dates passed in, if there were no open, closed, updated or merged PR's between the two dates an empty array/list should be printed out.
