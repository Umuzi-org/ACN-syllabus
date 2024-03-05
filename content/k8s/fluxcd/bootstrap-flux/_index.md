---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/fluxcd/start-k3s
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
title: Bootstrap flux

---
## Bootstrap flux

first we install the fluxCD cli

```
curl -s https://fluxcd.io/install.sh | sudo bash
```

next create a github personal access token (We will use the classic token for this course)

 https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

```
export GITHUB_TOKEN=<gh-token>
export GITHUB_USER=<my-github-username>
flux bootstrap github \
  --token-auth \
  --components-extra=image-reflector-controller,image-automation-controller \
  --owner=my-github-username \
  --repository=my-repository-name \
  --branch=main \
  --path=clusters/my-cluster \
  --personal \
  --read-write-key=true
```

A few things are happening here

* a new namespace is being created flux-system
* You'll notice a new folder being created in your repo called clusters and subfolder my-cluster
* Fluxcd does a git clone and applies the kustomization along with the helm charts specified
* This is the deployment step from now on everything will be done inside the repo that way we can always keep track of the cluster state and it will always be easy to rebuild in case of disaster recovery needed

```
# remember to pull the commit that flux made before continuing
git pull 
```

