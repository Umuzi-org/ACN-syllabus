---
_db_id: 1017
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/kubernetes/expanding-the-cluster/install-harbor
ready: true
submission_type: continue_repo
tags:
- kubernetes
title: Push Docker images to Harbor
---

First, let's install Docker on this instance. Refer to the {{< contentlink path="k8s/containers-with-docker/install-docker-and-docker-compose" >}} chapter for the instructions.

In your browser navigate to `https://harbor.<your-domain>` and login using the username `admin` and password you created in the `values.yaml` file.

Go to projects and create a project called `application`.

Now go to your command line and let's issue some Docker commands to login into Harbor, build the Nginx image and push it to Harbor. Remember to substitute `<your-domain>` with the domain given to you by Umuzi.

```
# logs in into Harbor
docker login harbor.<your-domain>

# builds the Nginx image
cd /home/ubuntu/umuzi-k8s/nginx
docker build . -t harbor.<your-domain>/application/nginx:v1

# pushes the image to Harbor
docker push harbor.<your-domain>/application/nginx:v1
```

Let's do the same from the Python app using a oneliner:

```
cd /home/ubuntu/umuzi-k8s/python
docker build . -t harbor.<your-domain>/application/python:v1 --push
```