---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/fluxcd/postgresql-buttons
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
-- title: Automation

# Automation

Although we are now mostly automated we still need to push code then edit the values file to reflect the new docker tag to rollout new code, how about we automate this step.

Let's get flux to start staring at the docker-registry by using a imagerepository.

There are 4 things that make the automations work:
- ImageRepository: This is used to watch your harbor registry for new tags.
- ImagePolicy: The decision when a new tag is discovered whether to roll them out.
- ImageUpdateAutomation: The action of where to make the update in your gitrepository for the tag it discovered.
- # {"$imagepolicy": "flux-system:nginx:tag"} : in the *.yaml file where you want to update the tag you need to tell flux where to make the commit.

Copy the secret from buttons namespace to flux-system so that it can log in to image registry

```
kubectl get secret your-regcred -n buttons -o yaml | sed 's/namespace: buttons/namespace: flux-system/' | kubectl apply -n flux-system -f -
```

Create the file.

```
# apps/automation.yaml
---
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImageRepository
metadata:
  name: nginx
  namespace: flux-system
spec:
  image: <my.domain.com>/application/nginx
  interval: 1m
  secretRef:
    name: your-regcred
```

Now check if the imagerepository is loaded

```
kubectl -n buttons get ImageRepository
```

```
# apps/automation.yaml
---
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImageRepository
metadata:
  name: python
  namespace: flux-system
spec:
  image: <my.domain.com>/application/python
  interval: 1m
  secretRef:
    name: your-regcred
```

Now we need to give it a policy as we may not want to automate any new images

```
---
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImagePolicy
metadata:
  name: nginx
  namespace: flux-system
spec:
  imageRepositoryRef:
    name: nginx
  filterTags:
    pattern: '^*-[a-fA-F0-9]+-(?P<ts>.*)'
    extract: '$ts'
  policy:
    numerical:
      order: asc
```

You can do the same for python

Lastly we want to tell flux where to go make the commit once it receives an image it wants to update,

so we can add to our automations file the imageupdateautomation.

what this does is look for the apps/values.yaml and searches for # { your reference } then creates a commit with the relavant update



```
---
apiVersion: image.toolkit.fluxcd.io/v1beta1
kind: ImageUpdateAutomation
metadata:
  name: buttons
  namespace: flux-system
spec:
  git:
    checkout:
      ref:
        branch: main
    commit:
      author:
        email: fluxcdbot@users.noreply.github.com
        name: fluxcdbot
      messageTemplate: '{{range .Updated.Images}}{{println .}}{{end}}'
    push:
      branch: main
  interval: 1m0s
  sourceRef:
    kind: GitRepository
    name: flux-system
  update:
    path: ./apps/buttons/values.yaml
    strategy: Setters
```

And the last piece to this puzzle is the refrence inside the values.yaml file.

```
# apps/buttons/values.yaml
---
nginx:
  image:
    repository: ross-docker.whatever.beer/application/nginx
    tag: main-3e54d47-1706726487 `# {"$imagepolicy": "flux-system:nginx:tag"}`
python:
  image:
    repository: ross-docker.whatever.beer/application/python
    tag: main-a6c715b-1706875745 `# {"$imagepolicy": "flux-system:python:tag"}`
```

Now when you create a new build you will notice that flux updates your values.yaml and the new image rolls out automatically.