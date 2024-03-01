# 4.1.2 Apps kustomization

The reason we split your workload from the infrastructure is we can reuse a base template infrastructure to fire up aditional clusters, think staging, UAT, QA, pre-prod, production, we can use kustomize to fine tune any environment specific needs like use this base except change the NLB annotations etc.&#x20;

````
# clusters/my-cluster/apps.yaml
---
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: apps
  namespace: flux-system
spec:
  interval: 10m0s
  sourceRef:
    kind: GitRepository
    name: flux-system
  path: ./apps
  prune: true
```
````