# helmrepository
This is the content of helmrepository.

# 4.1.6 Helmrepository

For flux we need a collection of helmrepositories that pull down helm charts to be available to deploy

create the folder infrastructure/sources along with its kustomization.yaml file

```
# infrastructure/sources/kustomization.yaml
---
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: flux-system
resources:
  - jetstack.yaml
```

```
# infrastructure/sources/jet-stack.yaml
---
apiVersion: source.toolkit.fluxcd.io/v1beta1
kind: HelmRepository
metadata:
  name: jetstack
spec:
  interval: 24h
  url: https://charts.jetstack.io
```

And finally add the sources fodler to the infrastructure/kustomization.yaml file so that it's not empty and push to main branch again

```
# infrastructure/kustomization.yaml
---
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - sources
```

Wait for the kustomization to apply and check if you can see the helmrepository&#x20;

```
kubectl -n flux-system get helmrepository
```
