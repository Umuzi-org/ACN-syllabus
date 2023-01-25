---
title: Inconsistent return types
content_type: topic
---

Consider the following pseudocode function

```
function get_all_pull_requests(arguments){
    prs = do_some_api_calls_to_get_the_prs()
    if len(prs) == 0 
        return "No pull requests"
    else
       return make_a_nice_array(prs)
}
```

If there are no prs, then this function would return a string. If there are PRs then this function returns an array/list of data.

This is bad because it adds a whole lot of complexity to the calling code. 

Let's say we make use of the above function. We want to get a list of PRs and then make sure each PR has enough reviewers assigned to it. Here is some pseudocode:

```
array_of_prs = get_all_pull_requests(...)

if type of array_of_prs is array:   # required because we shouldn't loop over the string
    for pr in array_of_prs:
        add_reviewers_to_pr(pr)
```

That's a bit crazy. The following would be better, but it would cause bugs if there aren't any prs.

```
array_of_prs = get_all_pull_requests(...)

for pr in array_of_prs:
   add_reviewers_to_pr(pr)
```

The best thing to do would be to fix the get_all_pull_requests function so it just returns an array all the time. 

```
function get_all_pull_requests(arguments){
    prs = do_some_api_calls_to_get_the_prs()
    if len(prs) == 0 
        return [] # How easy is that?
    else
       return make_a_nice_array(prs)
}
```