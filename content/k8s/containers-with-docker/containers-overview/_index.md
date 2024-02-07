---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/nginx-reverse-proxy
ready: true
submission_type: continue_repo
tags:
- kubernetes
title: Overview of Containers and using Docker & Docker-compose
---

Let's start our Docker and Docker Compose journey!

We will use the same `index.html`, `nginx.conf` (with modifications) and `app.py` files but this time we will deploy them using Docker and Docker Compose.

The reason we use Docker is so that we can skip all the custom installation of the pet server making it quicker and easier to deploy code on a new server or in different environments.

You will notice two `docker-compose.yaml` files. One is for your local environment and one for your production environment.