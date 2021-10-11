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

As you advance in this career, you might find yourself having to work with a team most of the time, need to re-visit prevously-written SQL code or better yet a potential client might want to read your code - so it is very important to write code that is understandable, logical, organized and modifiable when working with databases. 

### Script files naming
- Make sure that your script file name describes the purpose of the SQL commands it contains: `school.sql` doesn't really say much about the script file content but `insert-records.sql` does, and will make it easy for the next programmer to find the file containing the commands you used to insert table records
- File names normally follow this format: `create_database.sql` or `create-database.sql` 
- It's good practice to separate script files according to their purpose, e.g. `create-database.sql` for the commands you use for creating a database, `create-tables.sql` for the commands used for creating tables, e.t.c

### Comments

- Single-line comments should start with **- -**
- Multi-line comments should start with **/\*** and end with **\*/**

### SQL Expressions

```
INSERT INTO customers (first_name, last_name)
VALUES ('John', 'Doe');
```

```
SELECT first_name 
FROM customers;
```

It's good practice to:

- write all the SQL keywords in UPPERCASE
- write all the identifiers using one of these formats: `customers`, `first_name` or `FirstName`)
- have a semi-colon `;` at the end of an expression

### Indentation, Alignment and Consistency
Example of bad indentation:
```
SELECT clients.id, clients.first_name, places.province FROM clients INNER JOIN places ON places.client_id = clients.id  WHERE province = 'Free State';
```

Example of good indentation:
```
SELECT 
    clients.id, 
    clients.first_name, 
    places.province 
FROM clients 
INNER JOIN places ON places.client_id = clients.id  
WHERE province = 'Free State';
```

Remember good SQL code is easy to read and understand.



 