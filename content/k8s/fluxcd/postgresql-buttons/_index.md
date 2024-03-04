---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/fluxcd/root-apps-kustomization
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
title: Buttons helmrepository source
---

# postgressql buttons

You'll notice your front end starts and your backend can't start because it can't find the postgres secret and that is likely because you don't have postgressql helm chart installed

So let's start by adding the source for bitnami

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

Remeber the kustomization.yaml

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

you can push that up so long and then we can add the release

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

# notice the different way of refrencing the values file
```
