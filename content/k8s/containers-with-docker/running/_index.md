---
_db_id: 1007
content_type: project
flavours:
- none
prerequisites:
  hard:
  - k8s/containers-with-docker/python-app
  soft: []
ready: true
submission_type: link
tags:
- kubernetes
title: Running the App
---

Let's run our Docker Compose production environment!

On your EC2 instance, pull the repository changes from GitHub:

```
# pulls the changes
cd /home/ubuntu/umuzi-k8s
git pull
```

Let's build the containers and get them up and running:

```
# builds the containers
docker-compose build

# runs the containers
# -d will run everything on the background
docker-compose up -d
```

To see if everything is running nicely, take a look at the Docker Compose logs:

```
# verifies the logs
docker-compose logs
```

Now you should be able to access the Python app via the `https://your-domain` address.