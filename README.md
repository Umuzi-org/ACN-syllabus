# ACN syllabus

We are on a mission to support as many code schools as we can. Learn more here:

Learn more about the African Coding Network here:
https://www.africancoding.network/

This syllabus is a Hugo based static site (for now). But on top of that, it is the configuration of our Tilde learning platform. You can see Tilde here: https://github.com/Umuzi-org/Tilde

I'm sure you've heard of infrastructure-as-code, pipeline-as-code and other x-as-code things? Well, this is a syllabus-as-code. Our learning platform eats this up and generates a bunch of trello-like cards that move across the personal Kanban boards of students using the platform.

In order to make this work, we need to be strict on the shape of the syllabus files. We have very specific naming and metadata conventions that contributors need to follow. We'll talk more about that later. But let's start by getting you set up :)

This video will walk you trough the whole process. Or you can just read the docs.

https://www.youtube.com/watch?v=j5-uaSgIGI0&feature=youtu.be

## To clone this repo

There is a submodule in here so clone recursively:

Eg:

```
git clone --recursive git@github.com:Umuzi-org/ACN-syllabus.git
```

## running locally

This is a Hugo based application.

**PLEASE NOTE** We are using hugo version 0.51. We have run into some annoying problems when upgrading hugo in the past so please just use this version.
If you are tempted to give us a PR that upgrades this to the latest version of hugo, PLEASE DONT. The plan is to upgrade this all to use Eleventy in the near future.

### To get yourself set up on a Debian based machine (linux ubuntu/mint)

```
sudo apt install golang
./install_hugo.sh
```

### MAC

Add this in your bash file e.g .zshrc or .bashrc

```
# Go development
export GOPATH="${HOME}/.go"
export GOROOT="$(brew --prefix golang)/libexec"
export PATH="$PATH:${GOPATH}/bin:${GOROOT}/bin"
```

Run these installs in your terminal using Homebrew

```
brew install go
brew install hugo -> look for version 0.51
```

### To run the development server, once it is installed

```
hugo serve -b "http://localhost:1313/"
```

That's it :) now you'll be able to poke around the main site

### Setting up and running the linter with using Pipenv

Make sure you have Python3 installed. This wont work with legacy Python (python2.7 == legacy == dangerzone).

```
# with Pipenv installed there is no need to create a virtual environment, so go ahead and install it if you haven't already
pip install pipenv

# Pipenv will automatically create a virtual environment and install all required packages for this repo, simply type the following
pipenv install

# activate Pipenv virtual environment and run the linter
pipenv shell
python lint.py

# to install any new packages simply use pipenv and it will install and automatically update the Pipfile and Pipfile.lock  with the newly 
# installed package
# for example, if you want to install pandas:
pipenv install pandas

```

Then if you want to run the linter again, you dont need to run pipenv install. Do this:

```
# activate pipenv environment and run the linter
pipenv shell
python lint.py

```

The linter starts off by looking over all the frontmatter and making sure that's fine. Then it builds the site and looks for trouble.

Some error messages are a bit funny looking. If you see something like this:

```
content/projects/django-airbnb-clone/users-can-crud-properties/_index.md has unrecognized frontmatter: reatdy
```

Then it means that there is a typo in the given file.

And then if you get a message like this:

```
public/syllabuses/data-eng-boot/index.html:  <span class="contentlink-missing" data="topics/intro-to-tilde"
```

Then that means there is a contentlink that is pointint to a file that doesn't exist. Did the file move? Was it deleted? Is something misspelled?

## Syllabus Content

Look inside the content directory. The documentation is composed of a bunch of markdown files (all named `_index.md`) with a lil metadata. Ok, a lot of metadata.

## Contributing

There are lots of ways to contribute. You can improve the instructions on a specific project, add extra info to some metadata, or spin up a whole new curriculum :)

Please take a look at contribute.md. It will tell you all.
