---
_db_id: 125
content_type: topic
ready: true
title: JDBC templates
---

Both Springboot and VanillaJS require a middle man to be able to talk to a database. This is where JDBC comes in. It can be used with multiple programming languages.
Javascript languages tend to make more use of ODBC (Open Database Connectivity) whereas JDBC was created with Java in mind. The 2 are interchangeable.

Springboot has no way of directly communicating with a database, it requires a JDBC driver.

## JDBC - Java Database Connectivity

JDBC is an API that consists of interfaces used to access relational databases such as SQL.

Note: A relational database is one where the database can recognise relationships/links between the data saved in it.

JDBC allows a Java application to connect to a SQL server and run SQL scripts to work with the databases 
on the server and manipulate the tables and the data stored within them.

- [Example:](https://www.tutorialspoint.com/jdbc/jdbc-select-records.htm) Connect to a database server and fetch data from the database.

How to store data

```
long id = 1;
string name = "umuzi" 
jdbcTemplate.update("insert into User (id, name) values(?,?)", new Object[]{id,name});

```

## JPA - Java Persistence API

JPA allows an individual to communicate with a database without having to create SQL queries. It bridges
the gap between SQL and Java. For instance, you can create a modal and by adding certain annotations to it, you
can create/alter the database.

[Here's](https://www.javaworld.com/article/3373652/java-persistence-with-jpa-and-hibernate-part-1-entities-and-relationships.html) a quick tutorial that outlines some of the functionality that JPA provides.

In User.java
```
@Entity
public class User
{
	@Id
	private int id;
	private String firstName;
	private String lastName;

	// Constructors, Getter and Setters
}

```

It also comes with a more convenient way to add data into the database by the help of jpsRepository

```
user = new User(2, "umuzi");
userRepository.save(user);

```

## Hibernate

JPA provides the interface (the set of rules that need to be followed). But alone it does nothing.
It needs to be implemented. This is where Hibernate comes in.

Without JPA though, Hibernate can still be used to communicate with the database in a similar manner, as can be seen
[here](https://www.tutorialspoint.com/hibernate/hibernate_examples.htm).

## Resources

- [JDBC documentation](https://www.tutorialspoint.com/jdbc/jdbc-introduction.htm).
- [Video tutorials](https://www.youtube.com/playlist?list=PLmCsXDGbJHdhs1dWrgeT1ZoitLGp90I6D).

- [JPA Documentation](https://www.tutorialspoint.com/jpa/index.htm).
- [Hibernate Documentation](https://www.tutorialspoint.com/hibernate/index.htm).

- [JPA with Hibernate video tutorials](https://www.youtube.com/watch?v=LKidsEzqwXw&list=PLgzDdh90-m_TKIz4JNuqh3QarIdKiTS3q).