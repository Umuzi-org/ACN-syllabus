---
_db_id: 63
content_type: topic
ready: true
title: ZeroMQ versus RabbitMQ versus Kafka
---

If you have a function that needs to be executed 1000 times on 1000 pieces of data, and you have a 50 computers that are all set up to help get the task done, then it would be useful to know how to effectively distribute the work across the computers. 

If each computer was exactly the same, and didn't have other workloads in play then:
  
- Each computer should execute about 20 function calls.
- The computers shouldn't re-execute stuff that was executed on the other computers.

To make this kind of thing happen, you need a mechanism to coordinate the computers. There are loads and loads of different tools that can be used for this kind of thing, and we've chosen to talk about only three. 

By understanding the differences between these three, you'll be able to better understand all other task distribution mechanisms.

Take a bit of time to look into each of these on your own. Consider:

- How each of these remembers what tasks are in the queue.
- How each of these keep track of task status. Does the tool know if the task has been started, if it failed, if it succeeded?
- Read up on use cases for each of these tools. When would you use one instead of another?
