---
_db_id: 64
content_type: topic
ready: true
title: Database Comparison
---

SQL is great and all, and even though a lot of people think it's a lil old-school, it's here to stay. It is a robust and mature technology, the query language it defines can be used for all sorts of big data and analytic workloads, and it's easy to reason about.

But when it comes to data storage and access there isn't a once-size-fits-all technology.

There are a lot of databases out there. You can think of them in a few different categories.

_In memory databases_ are FAST, they store everythig in RAM and so the data that they store is not durable. If the computer shuts down then the data is gone. Redis is an example of this.

Most databases store data to disk. Eg Postgres is not an in-memory database. The data it stores is durable.

Then you get NoSQL databases. The No in NoSQL could maybe stand for "Not only" SQL. But it depends on who you talk to and their agenda. Basically when it comes to SQL, the database structure is pretty strict and rigid and if the shape of your data changes you need to jump through hoops to make it work. In many sitations this just isn't ideal. So there is a whole class of shemaless or low-schema databases that address this. MongoDB is a commonly used durable NoSQL database.

Another set of categories that databases fall into is to do with how they scale. The options are vertical and horizontal.

Imagine you have a database running on a server and it runs out of disk space or some other respource. Vertical scaling implies simply upgrading that server - by giving it a bigger hard-drive, more ram, or a bigger cpu you allow bigger workloads. There is an upper limit to how big you can vertically scale.

Horisontal scaling is all about introducing more computing nodes (computers, VMs or containers) to the mix, and then coordinating those nodes to do the job of one big database. This allows for much bigger data and database requests and writes can also be shared between the nodes. This is awesome but of course has its own complexities and limitations, for example data on different nodes tends to become out of sync and you have to be aware of that.

MongoDB is horizontally scalable by default. Postrgres isn't really but there are a [few workarounds](https://stackoverflow.com/questions/34831086/scaling-postgres-horizontally) depending on what you want to do with it.

## Resources

- https://realpython.com/data-engineer-interview-questions-python/ This covers a ot of ground around comparing different databases
- Python and MongoDB: https://realpython.com/introduction-to-mongodb-and-python/
- Python and Redis: https://realpython.com/python-redis/