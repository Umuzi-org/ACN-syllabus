---
_db_id: 68
content_type: topic
title: ElasticSearch
---

## What is ElasticSearch?

> ElasticSearch (ES) is a distributed and highly available open-source search engine that is built on top of Apache Lucene. It’s an open-source which is built in Java thus available for many platforms. You store unstructured data in JSON format which also makes it a NoSQL database. So, unlike other NoSQL databases ES also provides search engine capabilities and other related features.
> [source: Towards Data Science](https://towardsdatascience.com/getting-started-with-elasticsearch-in-python-c3598e718380)

> Elasticsearch is a distributed, open source search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. Elasticsearch is built on Apache Lucene and was first released in 2010 by Elasticsearch N.V. (now known as Elastic). Known for its simple REST APIs, distributed nature, speed, and scalability, Elasticsearch is the central component of the Elastic Stack, a set of open source tools for data ingestion, enrichment, storage, analysis, and visualization. Commonly referred to as the ELK Stack (after Elasticsearch, Logstash, and Kibana), the Elastic Stack now includes a rich collection of lightweight shipping agents known as Beats for sending data to Elasticsearch.
> [source: official docs](https://www.elastic.co/what-is/elasticsearch)

## Getting it running

Of course docker is a great way to get started:

If you follow this document you will end up with a 3 node cluster running on your computer. This will eat all your ram. Rather use a one node cluster.
Also there is no need to use TLS on your local development machine:

https://www.elastic.co/guide/en/elastic-stack-get-started/current/get-started-docker.html

## tutorials and fun stuff

- Twitter sentiment analysis: https://realpython.com/twitter-sentiment-python-docker-elasticsearch-kibana/ This tutorial is written in legacy python. See if you can make it work with modern tools.

- https://www.freecodecamp.org/news/how-to-use-elasticsearch-logstash-and-kibana-to-visualise-logs-in-python-in-realtime-acaab281c9de/ this one is more relevent to data engineers but also goes into kibana a bit

- python-elasticsearch docs: https://elasticsearch-py.readthedocs.io/en/master/ . Elasticsearch exposes a really wonderful API. You can jusut interact with t using http requests instead of a different library if you wanted to. But this package makes life a lot easier