---
_db_id: 
content_type: topic
ready: true
tags:
- clean-code
- sql
title: Clean Code for SQL
---

**SQL (Structured Query Language)** is mostly used to manipulate data from a relational database. A database is a container to help organize data and efficiently store and retrieve data. **Relational databases** describe the data and the relationships between data entities. 

As you advance in this career, you might find yourself having to work with a team most of the time, need to re-visit prevously-written code or better yet a potential client might want to read your code - so it is very important to write code that is understandable, logical, organized and modifiable when working with databases. 

### Script files naming
- Make sure that your script file name describes the purpose of the SQL commands it contains: `school.sql` doesn't really say much about the script file content but `insert-records.sql` does, and will make it easy for the next programmer to find the commands you used to insert table records
- File names with more than one word normally follow this format: `create_database.sql` or `create-database.sql` 
- It's good practice to separate script files according to their purpose, e.g. `create-database.sql` for the commands you use for creating a database, `create-tables.sql` for the commands for creating tables, e.t.c

### Comments

- Single-line comments start with **- -**
- Multi-line comments start with **/\*** and end with **\*/**

### SQL Expressions
`SELECT first_name FROM customers;`

It's good practice to:

- write all the SQL keywords in UPPERCASE (e.g. `SELECT` and `FROM` from the above expression)
- write all identifiers that consist of more than one name using one of these formats: `first_name` or `FirstName`)
 