---
title: Containers
content_type: topic
ready: True
---

A container is a very fast and lightweight deployment solution because it doesn't require a hypervisor layer: *it shares the underlying host kernel*. The host only needs a Container Engine, like Docker or LXC.

Instead of running a whole operating system inside a VM, a container will bundle the application and its dependencies to be run in virtually any infrastructure.

Because of its size and portability, it became extremely easy and fast to create and destroy the most complex applications and infrastructure, becoming the stepping stone for the development and growth of the latest technology movements, like microservices, CI/CD pipelines, cloud native development, Serverless etc.

It also blurred the line between local development and production, making it easier to run production-like code on a personal machine and removing friction when moving an application through different deployment stages.

Know more:  
-[Cloud Native Computing](https://en.wikipedia.org/wiki/Cloud-native_computing)  
-[Microservices explained - the What, Why and How?](https://www.youtube.com/watch?v=rv4LlmLmVWk)  
-[Play with Docker: a simple, interactive and fun playground to learn Docker](https://labs.play-with-docker.com/)  

Containers brought many benefits to the table, like cost reduction, consistency, agility, portability and scalability.

It also came with its own disadvantages, like:  
-**Management complexity**: building and deploying one container is easy, but maintaining hundreds of containers across multiple servers is quite challenging. Container orchestration tools like Kubernetes came to the rescue, but they have an intense learning curve.  
-**Security**: since they share the same OS kernel, if it becomes vulnerable, all the containers running on that system become vulnerable as well.  
-**Observability**: monitoring, collecting and analyzing behavior data about 100s of small applications running everywhere becomes also challenging.  
-**Storage**: containers are ephemeral by nature, they may run for a couple of seconds on a machine and restart in another, making persistent storage availability another question to take into consideration.  

If someone screams the word “Docker” inside a cave they might get “Kubernetes” for an answer. While this chapter won’t cover Kubernetes, it will leave you with a few articles to read.

Know more:  
-[What is Kubernetes | Kubernetes explained in 15 minutes](https://www.youtube.com/watch?v=VnvRFRk_51k)  
