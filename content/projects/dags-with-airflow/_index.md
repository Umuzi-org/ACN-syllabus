---
_db_id: 286
available_flavours:
- python
content_type: project
prerequisites:
  hard:
  - projects/rabbitmq
  soft: []
ready: true
submission_type: repo
tags:
- apache-airflow
title: DAGs with Airflow
---

Create a dag that does the following:

1. Grab all the open pull requests that exist on all the github repos you have access to and store them in a database. This should be a single task in your DAG
2. For each pull request, get the timestamp of the latest review and store that in the database. This should be a single task in your DAG
3. Send an email to yourself that shows the top 5 PRs that need attention in order of priority. If there are less than 5 PRs then just show those.

How do you know if a PR needs attention? Basically the quicker a PR is merged the better. If a PR just sits and gets ignored then the code inside it is completelly useless. And the longer it waits the harder it will be to merge. In general, you should always put effort towards finishing things instead of starting new things.

And how do you send an email? Sendinblue is pretty easy to work with. So is MailChimp

Also please note, Airflow has a database of its own. This uses sqlite by default. You need to store your PRs in a different database.

## Up for a challenge?

Try using RabbitMQ to get Step 2 to run as a bunch of parallel tasks by making a few worker processes do api calls to Github.

## Some success crieria

- Be careful about your .gitignore. Airflow creates a few files that you really shouldn't be sharing
- Create a README that explains how to set up your project. Getting your stuff to run should be easy