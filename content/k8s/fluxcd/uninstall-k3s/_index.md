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
title: Unistall k3s

---
description: >-
  Let's start by nuking the cluster as we have no idea what the true state is
  and we can start fresh
---

# Unistall k3s

```
sudo /usr/local/bin/k3s-uninstall.sh
```