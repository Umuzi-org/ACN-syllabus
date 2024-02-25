---
_db_id: 1004
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/manual-app-deployment/certbot
  - k8s/manual-app-deployment/nginx-installation
  - k8s/manual-app-deployment/postgresql-installation
ready: true
submission_type: continue_repo
tags:
- kubernetes
- nginx
title: Nginx TLS Setup
---

Let's setup TLS on our hello world Nginx server.

On the GitHub repository, create a file called `nginx.conf` under a folder named `nginx`.

Change `<your-domain>` for the domain given to you by Umuzi.

```nginx
# this redirects port 80 to port 443
server {
    listen 80;
    # change to your domain
    server_name <your-domain>;

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name <your-domain>;
    
    # remember these routes from certbot
    ssl_certificate /etc/letsencrypt/live/<your-domain>/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/<your-domain>/privkey.pem;

    location / {
        root /var/www/html;
        index index.html;
    }

    # SSL settings (add your SSL-related directives here)
    # Example SSL settings:
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384';
    ssl_prefer_server_ciphers off;
    
    # this was the last command in the certbot section.
    ssl_dhparam /etc/ssl/certs/dhparam.pem;
}
```

Create another file under the `nginx` folder named `index.html`. This will be our front page, for now.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to My Website</title>
</head>
<body>
    <h1>Hello, Nginx!</h1>
    <p>This is the default index page for your Nginx web server.</p>
    <p>Feel free to replace this content with your own website's content.</p>
</body>
</html> 
```

Save the files and commit the changes.

On the EC2 instance, pull the changes, copy the files and restart Nginx.

```
# enter the repository and pull the changes
cd /home/ubuntu/umuzi-k8s
git pull

# copy the created files
sudo cp nginx/nginx.conf /etc/nginx/conf.d/nginx.conf
sudo cp nginx/index.html /var/www/html/

# restart nginx
sudo systemctl restart nginx
```

Navigate to `https://your-domain` and you should see the HTML page we just created!