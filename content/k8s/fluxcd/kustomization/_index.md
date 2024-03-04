---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/fluxcd/bootstrap-flux
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
title: Kustomization
---

## Kustomization

```
kubectl -n flux-system get kustomization
kubectl -n flux-system describe kustomization
```

Now we need to add a new kustomization for our base infrastructure

In the infrastructure directory create the following files

```
# clusters/my-cluster/kustomization.yaml
---
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: infrastructure
  namespace: flux-system
spec:
  interval: 10m0s
  sourceRef:
    kind: GitRepository
    name: flux-system
  path: ./infrastructure
  prune: true
```

You'll notice kustomize tells flux to go and look inside the ./infrastructure folder for further instructions and then it will again look for the kustomization file and follow instructions

Commit to github you can push straight to main branch

```
kubectl -n flux-system get kustomization --watch
```

You'll need to wait a minute or so and you'll notice the new kustomization rolling out and tells you that it's missing a file let's add it now

```
# infrastructure/kustomization.yaml
---
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
```

Now it says the file is empty but let's add some sources in the next section
