---
title: SQL Library excercise
content_type: project
submission_type: repo
tags:
  - sql
flavours: 
  - postgres
---

## Introduction

You've heard of Libraries right? In the old times people used to go to libraries to borrow books made out of dead trees. Libraries need to keep track of a lot of stuff. Let's see if you can figure out how to use an SQL database to manage a Library's info.

## A note on pull requests

Many small PRs are better than one big one. You are more likely to be successful if you get rapid feedback.  This exercise should have 3 PRs.

## Resources

If your SQL is a lil rusty we got you. Or rather, these guys got you:

- https://www.sololearn.com/learning/1060
- https://www.w3schools.com/sql/

You're going to need to know how to make tables, how foreign keys work, and some select statements and joins.

## First we need some tables

Before we can use a database, we'll need to define some table structures. Please create a script that can be executed to create all the tables we need. We'll need to represent the following information:

### Books

Every book has the following attributes (columns):

- title
- author
- description
- an author

Ok, some books in real life have more than one author. But to keep things simple let's just pretend that one book only has one author.

### Authors

Every author has:

- first name
- last name
- nationality (this is an enumeration)

### Keeping it simple

Of course a library is way more complicated than this - there are people who borrow books and owe fines and membership fees and all sorts of things. But for now we want the bare basics. So that's it for now. Just books and authors. And one book only gets one author.

### Make a PR

Get some feedback on what you have done so far!

## Insert some data

Write a script that populates your database.

1. Create at least 5 authors
2. Create at least 10 books

## Queries

Make another script. Please write queries to achieve the following:

1. count how many books there are in total
2. find out which author has the most books
3. find out how many books there are according to nationality, eg maybe there are 5 books from South African authors and 3 books from Hong Kong

