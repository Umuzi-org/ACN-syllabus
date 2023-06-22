---
_db_id: 758
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
title: 'Coding aptitude assessment challenge: Task 6'
---

Write a function that can take in any number of numbers(integers). It should return the maximum number from those numbers.

Do this without using built-in methods. Write your own logic from scratch.

Again, the function should expect a bunch of numbers(integers) as input, not an array or list.

```
task6([1,2,44,3])  // BAD
task6(1,2,44,3)    // GOOD
```

Example usage:

- `task5(1,2,44,3)` should return `44`
- `task5(-1,-2,-44,-3,-5)` should return `-1`
- `task5(8,8,8,8,8,8,8)` should return `8`

## Check your understanding

- what kinds of loops do you know of? What are they for? How do they differ?
- will your code work if there are 50 numbers passed into your function?
- will it work if there are negative and positive numbers passed in?
- can it handle the number zero?
