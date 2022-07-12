---
_db_id: 230
content_type: project
flavours:
- any_language
prerequisites:
  hard:
  - topics/unit-testing-mocks-and-spies
  - topics/linux/os-environmental-variables
  soft: []
ready: true
story_points: 8
submission_type: repo
tags:
- tdd
- mocks
- environmental variables
- smtp
title: Email random inspirational quote
---

This basic project should demonstrate your understanding of mocks/spies.

We'll be making an application that sends emails.

## Set up

Step 1 is to sign up for [SendinBlue](https://www.sendinblue.com/). You can sign up for the free plan. Once you are logged in click on the "Transactional" tab at the top of the page. You'll see some SMTP settings. It'll look something like this:

```
SMTP server: smtp-relay.sendinblue.com
Port: 587
Login: ???
Password: ?????
```

Note, that SMTP isn't the most super secure way to authenticate with the email servers. But it's the simplest way. For now, let's keep it simple. We're here to practice unit testing.

Take these settings and save them in a shell script called `smtp_secrets.sh`. It should look like this.

```
#!/bin/sh

export SMTP_SERVER=smtp-relay.sendinblue.com
export SMTP_PORT=587
export SMTP_LOGIN=???
export SMTP_PASSWORD=?????
```

Why? Because **we don't mix code and configuration**. Your code should be able to access the configuration when it needs to.

Now add the following line to your `.gitignore` file:

```
smtp_secrets.sh
```

Why? Because these credentials should be kept secret. If you commit them to your git repo and push it to Github then anyone who has access to your repo can read your secrets and start sending emails from your account.

This remains true even if you make a commit that removes the secrets from the repo.

So far so good.

Now try this out in the terminal

```
source smtp_secrets.sh

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

java

String env = System.getenv("smtp") | System.getProperty("smtp")
System.out.print(env)

```

Ok, what just happened?

When you open up a new terminal you are running bash (or some variation thereof). Bash is a programming language and has variables too. When you define bash variables you can choose to export them. Exporting a bash variable makes it accessible to other programs running in the same terminal.

So when we call `source smtp_secrets.sh`, bash makes a few variables and makes sure that if you launch another application then those secrets are available.

Cool eh?

If you want some further reading check this out: {{% contentlink path="topics/linux/os-environmental-variables" %}}

## The actual project

Write a program that sends a random inspirational quote to an email address. The email address should be a command-line parameter passed to the program.

You should have a list of quotes in a file by itself. Your program should grab one and send the email.

Your final email quotes should be formatted like this:

```
"The only true measure of success is the number of people you have helped" — Ray Dalio
```

### Node

After `npm init` you should add your script to `package.json`. Look for `scripts` inside the file.

you should be able to do the following:

```
npm run send_inspiration ...
```

The command needs to allow you to pass in an email address from the command line. Take a look at [this](https://stackoverflow.com/questions/11580961/sending-command-line-arguments-to-npm-script)

Also, note that good code is written to be reusable. Make sure all your executable code is inside useful functions. When we run `npm run send_inspiration` then the right functions will need to be executed.

### Python

You should be able to run your code using

```
python send_inspiration.py ...
```

The command needs to allow you to pass in an email address from the command line. Take a look at [this](https://stackoverflow.com/questions/1009860/how-to-read-process-command-line-arguments)

Go with the simplest option you can find initially - because [KISS](https://en.wikipedia.org/wiki/KISS_principle)

Also, note that good code is written to be reusable. Make sure all your executable code is inside useful functions. When we run `npm run send_inspiration` then the right functions will need to be executed.

### Java

Running it as part of your main application should be ok

## Testing your project

Your unit tests should make sure that when the application runs then it sends one email with one quote to one person.

If your tests

- send actual emails
- require your SMTP secret values

then they are wrong.

Please make sure that you understand what mocks and spies are for when writing your tests. These things do not exist to take up space, waste time or look fancy. They do have a purpose.

If you do anything that looks like the following pseudocode then you are doing it wrong;

```
spyOn(myFunction)
myFunction()
assert myFunction.wasCalleOnce
```

Here is a useful way to think about mocks and spies:

Sending emails is considered "expensive". Why? Because it costs actual money if you do it in bulk. Also, it costs time. It is not a fast and free operation. But it is an important operation.

You need to test that when you want to send an email then:

1. the function that sends emails gets called
2. it gets called once, not twice
3. it is called correctly, with the correct arguments

You don't want your unit tests to send emails. You just want them to prove that the part of your machine that sends emails is being used correctly.

As another example, if you were developing a "forgot password" or "confirm email address" function for a website then you would test pretty much the same thing. You need to make sure that the correct functionality gets evoked, without actually sending anything.

## Bonus fun stuff

- Set up a cron job so that your program sends you a bit of inspiration every weekday at the same time. You can start your day with inspiration. Or you can receive your email just before you go to lunch or go home so that you have something to ponder.
- You can also add extra functionality. Eg: send an inspirational quote and a funny quote.
- You can make the emails that get sent look good as well. it doesn't just need to be plain text
- You can look into sending SMS instead of email
- link to the quote author's Wikipedia page straight from the email/SMS
- add extra information such as a weather report


## Instructions for a reviewer

- Unit tests:
 - The learner should demonstrate that the email sends only once, with the correct arguments.
 - The learner should demonstrate an understanding of mocks and spies. Please see {{% contentlink path="topics/unit-testing-mocks-and-spies" %}} .

- Sending emails to multiple recipients is not a requirement, but if the code is structured well enough, then doing so should be easy. The unit test should demonstrate that the code is not restricted to sending just one email.