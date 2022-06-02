---
_db_id: 754
content_type: project
flavours:
- any_language
prerequisites:
  hard:
  - coding_aptitude_assessment/coding_challenges/introduction
  - coding_aptitude_assessment/coding_challenges/how_to_name_files
ready: true
submission_type: repo
title: 'Coding aptitude assessment challenge: Task 10'
protect_main_branch: false
---

Make a function that takes two strings as input, and print the common letters that they share.

The printed letters should:
- be lowercase
- be in alphabetical order
- appear as a single string. Please see the example to see the format of the string
- There should only be letters in your result, no whitespace, numbers or special characters

Example usage:

- `task10("House","computers")` should print `e, o, s and u` exactly. If it prints `eosu` then that would be incorrect.
- `task10("Hi","there")` should print `h`
- `task_10("Foo","bar")` should print `no common letters`

There should only be one call to `print` or `console.log` in your whole function.
