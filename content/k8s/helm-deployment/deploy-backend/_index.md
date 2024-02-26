---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/helm-deployment/deploy-frontend
ready: true
submission_type: continue_repo
tags:
- kubernetes
- helm
title: Deploy the Backend with Helm
---

Let's finish up by deploying our backend. First, update the `python` key under the `helm/buttons/values.yaml` file with the following content:

```yaml
python:
  image:
    repository: harbor.<your-domain>/application/python
    tag: v2
  name: nginx
  name: python
  envs:
    - name: DB_HOST
      value: "postgresql.default.svc.cluster.local" 
    - name: DB_NAME
      value: dbname
    - name: DB_USER
      value: youruser
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: postgresql
          key: password
  service: 
    type: ClusterIP
    port: 5000
```

And create the `helm/buttons/templates/python-deployment.yaml` file with the content below. A few things to notice:
- We are using the environment variables to connect to the PostgreSQL database
- Reusing the resource limits from the `nginx` values
- Checking our application health with the `liveness` and `readiness` probes this time it's on `/health`
- Remember to add the selector matchLabels so that your service can route

Commit your changes, go to your EC2 instance and let's upgrade our Helm installation with the new resources.

```
cd /home/ubuntu/umuzi-k8s/helm
git pull

# upgrades the helm installation, since we already installed it in the last chapter
helm upgrade buttons buttons

# checks the created deployment 
kubectl get deployment
```

On your browser, go to `https://<your-domain>` and try out the Buttons app, now deployed fully with Helm!