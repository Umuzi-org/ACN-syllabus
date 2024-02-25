---
_db_id: 1001
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/manual-app-deployment/ec2-access
ready: true
submission_type: continue_repo
tags:
- kubernetes
- github
title: GitHub Setup
---

We will be using GitHub to create and store the files we need through out the course (and use GitHub Actions to automate the deployment later).

When your start your first project in Tilde, you will receive the a GitHub repository under Umuzi's GitHub organization. This is the repository you'll be using through out the course.

Since this is a private repository, you will need a GitHub personal access token to clone it inside the EC2 instance.

> You can also opt to setup your SSH credentials within the EC2 instance if you know how to do it.

Here is how you generate the token:
- Go to your GitHub page
- Go to Settings > Developer Settings
- There, click on "Personal access token" and then "Tokens (classic)"
- Click on "Generate new token" and "Generate new token (classic)"
- Give it a name, like `umuzi-k8s`, give it an expiration of `60 days` and check the `repo` box to give it repo-wide permissions
- Down below, click on "Generate token"

On the following page, you'll be given the token. It is a string similar to `ghp_very-long-random-string`. Copy and save it somewhere safe.

On your EC2 instance, clone the repository inside your home folder:

```
# enters the home folder and clones the repo
# make sure to clone it as `umuzi-k8s` folder, we will be using it during the course
cd $HOME
git clone https://github.com/<your-user-name>/<your-repo>.git umuzi-k8s
```

You'll be asked for a `username` and `password`. For the first, enter your username. For the latter, enter the GitHub personal access token you generated.

Every time we make a change we will need to go under this folder and manually `pull` the changes with the following command:

```
# update the changes from GitHub
cd /home/ubuntu/umuzi-k8s
git pull
```