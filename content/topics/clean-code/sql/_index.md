---
_db_id: 733
content_type: topic
ready: true
tags:
- clean-code
- sql
title: Clean Code for SQL
---

**SQL (Structured Query Language)** is mostly used to fetch and manipulate data in a relational database. A database helps organize data and efficiently store and retrieve data. **Relational databases** describe the data and the relationships between data entities. 

As you advance in this career, you might find yourself having to work with a team most of the time, need to re-visit previously-written SQL code or better yet a potential client might want to read your code - so it is very important to write code that is understandable, logical, organized and modifiable when working with databases. 

## Script files naming

- Make sure that your script file name describes the purpose of the SQL commands it contains: `school.sql` doesn't really say much about the script file content but `insert-c34-learner-records.sql` does, and will make it easy for the next programmer to find the file containing the commands you used to insert table records
- SQL script file names normally follow this format: `create_tables.sql` or `create-tables.sql` 

## Comments

- Single-line comments should start with **- -**
- Multi-line comments should start with **/\*** and end with **\*/**

## SQL expressions

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
- have a semi-colon `;` at the end of an expression. This isn't just good practice, it is a necessary part of the SQL language.

## Indentation, alignment and consistency

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

## Databases

If you're creating a school database, name it `school` instead of just `database`. Yes, names are still important.

## Tables and table columns

- Name a table using a pleural instead of singular, i.e. `customers`, `payments`, e.t.c. Why? Rule number 1 of naming things is to call it what it is. If we have a table that contains customer data such that each line contains a single customer then all our **customers** are stored in the table. The table is a collection of **customers** 
- Primary key column: It's good practice to name this column as just `id`
- Foreign key column: Use the specific table's name and a "id" e.g. `customer_id` - that way it easily references the foreign key to the `customer` table 


### The customers table

| id            | first_name | last_name | gender     | address               | email               |
| ------------- | ---------- | --------- | ---------- | --------------------- | --------------      |
| 1             | John       | Doe       | Male       | 284 Chaucer St        | john@gmail.com      | 
| 2             | Thando     | Sithole   | Female     | 240 Sect 1            | thando@gmail.com    | 
| 3             | Leon       | Glen      | Male       | 81 Everton Rd,Gillits | leon@gmail.com      | 

### The payments table

| id            | customer_id     | payment_type    | payment_date     |
| ------------- | --------------- | --------------- | ---------------- | 
| 1             | 1               | Cheque          | 06-10-2010       | 
| 2             | 1               | Cash            | 03-09-2018       |            
| 3             | 2               | Cash            | 06-09-2020       |

### Naming no nos

- Do not use capital letters in names columns, tables or databases. `name_things_like_this`
- Do not invent your own conventions for naming files. Scripts can be named `like-this` or `like_this`