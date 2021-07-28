# ACN syllabus

We are on a mission to support as many code schools as we can. Learn more here:

Learn more about the African Coding Network here:[African coding Network](https://www.africancoding.network/)

This syllabus is a Hugo based static site (for now). But on top of that, it is the configuration of our Tilde learning platform. You can see [Tilde](https://github.com/Umuzi-org/Tilde) for more.  

I'm sure you've heard of infrastructure-as-code, pipeline-as-code and other x-as-code things? Well, this is a syllabus-as-code. Our learning platform eats this up and generates a bunch of trello-like cards that move across the personal Kanban boards of students using the platform.

In order to make this work, we need to be strict on the shape of the syllabus files. We have very specific naming and metadata conventions that contributors need to follow. We'll talk more about that later. But let's start by getting you set up :)

This [video](https://www.youtube.com/watch?v=j5-uaSgIGI0&feature=youtu.be) will walk you trough the whole process. Or you can just read the docs.

## To contribute

We are honoured by any contributions you may want to make.
There are lots of ways to contribute. You can improve the instructions on a specific project, add extra info to some metadata, or spin up a whole new curriculum, if interested, take a minute to read our [contribution guidelines and instructions document](https://github.com/Umuzi-org/ACN-syllabus/blob/develop/contribute.md) for any information about contributing to the project.

## running locally

This is a Hugo based application.

**PLEASE NOTE** We are using hugo version 0.51. We have run into some annoying problems when upgrading hugo in the past so please just use this version.
If you are tempted to give us a PR that upgrades this to the latest version of hugo, PLEASE DONT. The plan is to upgrade this all to use Eleventy in the near future.

### initial setup

Make sure your global Github details like your username and email is set up correctly. Run the following commands in
your terminal.

```
git config --global user.name "Your username on Github"
git config --global user.email "youremail@yourdomain.com"
```

### to clone this repo

```
git clone --recursive https://github.com/UserName_on_Github/ACN-syllabus.git
```

### to get yourself set up on a Debian based machine (linux ubuntu/mint)

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

### Windows 10

Ensure you have a compatible Linux terminal for windows, if not, checkout: https://ubuntu.com/tutorials/ubuntu-on-windows#1-overview

After cloning recursively from the repo and setting up your global github email and username you can run the following 
two commands, the correct Hugo version should be installed after running the second command.

```
sudo apt install golang
./install_hugo.sh
```

### to run the development server, once it is installed

```
hugo serve -b "http://localhost:1313/"
```

That's it :) now you'll be able to poke around the main site

### setting up and running the linter a Debian based machine (linux ubuntu/mint)

Make sure you have Python3 installed. This wont work with legacy Python (python2.7 == legacy == dangerzone).
We use [Pipenv](https://pipenv.pypa.io/en/latest/) for dependency management, to install run

```
pip install pipenv
```

Once installed Pipenv will create a virtual environment and install all required packages, just run

```
pipenv install
```

To activate the environment run

```
pipenv shell
```

You should now be all set to run the linter

```
python lint.py
```

If you want to run the linter again, there's no need to do the whole setup again. Do this:

```
# activate pipenv environment
pipenv shell

# and run the linter
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

### setting up and running the linter on windows

Installing pipenv will probably be different depending on which Python you have, you must have nothing less than
Python 3.

```
pip3 install pipenv
pipenv install
```

If you get the error 'virtualenv.seed.via_app_data' after running pipenv install then you need to first do the following

```
pip3 uninstall virtualenv
pip3 install pipenv
pipenv install
pipenv shell
```

It is the 'pipenv install' command which ensures that the correct depedencies are installed from the Pipfile in the repository.
Do not install 'frontmatter' by yourself, run the 'pipenv install' command which will ensure that the correct frontmatter library
is installed. Now you can run lint.py

```
python3 lint.py
```

You can also do all of this from the terminal of an IDE like Pycharm, again you will have to ensure
that you install any dependencies from the Pipfile.  You will probably run into trouble when you try to
run hugo, make sure to set the path to hugo, eg. C:\Users\UserName\Hugo\ in your system and user path variables.
See https://www.youtube.com/watch?v=C04dlR1Ufj4\ for details.
Also, when running lint.py the 'grep' command won't work as it is not a known Windows terminal command.
Go to the lint.py file, you will need to comment out the line with the 'grep' command and rewrite using
the 'findstr' command

```
#os.system('grep -r "contentlink-missing" public')
 os.system('findstr "contentlink-missing" public')
```

DO NOT commit the changes you made to the lint.py file as this will have a massive adverse effect on everyone else
who is running lint.py from a non Windows platform.

## Syllabus Content

Look inside the content directory. The documentation is composed of a bunch of markdown files (all named `_index.md`) with a lil metadata. Ok, a lot of metadata.