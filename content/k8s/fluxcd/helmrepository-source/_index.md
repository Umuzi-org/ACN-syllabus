# 4.1.3 Helmrepository source

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
  password: Harbor54321
```

Yes I know plain text password in the github but we aren't doing SOPS encryption or vault in this course&#x20;