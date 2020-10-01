---
_db_id: 265
available_flavours:
- any_language
content_type: project
pre: '<b>MEDIUM: </b>'
ready: true
submission_type: repo
title: recursive search
---

This should be written following a TDD process. Remember that this means: RED, GREEN, REFACTOR. The refactor part of this is very very important.

You have a data structure like this:

{{% code_snippet "struct-shallow.js" %}}

This represents a directory structure with files and directories. (directory == folder)

## Part 1

1. Write a function that returns a list/array of all `.mov` files. Call this function `find_all_movs`
2. Write a function that returns a list/array of all `.mp4` files. Call this function `find_all_mp4s`
3. Write a function that returns a list/array of all cat videos (`mp4` and `mov` files that have the word "cat" in their name). . Call this function `find_all_cat_videos`

You will notice that there is a lot of repetition in the functionality you implemented. Each of these functions need to visit every FILE in the directory structure and then check if that file matches the search criteria.

Now consider te following:

{{% code_snippet "struct.js" %}}

Directory structures usually have some depth. Directories have sub directories. Sub directories also contain stuff.

## Part 2

make sure `find_all_movs`,`find_all_mp4s`,`find_all_cat_videos` work with nested directory structures.

HINT: you'll be using a technique called "recursion" here. play with it a little bit. The just of it is: You can call a function from within itself. Play with this a little bit

```
function my_recursive_function(i){
    console.log(i) ;
    if (i > 100) // this terminates the recursion
        return
    my_recursive_function(i + 1);   // this does the recursion
}
```