---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/github-actions/github-configuration
ready: true
submission_type: continue_repo
tags:
- kubernetes
- github
title: Frontend Pipeline
---

Let's create a workflow to build and push the Nginx Docker image.

Create a file named `nginx.yaml` under `.github/workflows` with the following content:
```yaml
name: Build and Push Nginx to Harbor

on:
  # 1 
  push:
    paths:
      - 'k8s/nginx/**'

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    # 2
    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2

    # 3
    - name: Set outputs
      id: vars
      run: echo "::set-output name=sha_short::$(git symbolic-ref --short HEAD)-$(git rev-parse --short HEAD)-$(date +%s)"

    # 4
    - name: Build and Push Docker Image
      env:
        # 5
        DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
        HARBOR_ENDPOINT: ${{ secrets.HARBOR_ENDPOINT }}
        IMAGE_TAG: ${{ steps.vars.outputs.sha_short }}
      # 6
      run: |
        cd k8s/nginx
        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin $HARBOR_ENDPOINT
        docker build -t $HARBOR_ENDPOINT/application/nginx:$IMAGE_TAG . --push
```

What does it do?
1. This GitHub Action will run on every commit _only_ if there's a change under the `k8s/nginx` folder, avoiding unnecessary runs if the Nginx application isn't changed.
2. First step is to checkout the repository code.
3. Set a variable that will be our Docker image tag, in this case, it will be `<branch-name>-<commit>-<date>`.
4. Builds and pushes the Docker image.
5. Sets the environment variables used to authenticate with Harbor and to set the Docker image tag.
6. Runs the commands we already know: `docker login` and `docker build --push`.

Since it will only run when there's a change inside the `k8s/nginx`, perform a simple edit on the `k8s/nginx/index.html` – change some text, for example – to trigger this workflow.

Commit the changes and push to GitHub.

Now, when you go to the GitHub repository page and click on `Actions`, you should see your workflow running!

Once the workflow is finished, checkout the Harbor webpage to see your newly created Docker image.