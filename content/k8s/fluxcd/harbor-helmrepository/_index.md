# harbor-helmrepository
This is the content of harbor-helmrepository.

# 4.1.7 Harbor helmrepository

Yeah I know this is getting boring now

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
```

```
apiVersion: source.toolkit.fluxcd.io/v1beta1
kind: HelmRepository
metadata:
  name: goharbor
spec:
  interval: 120m
  url: https://helm.goharbor.io
```
