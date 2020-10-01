---
_db_id: 230
available_flavours:
- any_language
content_type: project
prerequisites:
  hard:
  - topics/unit-testing-mocks-and-spies
  - topics/linux/os-environmental-variables/
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

We'll be making an application that ends emails.

## Set up

Step 1 is to sign up for [SendinBlue](https://www.sendinblue.com/). You can sign up for the free plan. Once you are logged in click on the "Transactional" tab at the top of the page. You'll see some SMTP settings. It'll look something like this:

```
SMTP server: smtp-relay.sendinblue.com
Port: 587
Login: ???
Password: ?????
```

Note, SMTP isn't the most super secure way to authenticate with the email servers. But it's the simplest way. For now let's keep it simple. We're really here to practice unit testing.

Take these settings and save them in a shell script called `smtp_secrets.sh`. It should look like this.

```
#!/bin/sh

export SMTP_SERVER=smtp-relay.sendinblue.com
export SMTP_PORT=587
export SMTP_LOGIN=???
export SMTP_PASSWORD=?????
```

Why? Because **we don't mix code and configuration**. Your code should be able to access configuration when it needs to.

Now add the following line to your `.gitignore` file:

```
smtp_secrets.sh
```

Why? Because these credentials should be kept secret. If you commit them to your git repo and push it to github then anyone who has access to your repo can read your secrets and start sending emails from your account.

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
```

Ok, what just happened?

Basically when you open up a new terminal you are running bash (or some variation thereof). Bash is a programming language and has variables too. When you define bash variables you can choose to export them. Exporting a bash variable makes it accessable to other programs running in the same terminal.

So when we call `source smtp_secrets.sh`, bash makes a few variables and makes sure that if you launch another application then those secrets are available.

Cool eh?

If you want some further reading check this out: {{% contentlink path="topics/linux/os-environmental-variables" %}}

## The actual project

Write a program that sends a random inspirational quote to an email address. The email address should be a command-line parameter passed to the program.

You should have a list of quotes in a file by itself. Your program should grab one and send the email.

Your final email quotes should be formatted like this:

```
"The only true measure of success if the number of people you have helped" — Ray Dalio
```

### Node

After `npm init` you should add your own script to `package.json`. Look for `scripts` inside the file.

you should be able to do the following:

```
npm run send_inspiration ...
```

The command needs to allow you to pass in an email address from the command line. Take a look at [this](https://stackoverflow.com/questions/11580961/sending-command-line-arguments-to-npm-script)

### Python

you should be able to run your code using

```
python send_inspiration.py ...
```

The command needs to allow you to pass in an email address from the command line. Take a look at [this](https://stackoverflow.com/questions/1009860/how-to-read-process-command-line-arguments)

Go with the simplest option you can find initially - because [KISS](https://en.wikipedia.org/wiki/KISS_principle)

## Testing your project

Your unit tests should make sure that when the application runs then it sends one email with one quote to one person.

If your tests

- send actual emails
- require your smtp secret values

then they are wrong.

## Bonus fun stuff

- Set up a cron job so that your program sends you a bit of inspiration every week day at the same time. You can start your day with inspiration. Or you can recieve you email just before you go to lunch or go home so that you have something to ponder.
- You can also add extra functionality. Eg: send an inspirational quote and a funny quote.
- You can make the emails that get sent look good as well. it doesn't just need to be plain text
- You can look into sending sms instead of email
- link to the quote author's wikipedia page straight from the email/sms
- add extra information such as a weather report