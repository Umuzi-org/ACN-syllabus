---
title: Nginx Installation
content_type: project
tags:
- kubernetes
- nginx
prerequisites:
  hard: 
  - k8s/manual-app-deployment/certbot
  soft: []
ready: true
submission_type: continue_repo
from_repo: k8s/manual-app-deployment/certbot
---

Nginx is arguably the world's leading web server, load balancer, and proxy server. Known for its exceptional performance, scalability, and low resource usage, Nginx serves static content efficiently and acts as a reverse proxy to distribute incoming traffic across multiple servers. Its capabilities extend to caching, SSL/TLS termination, and robust security features. Widely used in high-traffic websites, Nginx is a versatile solution for enhancing the speed and reliability of web services.

```
# updates the package manager
sudo apt update

# installs nginx
sudo apt install nginx -y

# initialize nginx automatically
sudo systemctl enable nginx

# test nginx's configuration.
sudo nginx -t

# verify that nginx is running
sudo systemctl status nginx
```

Now navigate to `http://your-domain.com`.

> Your browser might complain to be accessing an HTTP-only page. Just click the button saying that you know what you are doing.

You should be able to see the default Nginx page without TLS as we haven't configured the certificate yet.
