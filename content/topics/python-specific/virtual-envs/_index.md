---
_db_id: 165
content_type: topic
ready: true
title: Virtual Environments
---

A good solid underatanding of virtual environments is critical to any serious Python developer. The purpose of a virtual env is "isolation of dependencies". This will probably sound confusing but I'll explain with an example.

Lets say you are working on two seperate python projects on your computer.

Your first project is a legacy project. It's pretty old and you are trying to get it to work with modern python. It relies heavily on an ooooold version of `requests`. And your second project is hip with the times, it also relies on `requests` but it is using the latest and greatest version.

If you could only install one version of `requests` then you would only be able to run one of those two projects on your computer. Which sucks.

Virtual environments let you isolate your projects from each other so they each have their own seperate copies of dependencies.

Please read this primer: https://realpython.com/python-virtual-environments-a-primer/

## Some important concepts and cool tricks

A virtualenv is really just a diretory with a bunch of python stuff inside it.

Every virtual env has it's own instance of the Python executable. So if you have a `python3.8` venv and it is active and you type in `python` it will run `python3.8`. If you type `python3` then it will also run `python3.8`. Same thing with pip.

## A really handy trick

Whevever you activate a virtualenv it runs a script called `activate`. This is a plain simple bash script. This means you can put extra stuff in there. It's very useful for setting up environmental variables,you can `export` your variables near the top of your activate script to make sure they are always available on your development machine.

For example, let's say you are writing a program that sends emails. And in order to send the emails the program needs to be able to authenticate using a keyfile.

Your python code could maybe be something like this:

```
import os
from some_cool_email_service import Client

PATH_TO_EMAIL_KEY = os.environ['PATH_TO_EMAIL_KEY'] # if the variable is not set then this will raise a KeyError
client = Client()
client.authenticate_with_key_file(PATH_TO_EMAIL_KEY)
client.send_email(
    subject="winning!",
    message="something really quite witty",
    etc
)
```

To get this code to work you would need to activate your venv, and make sure that the environmental variable is set up.

```
source /path/to/your_environment/bin/activate

python your_script.py
# This gives us a KeyError

export PATH_TO_EMAIL_KEY=`/something/local/on/your/machine`
python your_script.py
# yay! it works
```

You can also just add this to the top of your virtualenv bin/activate script.

```
export PATH_TO_EMAIL_KEY=`/something/local/on/your/machine`
```

Then you'll be able to do this:

```
source /path/to/your_environment/bin/activate
python your_script.py
# yay! it works
```

## Latest and greatest tooling

Ideally in serious projects you should be using a tool called `pipenv`. This probably wont make sense until you understand virtualenvironments. It feels very similar to `npm` and `yarn` for those of you with a JavaScript background.

This guide explains it nicely: https://realpython.com/pipenv-guide/

## Our expectations of you

- We expect you to be using modern python
- normal virtual environments are fine. But if you want to use virtualenvwrapper or pipenv that would be fine
- if you git commit your virtualenv on any of your projects then you wont be marked as competent. The best you'll be able to hope for is "not yet competent"
- use python 3. Python 2.7 is legacy python