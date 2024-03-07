---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/fluxcd/helmrepository-source
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
title: Root kustomization apps

---

## Root kustomization apps 

```
# apps/kustomization.yaml
---
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - buttons
```