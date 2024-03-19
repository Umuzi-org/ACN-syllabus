---
_db_id: 1048
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/fluxcd/buttons-helmrelease
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
title: PostgreSQL buttons
---

# PostgreSQL buttons

You'll notice your front end starts and your backend can't start because it can't find the PostgreSQL secret and that is likely because you don't have PostgreSQL helm chart installed.

Many of the awesome helm charts you'll use was developed by Bitnami so let's start by loading the source helmRepository.


```
# infrastructucture/sources/bitnami.yaml
--- 
apiVersion: source.toolkit.fluxcd.io/v1beta1
kind: HelmRepository
metadata:
  name: bitnami
spec:
  interval: 120m
  url: https://charts.bitnami.com/bitnami
```

Remember the kustomization.yaml

```
# infrastructure/sources/kustomization.yaml
---
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: flux-system
resources:
  - jetstack.yaml
  - ingress-nginx.yaml
  - harbor.yaml
  - buttons.yaml
  - bitnami.yaml
```

You can push that up so long and then we can add the release.

```
# apps/buttons/postgres.yaml
---
apiVersion: helm.toolkit.fluxcd.io/v2beta1
kind: HelmRelease
metadata:
  name: postgres
spec:
  releaseName: postgres
  chart:
    spec:
      chart: postgresql
      sourceRef:
        kind: HelmRepository
        name: bitnami
        namespace: flux-system
      version: "*"
  interval: 0h1m0s
  install:
    remediation:
      retries: 3
  values:
    global:
      postgresql:
        auth:
          database: dbname

# notice the different way of referencing the values file
```

PS. Remember to add the folder to your kustomization.yaml

After PostgreSQL starts up your backend should have a database to log in to so if you delete the pod one more time hopefully it will start up and if you ingress is configured correctly your counter will start working.