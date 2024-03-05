---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/github-actions/backend
ready: true
submission_type: continue_repo
tags:
- kubernetes
- github
title: Helm Chart Pipeline
---

For the Helm Chart pipeline, create a file named `helm.yaml` under `.github/workflows` and add the content below.

This time, we will run the Helm linter on its code, package and push it to Harbor as well! Helm Charts are also valid to any OCI (Open Container Initiative) repository, like Harbor.

```yaml
name: Build and Push Helm Chart to Harbor

on:
  push:
    paths:
      - 'helm/buttons/**'

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2

    - name: Build and Push Helm Chart
      env:
        DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
        HARBOR_ENDPOINT: ${{ secrets.HARBOR_ENDPOINT }}
      run: |
        cd helm
        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin $HARBOR_ENDPOINT
        helm lint buttons
        helm package buttons
        helm push buttons-*.tgz oci://$HARBOR_ENDPOINT/application
```

Again, the workflow will only be triggered where there's a change under the `helm/buttons/` directory. You can add a new empty file or change a description string.

Once you commit and push your changes, you will see the workflow running.

On the Harbor webpage, you'll see a new image under the `application` project!