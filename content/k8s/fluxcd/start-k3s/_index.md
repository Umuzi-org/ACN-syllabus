---
_db_id: 1044
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/fluxcd/setup-postgresql-backend
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
title: Start K3s
---

##  Start K3s

This time around we are starting the K3s cluster without Traefik and using the PostgreSQL that is running locally, in production likely your postgres database will be outside of the cluster and maintained separately

```
sudo curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server --disable=traefik --datastore-endpoint=postgres://k3s:yourpassword@localhost:5432/kubernetes" sh -

# and then remember to give permission to your kubeconfig file for access
sudo chmod 644 /etc/rancher/k3s/k3s.yaml
```