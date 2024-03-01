# ingress-nginx-helmrepository
This is the content of ingress-nginx-helmrepository.

# 4.1.7 Ingress-nginx helmrepository

add the following files&#x20;

```
# infrastructure/sources/kustomization.yaml
---
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: flux-system
resources:
  - jetstack.yaml
  - ingress-nginx
```

```
# infrastructure/sources/ingress-nginx.yaml
---
apiVersion: source.toolkit.fluxcd.io/v1beta1
kind: HelmRepository
metadata:
  name: ingress-nginx
spec:
  interval: 120m
  url: https://kubernetes.github.io/ingress-nginx
```

Push it up and check if the helmrepository has pulled through

```
kubectl -n flux-system get helmrepository
```
