---
_db_id: 261
available_flavours:
- python
content_type: project
prerequisites:
  hard:
  - topics/python-specific/sqlalchemy/migrations
  soft: []
ready: true
submission_type: repo
tags: []
title: Database migrations with SQLAlchemy
---

In this project you will practice the basics of alembic based migrations. A lot of this stuff might seem quite straight-forward now, but focus! When mygrations go wrong in production then life gets way too hard, and real user data can be put at serious risk!

This excercise will also teach you a bit more about why git is important. Make sure you commit often! Seriously! Git will save your bacon!

## Instructions

In this project you'll need 2 databases, I'll refer to them as "development" and "prod". How you set these up is up to you. You could have one docker composition that sets them both up, or (easier) you can have 2 docker compositions that are well named.

This is similar to how you would work with real databases later in life. You'll have a database on your computer that you can experiment on. If you destroy the data there then it's not a big deal at all. Your job is to keep your prod database safe.

### Using your dev database:

1. write some sql alchemy models to describe a Recruit. A recruit has the following attributes:

- first name
- surname
- chatname
- github name
- id number

2. create some migrations and run them against your dev database. Take a look inside the migration files - you wont necessarily ever need to write these things yourself, but it's good to be able to look at them and see what they mean.
3. write a small script called "create_recruits.py" that adds some new recruits to the database and run it against your dev database. Jst invent this information
4. add a new column to your sqlalchemy model for `personal_email_address`. Set it to be a required field, and must be unique
5. make your migrartions again and run them. This step wont go smoothly - you'll need to do it in a few steps.
6. Look at your migration files. They should make sense

### using your prodution database

1. run all your migrations
2. update your create_recruits script to add personal_email_address values, then run it against the prod database

This should have been quite smooth

### back to the dev db

Now a lot can go wrong with databases and migrations. Ideally the db, your models and your migrations will all be in sync. If they fall out of sync life gets kinda hard sometimes.

Generally the models should be considered the truth of things. That truth should then be propogated to the migration files, and then to the database. If the database is updated independantly then weird things start to happen.

In this secrtion we'll be updating the database independantly. In real life you wouldn' do this intentionally.

So why are we even doing this weird thing?

Basically if you are working on a team the one of your team mates migration files might disagree with yours. And you might end up in a mess. Or your migration files that work totally fine against your dev db might not work against prod because the last person to update the prod db wasn't you. This can lead to all sortf of chaos - that chaos is avoidable. But it's realy worth appreciating.

We're going to go through 3 situations. They are all nice and simple on their own. In real applications the database structure generally has many interlinking tables. Eg our Umuzi recruitment portal has 26 tables, and they're all connected to each other.

#### Situation 1: A new column

using your dev db:

1. open up a psql shell and add a new column to your database called "chort". manualy update the data - everyone is in "C25 Data Eng"
2. open a python shell and use your models to query the data. What happened?
3. now create your migrations and look at the changes. Are there any changes? What will happen if you run your migrations?
4. now go to your models and add a required cohort column
5. create your migrations and look at the changes. Did anything happen?
6. Now make a new script called "create_c26_recruits.py". USe it to add 5 random c26 recruits to your database.
7. run your script on your development database
8. Now run your migrations against your prod database. What happened?
9. run create_c26_recruits against your prod database. What happened?

Do whatever it takes to get it to work... you might need to checkout an earlier commit. By the end you'll have the C26 recruits in the prod database.

Rules: Dont delete any data in your production database! But you can completely delete your dev database if you wanted to.

#### Situation 2: A renamed column

using your dev db:

1. open up a psql shell and rename the "chatname" column to "rocketchat_user"
2. open up a python shell and try to query your db. what happened?
3. now create your migrations and look at the changes. Are there any changes? What will happen if you run your migrations?
4. now go to your models and rename the cohort column
5. create your migrations and look at the changes. Did anything happen?
6. create a new script to create some c27s and run it against your dev db
7. run your script on your development database
8. Now run your migrations against your prod database. What happened?
9. run create_c26_recruits against your prod database. What happened?

Do whatever it takes to get it to work... you might need to checkout an earlier commit. By the end you'll have the C27 recruits in the prod database.

Rules: Dont delete any data in your production database! But you can completely delete your dev database if you wanted to.

#### Situation 2: A deleted column

using your dev db:

1. open up a psql shell and delete the id number column
2. open up a python shell and try to query your db. what happened?
3. now create your migrations and look at the changes. Are there any changes? What will happen if you run your migrations?
4. now go to your models and remote the column
5. create your migrations and look at the changes. Did anything happen?
6. create a new script to create some c28s and run it against your dev db
7. run your script on your development database
8. Now run your migrations against your prod database. What happened?
9. run create_c26_recruits against your prod database. What happened?

Do whatever it takes to get it to work... you might need to checkout an earlier commit. By the end you'll have the C28 recruits in the prod database.

Rules: Dont delete any data in your production database! But you can completely delete your dev database if you wanted to.

## The End

Earlier I hinted that there are ways to prevent migration chaos. Basically what we do at Umuzi is work with a couple of rules.

1. We follow a version of the [git feature branching workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
2. We make a rule that no feature branch can include any migration files (devs add the migrations to their gitignore file)
3. The devs can then mess around with their local migrations and dev databases as much as they need to without corrupting the master branch. PRs that include any references to migrations are rejected with a snotty message
4. When it comes time to deploy the master branch migrations are generated off a real database and those migrations are pushed into the master branch