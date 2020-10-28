---
title: How to Contribute
---
# Contributing to ACN-syllabus

Ready to contribute? We'd love to have you on board. In this document we'll breeze through all the conventions in place. A lot of this stuff is really friggin important. We have to be very strict on the structure of this repo otherwise Tilde wont be able to consume it. Here are some guidelines we'd like you to follow so that everything can go smoothly, Ok. Let's get cracking!

-   [Choosing something to work on](#issues)
-   [Submitting a PR](#pr)
-   [Directory structure](#ds)
-   [Naming conventions](#nc)
-   [Static resources](#sr)
-   [A note on headings](#headings)
-   [Syllabus directory](#syllabus)
-   [Understanding the frontmatter](#frontmatter)
-   [Keys and values](#keys)
-   [Flavours](#flavours)
-   [Topic specific stuff](#topic)
-   [Project specific goodies](#goodies)
-   [Depricated and unimportant](#depricated)


## <a name="issues"></a> Choosing something to work on

The first thing you should do is go to our [issues](https://github.com/Umuzi-org/ACN-syllabus/issues ) and look for something you might be interested in working on. The issues have what we call labels that help us distinguish between available and claimed issues, issues that are simple or hard and issues for hactoberfest, it is important to look at those labels before claiming and issue, labels an issue might have are:
- status/help wanted
- status/issue-claimed
- good-first-issue
- hactoberfest and 
-experienced devs only

if an issue has the `status/issue-claimed` label please skip it and if you a beginner it is advisable to start with the issues that have the `good-first-issue` label. You can assign yourself an issue by commenting your name on the comment section inside the issue or if you feel you need help with choosing an issue or you unsure of anything you can join our [discord channel](https://discord.com/channels/758708091583332382/762669571852468254) and you will get all the help you need. 

## <a name="pr"></a> Submitting a PR

1. Please always run the hugo site locally and look at the site with your eyes before making a PR. If it looks weird an buggy, broken or missing, then please fix it
2. Always run the linter before making a PR. If the linter fails then we will be sad.
3. Dont hardcode links to content. Rather use the contentlink shortcode. Eg: {{% contentlink path="topics/web-frontend/react/intro-to-react" %}}. This renders all cool like and it is meaningful to Tilde and the linter.

## <a name="ds"></a> Directory structure

All our course materials live inside the `content` directory.

There are 3 kinds of content:

- topics are self study material. For example a topic might instruct a student to go read chapter 3 of "Automate the boring stuff".
- projects are deliverables.
- workshops are instructor led events.

We used to have to seperate them all out into different directories for different things (eg: workshops all get nested under content/workshops ) but that is no longer necessary. You can add the type of content to the frontmatter. We'll talk a bit about frontmatter later.

### <a name="nc"></a> Naming Conventions

Take a look at this:

`content/projects/redux-intro/part-1/_index.md`

- all the directory names are `words-seperated-with-dashes`
- all the markdown files are called `_index.md`


### <a name="sr"></a> Static resources

We're all about that high cohesion life. So if there is an image that has something to do with a specific \_index.md file, put it in the same directory as that file.

For example, look at this directory:

```
content/topics/kotlin/internet-data-and-images
```

### <a name="headings"></a> A note on headings

This is best shown with an example. Consider the following:

```
---
title: Redux
---

# Introduction

Blah blah

```

Hugo will generate the following html:

```
<h1>Redux</h1>
<h1>Introduction</h1>
```

That's 2 h1 elements in a row. This looks pretty bad. Please dont do that!

This is better:

```
---
title: Redux
---

## Introduction

Blah blah

```

This results in:

```
<h1>Redux</h1>
<h2>Introduction</h2>
```

A heading and a subheading. Much nicer!


### <a name="syllabus"></a> Syllabus directory

This directory is a special case. It doesn't have `index.md` files but rather has different `.md` files representing the different learning paths people can go through.

- If a file name starts with `_` then that means it is a draft.
- Tilde basically looks for contentlinks. The order of the contentlinks matters of course
- Anything that isn't a contentlink will get ignored by Tilde
- There should be maximim one contentlink per line

## <a name="frontmatter"></a> Understanding the frontmatter

You'll see that every piece of content in this repo has an `\_index.md` file. Those files are broken down into 2 parts. Frontmatter and content.

The content is perfectly normal markdown.

The frontmatter is yaml. Yaml has it's own syntax. Indentation is super duper important with yaml.
For example, the two samples below mean very different things

```
# 1

prerequisites:
  hard:
  - topics/redux-intro

# 2

prerequisites:
hard:
  - topics/redux-intro

```

If we were to convert them to json:

```
# 1

{
  prerequisites: {
    hard: ['topics/redux-intro']
  }
}

# 2

{
    prerequisites: null,
    hard: ['topics/redux-intro']
}

```

### <a name="keys"></a> Keys and values

The frontmatter is basically a bunch of key-value pairs. Some of the values are lists, or further key-value pairs. Some are optional, some are not.

Here they are:

#### <a name="simple"></a> The simple ones:

- \_db_id: Please don't touch this it's the database id of this content. It gets filled in automagically. Don't fill it in yourself. Don't even mention it in your content.
- content_type: is a workshop, a topic or a project?
- ready: if true then this content is fit for human consumption. The default is false. If theis is false then contentlinks to this page will have `[TODO]` in the text.
- prerequisites: what should the student do before this content. Mention the `hard` prerequisites only.
- tags: sortof like how you tag your stackoverfow questions.
- story_points: agile weights


#### <a name="flavours"></a> Flavours:

Some projects can be done in js or typescript. Some projects can be done in any language. Some can be done in any frontend framework. Some are specfic to Angular and typescript.This is where you specify what is available. All the flavour names that are allowed can be seen in `flavours.yaml`. You can take any combination of the strings in this file.

The available flavours are specified in `available_flavours`.

#### <a name="topic"></a> Topic specific stuff

Generally Topics turn into Tilde cards that the student can just move to complete on their own. But sometimes we want a staff member to check on the student and make sure that they did the work to a high enough quality.

`topic_needs_review: true` can be added to a topic's frontmatter to signify this.

#### <a name="goodies"></a> Project specific goodies

The `submission_type` says what form the project should take and describes how the Tilde cards should behave. It can have the following values:

- `repo`: this means that when the student starts the project then Tilde will create a repo for them, protect the main branch and add the student as a collaborator. The student now has to get cracking by making some PRs
- `continue_repo`: For example part 2 of a project might use the same repo as part 1.

An example of `continue_repo`:

```
content_type: project
submission_type: continue_repo
from_repo: projects/memory-game/part-1  # this is the repo it should be using
prerequisites:
  hard:
    - projects/memory-game/part-1   # therefore part-1 is a hard-prerequisite
```

- `link`: The student just needs to give us a link to their work.

Note: All projects need to list `available_flavbours`! And whenever you make a contentlink to a project from a syllabus page, you need to pick the relevant flavours.

For example:

```
Web devs ned to do this:
- {{% contentlink path="projects/oop/animals/part2"  flavour="javascript" %}}

And data engineers should rather do this
- {{% contentlink path="projects/oop/animals/part2"  flavour="python" %}}

You can also pick multiple flavours, like so:
- {{% contentlink path="projects/memory-game/part-2" flavour="react,redux" %}}

```

#### <a name="depricated"></a> Depricated and unimportant

If something is not on this list then it probably isn't important, or is irrelevant to most users.
If something on this list isn't too detailed, please look for examples in the code base, a lot of things can be understood through simple pattern matching.

Ignore the following, they are silly and will be removed:

- weight: this is a hugo thing that describes the order of things in the page sidebar. It really doesn't matter
- prerequisites - soft: We don't actually use these
