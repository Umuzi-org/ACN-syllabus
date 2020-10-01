---
_db_id: 65
content_type: topic
ready: true
title: DAGs with Airflow
---

Apache airflow is what Airbnb use to manage their data pipelines. They built it and then gave it to the Apache foundation. It is now an Apache top level project. Read a little bit about Apache if you don't know the significance of that. TLDR; it's a solid piece of tech.

What does it do? Basically, large scale data processing generally requires:

- multiple processing steps
- with specific interdependencies
- that need to happen on a specific schedule

This on it's own isn't too hard. But let's say you are working for a big company. Like a bank. What else might a data pipeline need?

- logging and error detection
- distributed workloads
- performance monitoring and SLAs
- secret managment
- visability to business stakeholders
- authentication
  And a lot more

This is why Airflow exists.

Another cool thing about airflow is that the concepts at its core can help you understand many other tools.

## What you need to know

Airflow's docs are great. Use the official tutorial, and make sure you understand the core concepts.

- https://airflow.apache.org/docs/stable/tutorial.html
- https://airflow.apache.org/docs/stable/concepts.html

And this guide has some good pictures

- https://www.polidea.com/blog/apache-airflow-tutorial-and-beginners-guide/