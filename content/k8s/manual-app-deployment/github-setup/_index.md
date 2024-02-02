---
title: GitHub Setup
content_type: topic
tags:
- kubernetes
- github
prerequisites:
  hard: []
  soft: []
ready: true
---

We will be using GitHub to create and store the files we need through out the course (and use GitHub Actions to automate the deployment later).

Create a public GitHub repository named `umuzi-k8s` (private will also work if you know how to setup command line access).

Clone the repository on the AWS EC2 instance's home folder:

```
# enters the home folder and clones the repo
cd $HOME
git clone https://github.com/<your-user-name>/umuzi-k8s.git
```

Every time we make a change we will need to go under this folder and manually `pull` the changes with the following command:

```
# update the changes from GitHub
cd /home/ubuntu/umuzi-k8s
git pull
```
