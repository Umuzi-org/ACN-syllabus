---
_db_id: 1040
content_type: topic
ready: true
tags:
- kubernetes
- github
- ci-cd
title: GitHub Actions
---

Although in production you would normally operate on multiple repos for this exercise we will use a monorepo structure with folders for code, Helm Charts, and, later, FluxCD. 

Now that we have an idea of the procedures needed to get workloads into production, let's have a look at how we can start automating these processes. 

We know we have to run `docker build` and `docker push` commands. But how about doing this every time we push to GitHub? This is called continuous integration, or the CI part of CI/CD.

Many teams opt for fire and forget and use the pipeline to deploy to an environment as well but we will see why this is not a good idea in practice as it doesn't allow for subsequent failures and rollback procedures.

We want to be able to push code to Github and it needs to deploy to different environments, like stating and production, and rollback if there is a failure. 

The rundown looks something like this:
- We push to GitHub and trigger a build 
- The build runs tests on the workload and we can also do security scans with the idea if something is wrong the pipeline fails stopping the deployment 
- We then want to push the artifact to a Docker registry (Harbor, in our case), where we can perform further security scans
- This will test wether this workload is satisfactory but not all the other workloads in the application ie. there may be a dependency that is not working and we can't test for that here and that is why we add tests in the Helm Chart to allow us to rollback if the application with all workloads don't perform as expected and that is why it's a bad Idea to deploy directly from a single pipeline

Create a folder named `.github` and, inside that folder, create another one named `workflows`.

Your folder structure should look something like this so far:

```
├── .github
│   └── workflows
├── docker-compose.yaml
├── docker-composeDev.yaml
├── helm
│   └── buttons
│       ├── Chart.yaml
│       ├── templates
│       │   ├── _helpers.tpl
│       │   ├── configmap.yaml
│       │   ├── ingress.yaml
│       │   ├── nginx-deployment.yaml
│       │   ├── nginx-service.yaml
│       │   ├── python-deployment.yaml
│       │   └── python-service.yaml
│       └── values.yaml
├── k8s
│   ├── cert-manager
│   │   └── issuer.yaml
│   ├── harbor
│   │   └── values.yaml
│   ├── ingress-nginx
│   │   └── values.yaml
│   ├── nginx
│   │   ├── Dockerfile
│   │   ├── deployment.yaml
│   │   ├── index.html
│   │   ├── ingress.yaml
│   │   ├── nginx.conf
│   │   └── service.yaml
│   └── python
│       ├── Dockerfile
│       ├── app.py
│       ├── deployment.yaml
│       ├── requirements.txt
│       └── service.yaml
├── nginx
│   ├── Dockerfile
│   ├── DockerfileDev
│   ├── http-nginx.conf
│   ├── https-nginx.conf
│   ├── index.html
│   └── nginx.conf
└── python
    ├── Dockerfile
    ├── app.py
    ├── myflaskapp.service
    └── requirements.txt
```