---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/fluxcd/root-kustomization-apps
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
title: Buttons helmrepository source
---



We want to pull from our own helmrepository source so let's add that to our sources

```
# infrastructure/sources/buttons.yaml
---
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: HelmRepository
metadata:
  name: buttons
  namespace: flux-system
spec:
  interval: 5m0s
  url: oci://<myUrl.com>/application
  type: "oci"
  secretRef:
    name: oci-creds
---
apiVersion: v1
kind: Secret
metadata:
  name: oci-creds
  namespace: flux-system
stringData:
  username: admin
  password: harbor12345
```

Remember to add buttons.yaml to your `infrastructure/sources/kustomization.yaml` file

Yes I know plain text password in the GitHub but we aren't doing Mozilla SOPS encryption or Hashicorp Vault in this course.

Make sure your helmrepository shows 

`kubectl -n flux-system get helmrepository'