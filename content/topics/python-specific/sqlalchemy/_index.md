---
_db_id: 159
content_type: topic
ready: true
title: Sqlalchemy ORM
---

Sqlalchemy is the most popular Python ORM (Object Relational Mapper). It is highly legit. Lit even (am I using that right?)

What's an ORM? Well, I'm glad you asked. And I'm also glad that [this guy asked](https://stackoverflow.com/questions/1279613/what-is-an-orm-how-does-it-work-and-how-should-i-use-one)

Sqlalchamy of course is not the only ORM around. There's a very good chance that you'll come across [this one](https://docs.djangoproject.com/en/3.0/topics/db/queries/) as well.

Take a little bit of time to learn the fundamentals here:
{{% contentlink path="topics/python-specific/sqlalchemy/basics" %}}

Once you are done with the basics, it's good to understand migrations. Migrations basically let you version control the structure of your database. This is seriously freaking useful if you ever want to actually us an ORM in production (hint: You do!)

{{% contentlink path="topics/python-specific/sqlalchemy/migrations" %}}