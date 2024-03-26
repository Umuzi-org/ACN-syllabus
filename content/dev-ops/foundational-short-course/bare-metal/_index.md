---
title: Bare Metal
content_type: topic
ready: True
---

With a bare metal deployment, one gets access to a server (bought or rented by a cloud provider), installs the operating system and needs to manage everything necessary to run the application, like libraries, dependencies, packages, services, before running the actual business app.

Pros:  
-Full access to the server, maximum flexibility and autonomy  
-Best performance, access to the raw computing resources  
-No *noisy neighbors*: other people running applications on a shared server like (VMs)  

Cons:  
-Needs a lot of management and care  
-Limited resource scalability  
-Resource can be underutilized if only one or few apps can run  
-Runs a single operating system, sometimes libraries and dependencies can conflict  

Challenges:  
-What if we want to run another app with a different set of dependencies?  
-What if we want to run an app that requires a different operating system?  
-What if we could slice the server into multiple, *virtual servers*?  