---
title: How to Contribute
---

If you want to contribute content to this repo there are a few things you need to know.

Firstly, this is a [Hugo](https://gohugo.io/) based web site. If you are contributing to the content of this site you will be editing markdown files. So you wont need to know too much about how Hugo works in order to be effective. If you need to figure out the mechanics of this thing, best read the Hugo docs.

## Understanding the frontmatter

You'll see that every piece of content in this repo has an \_index.md file. Those files are broken down into 2 parts. Frontmatter and content.

The content is perfectly normal markdown.

The frontmatter is yaml. Yaml has it's own syntax, indentation matters. Best be familiar.

The frontmatter is basically a bunch of key-value pairs. Some of the values are lists, or further key-value pairs. Some are optional, some are not. Here they are:

If something is not on this list then it probably isn't important, or is irrelevant to most users.
If something on this list isn't too detailed, please look for examples in the code base, a lot of things can be understood through simple pattern matching.

- \_db_id: Please dont touch this :) it's the dataase id of this content. It gets filled in automagically
- content_type: for now this is not compulsory, it'll get filed in automatically. Basically we are trying to make the structure of the syllabus a bit more flexible
- ready: if true then this content is fit for human consumption
- prerequisites: what should the student do before this content.
- tags: sortof like how you tag your stackoverfow questions
- story_points: agile weights
- available_flavours: this one is a bit more involved. Some projects can be done in js or typescript. Some projects can be done in any language. Some projects can be done in

## First you need to get yourself set up

You'll notice a link to our GitHub repo in the menu on the left. See it? Cool. You'll need to fork that.

There are installation instructions in the README.

Once you have made your changes then:

1. Run the application on your local computer and look at the changes and make sure they are nice looking.
2. Make a pull request. Your pull request should have a nice description of what you are trying to do
3. If it looks like nobody has noticed your pull request then slack one of the tech team members. Feel free to remind us of your contribution

## Don't make any changes to the public/ directory

This is really important. It might be tempting to you to write some HTML, js or css in there. Resist that temptation. This is a Hugo based website. This means that the public directory is generated auto-magically. Any changes you make within the public directory will be overwritten.

## If you want to make changes to look and feel or basic site functionality

This gets interesting. Basically, Hugo allows the use of themes. The theme we are using is called `Hugo-theme-learn` and you can find it inside the `themes` directory in this repo. So most of the visual elements you see when looking at this website is generated through use of that theme.

If you want to override anything about how the theme behaves (maybe changing a colour or layout, or adding a functionality) then DO NOT directly edit the theme files.

If you want to change how a theme behaves then you need to override that behaviour WITHOUT directly editing the theme.

Take a look at this directory structure:

```
.
├── archetypes
├── config.toml
├── content
├── install_Hugo.sh
├── layouts
├── LICENSE.md
├── public
├── README.md
├── resources
├── static
└── themes
    └── Hugo-theme-learn
        ├── archetypes
        ├── CHANGELOG.md
        ├── exampleSite
        ├── i18n
        ├── images
        ├── layouts
        ├── LICENSE.md
        ├── netlify.toml
        ├── README.md
        ├── static
        ├── theme.toml
        └── wercker.yml
```

This is a summary of the directory structure of this application. You'll notice that the structure of the theme is very similar to the structure of the repo as a whole. If you want to override a piece of the theme's functionality then you need to find the file in the theme that defines that functionality, then make a file with an equivalent path in the main repo. This might sound weird but it's pretty easy to get the hang of.

Have an example:

Let's say we want to change what the menu looks like. You would do something like this:

```
cp themes/Hugo-theme-learn/layouts/partials/menu.html layouts/partials/menu.html
```

Cool, so now we have two copies of `menu.html`. Make your changes to the new one.

```
...
├── config.toml
├── layouts
|   └── partials
|       └── menu.html  ### EDIT THIS ONE
...
└── themes
    └── Hugo-theme-learn
        ├── layouts
            └── partials
                └── menu.html ### NOT THIS ONE
    ...
```

Nice eh?

The other thing to know is that Hugo is written in go. So these html files are actually go templates. So that's a topic you can read about on your own. Go templates are used in lots of interesting places.

## The syllabus index page

When you are running the development server (`Hugo serve`) then you can see this page [here](http://localhost:1313/syllabuses/). This is where each supported curriculum is outlined, week by week.

Take a look at the contents of [week 1](http://localhost:1313/syllabuses/#week-1-linux).

You will notice that the links there have a pretty consistent format. Eg:

```
WORKSHOPS: How to be a professional
TOPICS: [TODO] Introduction to Linux
PROJECTS: [TODO] Linux INTRO
```

If you look at the markdown file ('content/syllabuses/\_index.md') you can see that these links are generated by using the `contentlink` shortcode.

Eg: {{% contentlink path="workshops/how-to-be-a-professional" %}}

(take a look at this page's markdown and take a look at what happened above)

This shortcode does a few things:

- it makes the link work
- it checks the type of the linked to content and writes it down (eg: `WORKSHOPS`)
- it checks the `title` of the linked to content and writes it down (eg: `How to be a professional`)
- it (sometimes) adds a `[TODO]`. If the markdown file is marked as "ready" then the `TODO` wont show up.

Eg looking at workshops/how-to-be-a-professional. If the frontmatter looks like this:

```
---
title: How to be a professional
ready: true
---
```

Then the TODO wont show up.

This functionality is here just so that we can explicitly mark which content we are happy with so we can properly direct our efforts. Once the syllabus is ready as a whole then the TODO functionality will be removed.

## If you want to make changes to the course content

All of the content displayed on the website comes from the `content` directory. You'll notice a bunch of different directories inside content, each of these directories has a purpose. Try to put your stuff in the right place.

Here are a few major kinds of content:

- WORKSHOP == instructor led event.
- TOPIC == self study material
- PROJECT == deliverable

Let's say you want to make a new TOPIC entitled "Intro to BeautifulSoup". What you will need to do is this:

Create a new file here: `content/topics/python-specific/intro-to-beautifulsoup.md`. Then add come content and make sure to include a title in your frontmatter/metadata:

```
---
title: Intro to Beautifulsoup
---

Your content goes here.

## some heading

blah blah blah
```

Once you have saved your file then you should be able to see it in the it in the menu panel on the left hand side of the website.

And you can make a content link to your new file like this:

## Advanced frontmatter

So you know how to specify a title in your frontmatter, there are a few more things to know about.

- weight: this effects the order of things as they show up in the menu on the left-hand side of the screen. Menu items are sorted in ascending weight order
- pre: This is stuff that shows up before the title in the menu on the left
- ready: we spoke about this earlier

The only really compulsory thing is the title.

Here is the frontmatter of the `content/syllabuses/_index.md`

```
---
title: Syllabus
pre: "<b>1. </b>"
weight: 1
---

```

- since the weight is 1 this item shows up as the first item in the menu on the left
- the menu item is rendered with HTML something like this: `<b>1. </b> Syllabus`

## Advanced folder structure

If you wanted to create a new section with subsections then you would be able to do that too. Experiment a little bit if you need to. Basically do something like this:

```
└── content/
    └── topics/
        ├── beautifulsoup/
            ├── _index.md
            ├── intro.md
            ├── advanced.md
            ├── something_else/
                ├── _index.md
```

You can also use this kind of folder structure if you want to include other resources in your markdown. For example a diagram or witty gif.

## What not to include

Please don't include large binary files in the repo. Just link to that sort of thing. This includes PDFs, presentations, videos and other documents.
