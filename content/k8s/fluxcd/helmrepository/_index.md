---
_db_id: 1053
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/fluxcd/kustomization
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
title: Helmrepository
---

## Helmrepository

For flux we need a collection of helmrepositories that pull down helm charts to be available to deploy.

Create the folder `infrastructure/sources` along with its kustomization.yaml file

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
# infrastructure/sources/jetstack.yaml
---
apiVersion: source.toolkit.fluxcd.io/v1beta1
kind: HelmRepository
metadata:
  name: jetstack
spec:
  interval: 24h
  url: https://charts.jetstack.io
```

And finally add the sources folder to the `infrastructure/kustomization.yaml` file so that it's not empty and push to main branch again

```
# infrastructure/kustomization.yaml
---
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - sources
```

Wait for the kustomization to apply and check if you can see the helmrepository

```
kubectl -n flux-system get helmrepository
```

Now create the files
```
# infrastructure/sources/ingress-nginx.yaml
# infrastructure/sources/harbor.yaml
```

Within these files, create a HelmRepository resource (like we did in jetstack.yaml) using the following URLs, respectively.
- ingress-nginx `url: https://kubernetes.github.io/ingress-nginx`
- harbor `url: https://helm.goharbor.io`

``` 
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: flux-system
resources:
  - jetstack.yaml
  - ingress-nginx.yaml
  - harbor.yaml
```

You should see 3 items when you run 
`kubectl -n flux-system get helmrepository` 
If not try `kubectl -n flux-system get kustomization` and use `describe kustomization/helmrepository` etc to debug