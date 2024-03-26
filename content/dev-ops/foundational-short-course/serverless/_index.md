---
title: Serverless (Function as a Service)
content_type: topic
ready: True
---

Now you throw away the servers, the virtual machines and the containers. In a Serverless architecture, you write a piece of code – usually a function – upload it to the cloud provider and it will set up everything needed to run the code. Attach that artifact with an API gateway and you have an application up and running.

No server management is necessary (or even possible). The developer has almost no control over the environment. A couple of configuration options are available, like amount of memory, environment variables, but one won’t be able to choose an operating system or IP address.

The pricing is radically different as well. The cost is calculated based on the amount of the time the code runs, usually down to the millisecond. If the code runs for 1 minute everyday, it will be charged only for that.

Scalability becomes less of an issue, since Serverless architectures will automatically scale as needed. If there’s a sudden load on the system and the function needs to be run 10x more than usual, the cloud provider will scale the environment accordingly.

Of course nothing is flowers. Less control means less flexibility and more vendor lock-in. The Serverless environment from AWS is quite different from GCP, making the application portability more tricky.

When writing Serverless software, one usually *glues* together many different cloud provider specific platforms that are quite hard to simulate locally. Debugging, testing and troubleshooting becomes harder and more complex, increasing the friction between a local developer machine and the production environment.

Main Serverless (FaaS) technologies:  
-AWS Lambda  
-Google Cloud Functions  
-Apache OpenWhisk  
-Kubernetes Knative  

Known more:  
-[What is Serverless?](https://www.youtube.com/watch?v=vxJobGtqKVM)  
