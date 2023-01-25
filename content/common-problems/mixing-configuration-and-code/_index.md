---
title: Mixing code and configuration
content_type: topic
---

Learners often do this kind of thing in their code:

```
DATABASE_HOST = 'localhost'
DATABASE_PORT = '6543'
```

Why is this bad?

## It's bad for teamwork

This is bad practice for a number of reasons. First of all let's imagine yo uare working with a team mate on a legit professional project. Your team mate has something else running on port 6543 and they want to use port 7654 for this project. 

They would need to edit the code to make the configuration match their local environment. When they commit their code and get their PR merged then the project will no longer work on your computer. 

If anyone ever says "but it works on my computer" then this it the first thing you should be looking into. The configuration might be hard-coded so that it only works on computers that have a very specific set up.

## It's bad for documentation

Often when this happens you'll find all the different configuration variables scattered around the code base randomly as though they were perfectly normal variables. This would cause problems because it would be hard to discover where things would need to be tweaked in order to get the code to run in a different environment. 

## It's bad for staging and production use

If you deploy a project into a production environment then it's definitely not going to be set up in the same way as your computer. Eg: If you are writing code locally then you might have a throwaway dev database running on your localhost. In a prod environment the database will be running at a totally different IP address.

On top of that, code typically gets deployed to a staging environment before it gets deployed to prod. And the staging environment is likely to have it's own database with yet another IP address.

So that means you'll be working with at least 3 IP addresses: one for your dev database, one for staging and one for prod.

If your database was configured randomly within your code base you would need to have 3 different versions of your code to run in the different environments. That's a bit nuts. We have better tools for this.

## Good practice

1. Either use standard environmental variables or something like dotenv to feed configuration variables into your program.
2. Have a central file that grabs the configuration values from the environment
3. Name your variables in a consistent and meaningful way
4. Make use of sensible default values to make the dev experience nice. Eg if you are running a dev database using a docker composition that is inside your repo then you can set up your config so that your code will just work against the dev database without any pain and suffering
5. Just import the configuration wherever it is needed 

eg:

```
// config.py

DATABASE_HOST = os.getenv('DATABASE_HOST','localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT','6543')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'supersecret')

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST','localhost')
...
```

In other languages this would be similar. Eg in JavaScript you would use `process.env` instead of Python's `os.getenv`. The syntax is a bit different for different languages but the concepts are the same.