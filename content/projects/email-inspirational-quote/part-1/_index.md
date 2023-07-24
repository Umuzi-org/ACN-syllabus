---
content_type: project
flavours:
- any_language
prerequisites:
  hard:
  - projects/github-api-consume/part2
  - topics/unit-testing-mocks-and-spies
  - topics/linux/os-environmental-variables
  soft: []
ready: true
story_points: 8
submission_type: repo
tags:
- mocks
- environmental variables
- smtp
title: Email random inspirational quote - part 1
---

This project is going to cover quite a lot of ground. You'll have something pretty cool by the end of it. 

## First, sign up to an email sending service

There are a lot of different email sending services around. We are using one called Brevo because it's free and easy. 

Sign up for Brevo's free plan [here](https://www.brevo.com/). Once you are logged in click on the drop down near the profile avatar at the top right of the page and click on SMTP & API. This is where you will find the SMTP settings. It'll look something like this:

```
SMTP server: ???
Port: ???
Login: ???
Password: ?????
```

Note, that SMTP isn't the most super secure way to authenticate with the email servers. We are using it because it is simple.

## Set up your environment 

Now if you want to send email from your code then you will need to make sure your code has access to your SMTP settings. You might be tempted to just copy your settings right into your code. 

**Don't do that.**

Why? Because **we don't mix code and configuration**. Your code should be able to access the configuration when it needs to. If you mix your code and your configuration then:

1. Your code wont be reusable. If anyone wants to make use of it they will need to rewrite portions of the code just to make it work with their setup. 
2. You shouldn't put secret passwords into git repos willy nilly. Unless you want to get hacked. 

### A language agnostic way to set up your environment 

Different languages have different conventions around making use of configuration variables. But these conventions mimic perfectly normal environmental variables. Environmental variables are used all over the place and it would be very useful to be very familiar with them. So that is what we'll be using here.

1. Create a file called `smtp_secrets.sh`. It should look something like this:

```
#!/bin/sh

export SMTP_SERVER=???
export SMTP_PORT=???
export SMTP_LOGIN=???
export SMTP_PASSWORD=?????
```

Please replace the ??? with your actual settings.

2. Make sure that your `smtp_secrets.sh` file is gitignored. Because it is secret.

Note that if you git commit your secrets to your git repo, then make another commit that removes the secrets, then the secrets will still be available. Anyone who has access to the repo will be able to access any commit. So anything that was committed and pushed will be there for anyone to read.

If you make the mistake of committing and pushing secrets then it's best practice to invalidate the secrets. You would need to generate a new password/token/whatever. It's a giant pain in the neck.

3. Make sure you can access your smtp_secrets from within your code. Try this out in a terminal:

```
#############################
# first load up the secrets #
#############################

source smtp_secrets.sh 

# if you aren't sure what this command means, then do some research
# understanding is golden!

#############################
# if you are running Python #
#############################
python3

# now you are in a python shell

import os
SMTP_SERVER = os.getenv('SMTP_SERVER')
print(SMTP_SERVER)

###########################
# if you are running Node #
###########################

node

# now you are in a node shell

const SMTP_SERVER = process.env.SMTP_SERVER;
console.log(SMTP_SERVER)

###########################
# if you are running Java #
###########################

jshell 

# now you are in the java shell

String env = System.getenv("smtp") | System.getProperty("smtp")
System.out.print(env)

```

Ok, what just happened?

When you open up a new terminal you are running bash (or some variation thereof). Bash is a programming language and has variables too. When you define bash variables you can choose to export them. Exporting a bash variable makes it accessible to other programs running in the same terminal.

So when we call `source smtp_secrets.sh`, bash makes a few variables and makes sure that if you launch another application then those secrets are available.

Cool eh?

## The actual project

Create a command-line program that sends a random inspirational email to an email address.

It should work like this in the different languages:

```
# if you are writing python:
python send_inspiration.py someone@email.com 

# if you are writing javascript:
npm run send_inspiration someone@email.com

# if you are writing Java 
java SendInspiration someone@email.com
```

### The quotes 

You should have a list of quotes in a JSON file. Make sure your data is structured in a consistent way. For example, if each quote has a different set of keys then that would be bad. 

Your program should grab a single quote from the file.

### The email

Make sure your email subject is sensibly chosen.

The email body should include a quote and an attribution. For example:

```
"The only true measure of success is the number of people you have helped" - Ray Dalio
```

### Errors

Raise/throw an error/exception with an appropriate message if:

- the email address argument was left out or blank
- an invalid email address is passed into your application 

### Test your work

Your unit tests should not send actual emails, but should prove that the right emails get sent. To get this right, you will need to make use of mocks or spies.

Your unit tests should not require the smtp secrets to be available as environmental variables. 

You will need to make use of mocks or spies when testing your work.

## Project structure and gotchas

### Javascript 

Make a good choice about the name.
```
├── spec
|   ├── support
|   |   └── jasmine.json
|   └── ???
├── src
|   └── ???
└── package.json
```

#### NPM run?

Remember that you need to be able to run your script like this:

```
npm run send_inspiration someone@email.com  # YES
```

NOT like this:

```
node send_inspiration someone@email.com  # NO!
```

[This](https://stackoverflow.com/questions/11580961/sending-command-line-arguments-to-npm-script) might be helpful.

#### Nodemailer 

Make use of [nodemailer](https://nodemailer.com/about/) to make it easier for yourself to send emails.

#### Imports 

An important thing to know is that importing a function shouldn't have side effects. 

If we have a script that does this:

```
function sendEmail(){
    ...
}

module.exports = { sendEmail }

sendEmail() // call the function
```

Then we import it like this in our tests:

```
{sendEmail} = require("../src/send_inspiration.js")
```
Then the sendEmail function will get called.

IMPORTING A FUNCTION IN YOUR TESTS SHOULD NOT HAVE SIDE EFFECTS!

Figure out how to structure your code so that your imports don't do weird things.

### Python 

```
├── inspirational_emails   the package under test
│   └── ???
├── requirements.txt    installation requirements
├── setup.py            installation script for the package under test
└── tests               all package tests go in this directory
    └── ???
```

Take a look at [this](https://stackoverflow.com/questions/1009860/how-to-read-process-command-line-arguments) to see a few options about how to use command-line arguments.

#### Imports 

An important thing to know is that importing a function shouldn't have side effects. 

If we have a script that does this:

```
def send_email():
    ...

send_email() // call the function
```

Then we import it like this in our tests:

```
from send_inspiration import send_email
```

Then the send_email function will get called.

IMPORTING A FUNCTION IN YOUR TESTS SHOULD NOT HAVE SIDE EFFECTS!

Figure out how to structure your code so that your imports don't do weird things.

Hint: `if __name__ == "__main__"`

### Java

Please make use of Gradle to set up your project.