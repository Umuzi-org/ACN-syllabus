---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/containers-with-docker/docker-compose
  - k8s/manual-app-deployment/project-overview
ready: true
submission_type: continue_repo
tags:
- kubernetes
title: Nginx
---

Now you need two `nginx.conf` files, one using HTTP for the `dev` environment and using HTTPS for production.

Create `nginx/http-nginx.conf` file:

```
server {
    listen 80;
    
    location / {
        root /usr/share/nginx/html/;
        index index.html;
    }

   location /api {
         proxy_pass http://flask-app:5000; 
    }
}
```

And `nginx/https-nginx.conf`. Change `<your-domain>` with the domain given to you by Umuzi.

```
server {
    listen 80;
    server_name <your-domain>;

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name <your-domain>;

    # the certificates file are mounted by Docker Compose
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    location /api {
        proxy_pass http://flask-app:5000;
    }

    # SSL settings
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384';
    ssl_prefer_server_ciphers off;
    ssl_dhparam /etc/ssl/certs/dhparam.pem;
}
```

Save the files, commit and push the changes to the GitHub repository.