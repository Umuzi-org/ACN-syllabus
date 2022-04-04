---
_db_id: 44
content_type: topic
title: Introduction to Node and SQL
---

## Prerequisites

Before you get started with Node and Postgres you'll need to know how to use asynchronous functions. This tutorial has a great introduction

[Learn Callbacks, Promises, and Async/Await in JS by Making Ice Cream](https://www.freecodecamp.org/news/javascript-async-await-tutorial-learn-callbacks-promises-async-await-by-making-icecream/)

## Introduction

In this topic, you will learn how to connect to a PostgreSQL database using node

- node-Postgres is a collection of Node.js modules used to interact with a PostgreSQL database.
- node-Postgres has many features like callbacks, connection pooling, prepared statements, async/await, and promises.
- connection pooling allows your application to reuse existing database connections by automatically saving the connection to a pool so it can be reused instead of having to create a new connection every time data is being retrieved/accessed. An example of this can be a cache component where data is frequently accessed and stored.

## Connection pooling

### Client

[Getting started with Node & SQL using Client](https://node-postgres.com/api/client)

### Pool

[Getting started with Node & SQL using Pool](https://node-postgres.com/api/pool)

### Tutorial

[Getting started with Node & SQL tutorial using Pool](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-node-js-on-ubuntu-20-04)