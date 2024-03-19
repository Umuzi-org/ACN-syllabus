---
_db_id: 1036
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/github-actions/frontend
ready: true
submission_type: continue_repo
tags:
- kubernetes
- github
title: Backend Pipeline
---

Now that you understand how a workflows works, create a file named `python.yaml` under `.github/workflows` to build and push the backend Docker image.