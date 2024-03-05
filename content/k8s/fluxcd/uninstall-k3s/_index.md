---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/helm-deployment/deploy-backend
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
title: Unistall K3s

---


## Unistall K3s

  Let's start by nuking the cluster as we have no idea what the true state is
  and we can start fresh

```
sudo /usr/local/bin/k3s-uninstall.sh
```