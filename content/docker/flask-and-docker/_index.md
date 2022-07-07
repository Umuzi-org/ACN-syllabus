---
_db_id: 703
content_type: project
flavours:
  - none
from_repo: projects/python-specific/flask-rest-api/part-1
prerequisites:
  hard:
    - docker/intro-to-docker
    - projects/python-specific/flask-rest-api/part-1
    - projects/python-specific/flask-rest-api/part-2
ready: true
submission_type: continue_repo
title: Flask and docker
---

Before you do this, please revise {{% contentlink path="docker/intro-to-docker" %}}. You are going to need to have solid understanding of all the **Advanced Topics**.

Make sure you understand:

- What a volume is, and why you would use one
- How ports and port mapping works. And what a port is
- How to create your own Docker images

## Project

### Build and push

Make a docker image that can be used to run your flask app. Please create the following files:

- `Dockerfile` this should do normal dockerfile things :)
- `build.sh` This should be a shell script that you can use to quickly build your image and give it the right name. Here is an example build script from the Tilde code base:

```
#!/bin/sh

docker build -t umuzi-org/tilde-backend .
```

- `push.sh` executing this script should push your image to dockerhub

### Docker-compose

Create a `docker-compose.yaml` file. This should be used to launch your app and database.

- Make use of volumes to make sure you can store your logs on your computer
- Make use of port mapping so that your application is accessible
- Make use of environmental variables to set the logging level to log the debug messages.
