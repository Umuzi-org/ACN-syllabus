---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/helm-deployment/ingress
ready: true
submission_type: continue_repo
tags:
- kubernetes
- helm
title: Creating the Services
---

Let's add the Kubernetes Services to connect the Ingress we just created and the Deployments we will create, as we did in previous chapters.

Create two files named `helm/buttons/templates/nginx-service.yaml` and `helm/buttons/templates/python-service.yaml`.

On the first one, add the following content:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ .Values.nginx.name }}
  labels:
    {{- include "button.labels" . | nindent 4 }}
spec:
  type: {{ .Values.nginx.service.type }}
  ports:
    - port: {{ .Values.nginx.service.port }}
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app: {{ .Values.nginx.name }}
```

As you can see, the content from this file is coming from `.Values.nginx`. So let's update our `helm/buttons/values.yaml` with the newly required parameters:

```yaml
nginx:
  name: nginx
  service:
    type: ClusterIP
    port: 80
```

## Now a challenge!
Create yourself the `python-service.yaml` template and change the `values.yaml` file accordingly.

Commit your changes, go to your EC2 instance and upgrade the Helm installation with the new Services. If you don't remember the commands, check the {{< contentlink path="k8s/helm-deployment/ingress" >}} for tips!