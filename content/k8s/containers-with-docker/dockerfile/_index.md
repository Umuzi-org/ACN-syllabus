---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/containers-with-docker/certbot
  soft: []
ready: true
submission_type: continue_repo
tags:
- kubernetes
title: Dockerfile
---

A Dockerfile is a recipe to deploy your code in a light weight virtual machine (container) while using the libraries from the host machine.

We will have two sets of files: `dev` and `production`. The first would be used in a local development environment (your machine) and the second on a production environment.

The main difference is that the `dev` uses HTTP and `production` uses HTTPS.

***

Let's create a couple of new files on the GitHub repository and commit the changes.

First, create the Dockerfile for Nginx as `nginx/Dockerfile.`

```
FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY https-nginx.conf /etc/nginx/conf.d

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

Create the `nginx/DockerfileDev` file.

```
FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY http-nginx.conf /etc/nginx/conf.d

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

Create the `python/Dockerfile` to build our Python app.

```
FROM python:latest

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY app.py /app

EXPOSE 5000

CMD ["python", "app.py"]
```

And create a file stating the Python app dependencies, under `python/requirements.txt` .

```
flask
psycopg2
```

Save the files, commit and push the changes to the GitHub repository.