---
_db_id: 1037
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/github-actions
ready: true
submission_type: continue_repo
tags:
- kubernetes
- github
title: Setup GitHub Secrets
---

In the next chapters, we will be using GitHub to automate the process of building and pushing the Docker images and Helm Charts to Harbor using GitHub Actions. However, the communication with Harbor needs to be authenticated using its username and password.

So far we been using the `docker login` command on the EC2 instance. Now we need store the Harbor credentials on GitHub using the GitHub Secrets, so it will know how to authenticate.

On your GitHub repository page, go to `Settings` and then click on the `Secrets and variables` on the left panel and the on `Actions`.

Click on the button `New repository secret` and create the following secrets, one at a time:
- Name: `DOCKER_USERNAME`, secret: `admin`
- Name: `DOCKER_PASSWORD`, secret: `harbor12345`
- Name: `HARBOR_ENDPOINT`, secret: `harbor.<your-domain>`

We will be referencing these secrets in the GitHub Actions workflow files.