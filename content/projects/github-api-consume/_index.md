---
_db_id: 186
available_flavours:
- any_language
content_type: project
prerequisites:
  hard:
  - topics/apis/basics/
  soft: []
ready: true
story_points: 3
submission_type: repo
tags: []
title: Consume Github API
---

In this project you'll make use of Github's awesome API. We chose Github for this project because:

- you are already familiar with Github
- The api is really well documented
- the api is solidly built and a lot of people use it

## Instructions

First, get familar with consuming apis from the command line. Play with this. [Getting started with the Github API V3](https://developer.github.com/v3/guides/getting-started/).

Remember, `curl` is your friend. And do is `man`. (try tying in `man curl` at the command line)

Now in your language of choice (not bash, use Java, Python or Js) write a function with the input arguments:

- reporitory name
- start date
- end date

The function should output a list or array of pull requests on the repo such that the PRs were created, updated, merged or closed between the given two dates.

Please be sure to follow the standard naming conventions for your language.

## Resources

- [An introduction to curl using GitHub's API](https://gist.github.com/tazjel/8735770).