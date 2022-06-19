---
content_type: project
flavours:
- any_language
prerequisites:
  hard:
  - projects/github-api-consume/part1
  soft: []
ready: true
story_points: 3
submission_type: repo
tags:
- pagination
title: Add pagination to Consume Github API
---

In part 1 of this project, you made use of Github's awesome API. Now that you are familiar with how it works, you are going to upgrade that project by adding pagination. 

API Pagination is essential if you're dealing with alot of data and endpoints - making sure your response is easier to handle.

## Instructions

In your language of choice(Java, Python, JS) upgrade your existing function to take 2 extra input arguments:

- page 
- limit 

This means that if your function worked like so:
```
getPullRequests("Owner", "RepoName", "2022-01-01", "2022-05-05");
```

It will now need to work like so:
```
getPullRequests("Owner", "RepoName", "2022-01-01", "2022-05-05", 1, 5);
```

1 here representing the page we want to return from the end point and 5 representing the offset or limit that we want from page 1.

## Instructions for reviewers

- Make sure that the learner has made use of mocks and spies to test the project.

## Resources

- [Traversing with pagination](https://docs.github.com/en/rest/guides/traversing-with-pagination#basics-of-pagination).

- [Pagination](https://docs.github.com/en/github-ae@latest/rest/overview/resources-in-the-rest-api#pagination)