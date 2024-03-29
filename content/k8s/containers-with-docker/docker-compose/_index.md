---
_db_id: 1012
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/containers-with-docker/dockerfile
ready: true
submission_type: continue_repo
tags:
- kubernetes
title: Docker Compose
---

Docker Compose helps us orchestrate Docker containers.

In this project will have 3 containers running: Nginx, Python, PostgreSQL.

Create the `docker-composeDev.yaml` in root of the repository.

```
services:
  flask-app:
    build:
      context: ./python
    ports:
      - "5000:5000"
    environment:
      - DB_NAME=dbname
      - DB_USER=dbuser
      - DB_PASSWORD=dbpassword
      - DB_HOST=postgres
    depends_on:
      - postgres
    command: bash -c 'sleep 10 && python app.py'

  nginx:
    build:
      context: ./nginx
      dockerfile: DockerfileDev
    ports:
      - "8080:80"
    depends_on:
      - flask-app

  postgres:
    image: postgres:latest
    environment:
      POSTGRES_DB: dbname
      POSTGRES_USER: dbuser
      POSTGRES_PASSWORD: dbpassword
```

Create the `docker-compose.yaml` in root of the repository.

```
services:
  flask-app:
    build:
      context: ./python
    ports:
      - "5000:5000"
    environment:
      - DB_NAME=dbname
      - DB_USER=youruser
      - DB_PASSWORD=yourpassword
      - DB_HOST=postgres
    depends_on:
      - postgres
    command: bash -c 'sleep 10 && python app.py'

  nginx:
    build:
      context: ./nginx
      dockerfile: Dockerfile
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - flask-app      
    # mount the TLS certificates from the host machine to the container
    # change <your-domain> to the domain given to you by Umuzi
    volumes:
      - /etc/letsencrypt/live/<your-domain>/fullchain.pem:/etc/letsencrypt/live/example.com/fullchain.pem
      - /etc/letsencrypt/live/<your-domain>/privkey.pem:/etc/letsencrypt/live/example.com/privkey.pem
      - /etc/ssl/certs/dhparam.pem:/etc/ssl/certs/dhparam.pem
      
  postgres:
    image: postgres:latest
    environment:
      POSTGRES_DB: dbname
      POSTGRES_USER: youruser
      POSTGRES_PASSWORD: yourpassword
```

Save the files, commit and push the changes to the GitHub repository.