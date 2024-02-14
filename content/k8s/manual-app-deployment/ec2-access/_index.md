---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard: []
  soft:
  - k8s/manual-app-deployment/project-overview
ready: true
submission_type: continue_repo
tags:
- kubernetes
title: Access EC2
---

### Receive your Key Pair
When the course starts you will receive:
- The IP address and domain address to access an AWS EC2 instance
- A SSH key named `<your-name>.pem` to connect to the machine

Every time a new instance is created you will receive an email with a new IP address and domain.

### SSH into your EC2
First, make your key more secure by its restricting access to your own user:

```
chmod 0400 /path/to/your-name.pem
```

To connect to your EC2 instance run the following from your terminal:

```
ssh -i "<your-name>.pem" ubuntu@<ip-address>
```
