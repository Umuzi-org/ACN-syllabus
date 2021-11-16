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
learning_outcomes:
  web_dev_http_requests
  web_dev_api_call_tools
  web_dev_restful_apis
  web_dev_json_data_representation
  web_dev_api_consumption
---

In this project you'll make use of Github's awesome API. We chose Github for this project because:

- you are already familiar with Github
- The api is really well documented
- the api is solidly built and a lot of people use it

## Instructions

First, get familiar with consuming apis from the command line. Play with this. [Getting started with the Github API V3](https://developer.github.com/v3/guides/getting-started/).

Remember, `curl` is your friend. And so is `man`. (try typing in `man curl` at the command line)

Now, in your language of choice (not bash, use Java, Python or Js) write a function with the input arguments:
- owner
- reporitory name
- start date
- end date

The function should output a list or array of pull requests on the repo such that the PRs were created, updated, merged or closed between the given two dates.
For each PR include the `id`, `user` (who opened the PR), `title`, `state`, and when it was created.  
While for private repos a token will be required, the function should be able to work on public repos (eg. [ACN-syllabus](https://github.com/Umuzi-org/ACN-syllabus)) without needing a token.

Please be sure to follow the standard naming conventions for your language.

## Resources

- [An introduction to curl using GitHub's API](https://gist.github.com/tazjel/8735770).
