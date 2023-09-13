---
_db_id: 763
content_type: project
flavours:
- any_language
prerequisites:
  hard:
  - coding_aptitude_assessment/coding_challenges/introduction
  - coding_aptitude_assessment/coding_challenges/how_to_name_files
protect_main_branch: false
ready: true
submission_type: repo
title: 'Coding aptitude assessment challenge: Task 5'
---

Write a function that takes in three numbers(integers) and **returns** the maximum number.

Do this without using any built-in methods. Write your own logic from scratch.

The function should expect 3 numbers(integers), not an array or list.

```
task5([1,2,3])  // BAD - this function accepts an array/list which is wrong
task5(1,2,3)  // GOOD - this accepts three numbers just like we need it to.
```

Example usage:

- `task5(1,2,3)` should return `3`
- `task5(-1,-2,-3)` should return `-1`
- `task5(2,2,2)` should return `2`

## Check your understanding

- Which number is bigger: -1 or -12?
- Which number is bigger: -1 or 0?
- What would you need to do differently in your code if you did accept an array or list?
- Are there built-in functions that can calculate the maximum number? How about the minimum number?
- How do you think you benefit from writing these kinds of functions yourself? What do you think we are testing for?
- You made use of `>` or `<` operators. What other comparison operators are there?
- can you think of how you would solve this problem using a loop?
- can you think of how you would solve this problem without using a loop?