---
title: Deploy the Backend
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
- Checking our application health with the `liveness` and `readiness` probes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Values.python.name }}
  labels:
    {{- include "button.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.python.replicaCount }}
  selector:
    matchLabels:
      {{- include "button.selectorLabels" . | nindent 6 }}
      app: {{ .Values.python.name }}
  template:
    metadata:
      {{- with .Values.podAnnotations }}
      annotations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      labels:
        {{- include "button.selectorLabels" . | nindent 8 }}
        app: {{ .Values.python.name }}
    spec:
      {{- with .Values.imagePullSecrets }}
      imagePullSecrets:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      securityContext:
        {{- toYaml .Values.podSecurityContext | nindent 8 }}
      containers:
        - name: {{ .Chart.Name }}
          securityContext:
            {{- toYaml .Values.securityContext | nindent 12 }}
          image: "{{ .Values.python.image.repository }}:{{ .Values.python.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: {{ .Values.python.image.pullPolicy }}
          ports:
            - name: http
              containerPort: {{ .Values.python.service.port }}
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /health
              port: http
          readinessProbe:
            httpGet:
              path: /health
              port: http
          env:
            {{- toYaml .Values.python.envs | nindent 12 }}
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
```

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
