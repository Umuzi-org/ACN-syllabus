---
_db_id: 83
content_type: topic
ready: true
title: Clean Code For JavaScript
---

Maintaining someone else’s code is not a smooth process. It takes time to understand the project ( such as the folder structure, naming, dependencies, scripts etc.), to find the pattern and develop the new feature in harmony and consistency with the existing code. Different developers use different styles which are derived from their different tastes. They may work on a project together or pick up someone else’s work. Which in both cases, having a common ground is essential.

#### JavaScript Naming Conventions

There is an introduction about [ JavaScript Naming Conventions here](https://www.robinwieruch.de/javascript-naming-conventions) with examples, which gives you the common sense when it comes to naming variables, functions, classes or components in JavaScript. No one is enforcing these naming convention rules, however, they are widely accepted as a standard in the JS community.

We do expect you to put effort into keeping your code clean and tidy. So please follow these conventions.

For most of your early work, you'll be naming `functionsLikeThis` and `variablesLikeThisToo`. The first letter is small, and then every word in the name starts with a capital letter.

`ClassesAreNamedLikeThis`, we'll get there a bit later :)

#### Good code makes its intentions clear

If someone else reads your code, they should know what's up. That's basically it. If you are working on a team and you are forever making your team members run screaming from your code then... well... that's a bad thing.

I am required by law to link to this cartoon: https://www.osnews.com/story/19266/wtfsm/.

And this one https://xkcd.com/1513/ (hover your mouse over the picture for extra lols)

#### Use ESLint and Prettier (if you can)

If you are coding on your phone then this tool might not be available to you.

[ ESLint](http://eslint.org/) is a quality tool that inspects code and warns a developer about potential problems. It is available online and can also be integrated into several development environments, so errors will be highlighted when writing code. It also has rules that relate to better ways of doing things to help you avoid problems.

If you install the vscode Prettier plugin then you can set it up to format your code prettily every time you hit save. This saves a lot of time.