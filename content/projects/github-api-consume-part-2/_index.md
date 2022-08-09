---
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
  - projects/github-api-consume-part-1
  soft: []
ready: true
story_points: 3
submission_type: repo
tags:
- pagination
title: Add pagination to Consume Github API
---

In part 1 of this project, you made use of Github's awesome API. Now that you are familiar with how it works, you are going to upgrade that project by adding pagination. 

API Pagination is essential if you're dealing with alot of data and endpoints. It helps make your response easier to handle.

## Instructions

In your language of choice(Java, Python, JS) upgrade your existing function to take 2 extra input arguments:

- limit 
- offset 

This means that if your function worked like so:
```
getPullRequests("owner", "repoName", "2022-01-01", "2022-05-05")
```

It will now need to work like so:
```
getPullRequests("owner", "repoName", "2022-01-01", "2022-05-05", 50, 100)
```

The URL will now look like this:
```
https://api.github.com/repos/owner/repoName/pulls?limit=50&offset=100
```

50 in the URL represents the maximum number of items in a page and 100 representing the starting position of the list of items.

## Resources

- [Traversing with pagination](https://docs.github.com/en/rest/guides/traversing-with-pagination#basics-of-pagination).
- [Pagination](https://docs.github.com/en/github-ae@latest/rest/overview/resources-in-the-rest-api#pagination)

## Instructions for reviewers

- Make sure that the learner has made use of mocks and spies if/when testing this project.