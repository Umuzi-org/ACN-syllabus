---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/fluxcd/create-folder-structure
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
title: Apps kustomization
---

# Apps kustomization

The reason we split your workload from the infrastructure is we can reuse a base template infrastructure to fire up additional clusters, think dev, staging, UAT, QA, pre-prod, production, etc. We can use kustomize to fine tune any environment specific needs like use this base except change the network loadbalancer annotations etc.

I want exactly these helm charts but replace dev.k8s-course.co.za with staging.k8s-course.co.za 


```
# clusters/my-cluster/apps.yaml
---
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: apps
  namespace: flux-system
spec:
  interval: 30s
  sourceRef:
    kind: GitRepository
    name: flux-system
  path: ./apps
  prune: true
```
