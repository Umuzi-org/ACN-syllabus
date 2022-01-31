---
_db_id: 89
content_type: topic
ready: true
tags:
- clean-code
title: General Clean Code Guidelines
---

Please bookmark this page. If you submit a project and the code is not clean then you will be asked to go clean up your work. This isn't all going to make 100% perfect sense to you right now, but as you move forward in your course more and more will make sense.



“Any fool can write code that a computer can understand. Good programmers write code that humans can understand.” ― Martin Fowler

Always keep in mind that code is READ more often than it is written, so you should make sure it is easy to read. Always consider that someone else may need to understand your code a year from now.


## Good code makes its intentions clear

If someone else reads your code, they should know what's up. That's basically it. If you are working on a team and you are forever making your team members run screaming from your code then... well... that's a bad thing.

I am required by law to link to this cartoon: https://www.osnews.com/story/19266/wtfsm/.

And this one https://xkcd.com/1513/ (hover your mouse over the picture for extra lols)

## Naming conventions

 - Make sure your naming conventions use vowels. tld_crd is hard to interpret, but tilde_card would make sense in context.
 - Be consistent in your code-base as much as possible. Consistency in your code makes it much easier to understand.
 - Meaningful abbreviations are ok


## Names to Avoid

Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
In some fonts, these characters are indistinguishable from the numerals one and zero.

## Obvious Function and Variable Names

When you declare a variable, give it a name that describes what values or data it holds.
When you declare a function, give it a name that describes what it does.

Example of a bad function name:
```
run_process()
```
Example of a good function name:
```
sort_files()
```
Bad variable name:
```
divs
```
Good variable name:
```
cards
```

These names should be obvious and specific. Try to look at your code from the perspective of someone who has never seen it. They should be able to tell what it does just by reading it. Consider the next developer who will work on the code as your client. Name things according to exactly what they are and what they do. If you are struggling to name a function, it may be because your function does too many different things to give it a one simple descriptive name. Which brings us to the next point...

## Functions Should do One Thing

The moment you find yourself struggling to describe what your function does in a simple sentence, your function may be too long or too busy. Describing your function should be easy. This is when you need to take the pieces of logic that do specific things in your and move them into another function. Try to keep your functions under 25 lines long.

Let's say you wrote a function that sorts files. Below is some pseudocode illustrating what a bad vs good functions structure would look like.

```md
Bad File Sorting Function()
    some code that opens the folder
    some code that looks through the files
    attempts at finding the file
    some code that filters
    the results
    some code that sorts results
    some code that prints the result after the sorting
    some logic that closes
    the folder
```

```md
Sort Files(folder)
    open the folder
    sort files in the folder
    return the sorted files

Print Files(sorted folder)
    open the sorted folder
    print the files in the folder

Good File Sorting Function()
    sorted folder = Sort Files(folder)
    Print Files(sorted folder)
```

As you can see, there is a lot going on in the Bad file sorting function, so it would be difficult to describe what it does in one sentence or to give it a name.

## DRY - Don't Repeat Yourself

Ideally functionality should be represented in a code-base exactly once. If you find yourself repeating certain values such as strings or numbers for example, rather save those values to variables. This also means that if the values change, you won't have to change them update them again on every line where you've used them. You'll only need to change them where you originally created and assigned them.

The same applies to functions.

## Flat is Better Than Nested

If you are ever tempted to put a loop inside a loop... etc. Don't.

Functions are:

 - More explicit and specific about what they actually do than a loop inside a loop.
 - Easier to test than the inner-most loop of a 5 loop stack of spaghetti-code.
 - Easier to reuse.
 - Easier to document.

## Indentation, Alignment and Consistency

Indent and align your code so that you can clearly see what code runs inside a particular loop or function. Indented code is easier to read and maintain.

Example of Good Indentation

```md
Good File Sorting Function()
    Sort Files(folder)
    Print Files(sorted folder)
```

Example of Bad Indentation

```md
Good File Sorting Function()
Sort Files(folder)
Print Files(sorted folder)
```

In the above pseudo-code the "Sort Files" and "Print Files" function are actually called inside of the "Good File Sorting" function. They are a part of the "Good File Sorting" function. But without the indentation they all look like separate functions.

Besides alignment your code needs to be consistent. If you use spaces for indentation use them on every line. Don't use tabs in one line and spaces in another line. Rather just use spaces. You can set your IDE to indent using spaces as the default. There also plenty of code formatting and linting tools such as ESLint, Prettier, Black etc... Do make use of them.

## Cohesion and Loose Coupling

Cohesion can be summarized as: "Things that belong together should be together". Your code (files or modules) should be organized in such a way that they do one thing. They should have a single responsibility. If you want to understand a piece of code then you shouldn't have to travel to the far reaches of the code base, scrolling up and down forever in a single file to figure out how it works. So avoid writing code that contains a lot of random functions that don't have an obvious effect and don't be that person who writes files that have 200 lines of code.

Coupling is about how much each component in your code base depends on other components. Loose coupling is making sure that if you change some code it doesn't have any weird side effects that break other parts of your code base.  Your code should be loosely coupled.

## Defensive Programming

Defensive programming means anticipating things that could probably go wrong and coding to handle such situations or edge cases. The goal is to write code that can handle real life situations: e.g. invalid input from the user - the user inputs a number where your program requires a text string.

If you don't code defensively your code might for example fail to complete its work but still run with no errors and act as if there is no problem. This leads to bugs that are difficult to find and fix after you've pushed your code. You can make use of exception or error messages for example to prevent your code from running if the input was invalid. So think about the edge cases. Assume that your user isn't always going to follow the instructions or use your program as they were supposed. Then write your code in a way that anticipates and handles such misuse.

## General Tips

 - Never put passwords into the code base!
 - Always use version control, version control can save you in the event of a mishap.
 - KISS: Keep It Simple Stupid
   - Don't do fancy things for the sake of being fancy
   - Aim for elegance
     - This means clarity and simplicity (maintainability)
     - The more moving parts you have in your code the more likely things will be to break.
 - Break it down
   - If a function is more than 30 lines of code consider breaking it down
   - If you keep using the word and when describing a function consider breaking it down
 - Don't use global variables.

### When to break the rules

If you are working with someone else's code and there is a different convention in place then follow that convention. It's really important to stay consistent. Inconsistent code leaves people guessing, and guesses make messes people!

But if you are working with someone else's code and they are doing something bad, it is on you to help them out by talking things through.

## Expectations

We will be expecting you to write clean code for all your projects for now on. If the code you submit works but makes your reviewer feel like they need a shower then you will be asked to clean things up.

There are a few very common pitfalls people fall into. Here are a few things to keep in mind:

1. Names should make sense to humans and not be misleading
2. Comments are useful if they add clarity to programmers - if you are just rewriting your code in English then that is a waste of time
3. Files and folders should be named well too, code should be organized well
4. Code is overcomplicated, or there is random junk code that should have been deleted but wasn't
5. Language specific naming conventions should be followed