---
_db_id: 1025
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/kubernetes/expanding-the-cluster/push-images-harbor
  - k8s/manual-app-deployment/project-overview
  soft: []
ready: true
submission_type: continue_repo
tags:
- kubernetes
title: Install PostgreSQL
---

Now let's start deploying our application stack with the PostgreSQL database.

Let's install PostgreSQL using the Bitnami's Helm chart.

```
# adds the bitnami helm repo
helm repo add bitnami https://charts.bitnami.com/bitnami

# updates helm index
helm repo update

# installs the postgresql
helm install postgresql bitnami/postgresql \
  --set global.postgresql.auth.username=youruser \
  --set global.postgresql.auth.password=yourpassword \
  --set global.postgresql.auth.database=dbname
  
# lists the helm charts installed
helm list
```

The Helm chat will generate a Kubernetes Service with the database address and a Kubernetes Secret with the database password. Let's find them!

```
# gets the postgresql service
kubectl get svc postgresql

# describes the postgresql secret
kubectl describe secret postgresql
```

Based on the commands output, you can use the following addresses to access the database:

```
# if the app is on the default Kubernetes namespace
postgresql:5432

# to access the database from any namespace
postgresql.default.svc.cluster.local:5432
```