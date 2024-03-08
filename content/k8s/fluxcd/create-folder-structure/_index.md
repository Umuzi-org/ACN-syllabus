---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/fluxcd/helmrelease
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
title: Create folder structure
---

## Create folder structure

Finally we are in a position to release our own application.

First up create the following files and folders.

```
|-- apps
|   |-- kustomization.yaml
|   |-- buttons
|   |   |-- kustomization.yaml
|   |   |-- kustomizeconfig.yaml
|   |   |-- release.yaml
|   |   |-- values.yaml
|   |   |-- namespace.yaml
|   |   |-- issuer.yaml
|-- clusters
|   |-- my-cluster
|   |   |-- apps.yaml
```



