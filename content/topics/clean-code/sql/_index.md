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

As you advance in this career, you might find yourself having to work with a team most of the time, need to re-visit previously-written SQL code or better yet a potential client might want to read your code - so it is very important to write code that is understandable, logical, organized and modifiable when working with databases. 

### Script files naming
- Make sure that your script file name describes the purpose of the SQL commands it contains: `school.sql` doesn't really say much about the script file content but `insert-records.sql` does, and will make it easy for the next programmer to find the file containing the commands you used to insert table records
- SQL script file names normally follow this format: `create_tables.sql` or `create-tables.sql` 
- It's good practice to name script files according to their purpose, e.g. `create-tables.sql` for the commands you use for creating tables, `insert-records.sql` for the commands used for inserting records, e.t.c

### Comments

- Single-line comments should start with **- -**
- Multi-line comments should start with **/\*** and end with **\*/**

### SQL Expressions

```
INSERT INTO customer (first_name, last_name)
VALUES ('John', 'Doe');
```

```
SELECT first_name 
FROM customer;
```

It's good practice to:

- write all the SQL keywords in UPPERCASE
- write all the identifiers using one of these formats: `customer` or `first_name`
- have a semi-colon `;` at the end of an expression

### Indentation, Alignment and Consistency
Example of bad indentation:
```
SELECT clients.id, clients.first_name, places.province FROM clients INNER JOIN places ON places.client_id = clients.id  WHERE province = 'Free State';
```

Example of good indentation:
```
SELECT 
    client.id, 
    client.first_name, 
    place.province 
FROM client 
INNER JOIN place ON place.client_id = client.id  
WHERE province = 'Free State';
```
```
SELECT client.id, place.province 
FROM client 
INNER JOIN place ON place.client_id = client.id  
WHERE province = 'Free State';
```

Remember, good SQL code is easy to read and understand.

### Databases
If you're creating a school database, name it `school` instead of just `database`

### Tables and table columns
- Name a table using a singular instead of plural, i.e. `customer`, `account`, e.t.c 
- Primary key column: It's good practice to name this column as just `id`
- Foreign key column: Use the specific table's name and a "id" e.g. `customer_id` - that way it easily references the foreign key to the `customer` table 


 