---
title: Deploy the Frontend
content_type: topic
---

To deploy the frontend with Helm, we need 3 things:
- Create a Deployment template 
- Create a ConfigMap template
- Update the `helm/buttons/values.yaml` parameters

First, let's create the Deployment template on the `helm/buttons/templates/nginx-deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Values.nginx.name }}
  labels:
    {{- include "button.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.nginx.replicaCount }}
  selector:
    matchLabels:
      {{- include "button.selectorLabels" . | nindent 6 }}
      app: {{ .Values.nginx.name }}
  template:
    metadata:
      {{- with .Values.podAnnotations }}
      annotations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      labels:
        {{- include "button.selectorLabels" . | nindent 8 }}
        app: {{ .Values.nginx.name }}

    spec:
      {{- with .Values.imagePullSecrets }}
      imagePullSecrets:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.nginx.image.repository }}:{{ .Values.nginx.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: {{ .Values.nginx.image.pullPolicy }}
          ports:
            - name: http
              containerPort: {{ .Values.nginx.service.port }}
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /
              port: http
          readinessProbe:
            httpGet:
              path: /
              port: http
          # mounting the ConfigMap
          volumeMounts:
            - name: nginx-config-volume
              mountPath: {{ .Values.nginx.mountPath}}
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
      # mounting the ConfigMap
      volumes:
        - name: nginx-config-volume
          configMap:
            name: nginx-config
```

Next, let's create a Kubernetes ConfigMap. They are usually used to store a configuration file which is then mounted into the Pod. This is useful if different Pods share the same configuration file or if different environments demand different configuration values.

Let's create the ConfigMap template under `helm/buttons/templates/configmap`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-config
data:
  nginx.conf: |
    server {
        listen {{ .Values.nginx.service.port }};
        server_name {{ .Values.nginx.serverName }};

        location / {
            root   {{ .Values.nginx.rootPath }};
            index  {{- range .Values.nginx.indexFiles }} {{ . }} {{- end }};
        }
    }
```

Finally, update the `helm/buttons/values.yaml` to contain the following parameters in the `nginx` key. Remember to substitute `<your-domain>` for the domain given to you by Umuzi.

```yaml
nginx:
  image:
    repository: harbor.<your-domain>/application/nginx
    tag: v2
  replicaCount: 1
  name: nginx
  serverName: <your-domain>
  rootPath: "/usr/share/nginx/html"
  mountPath: "/etc/nginx/conf.d"
  indexFiles:
    - "index.html"
    - "index.htm"
  service:
    type: ClusterIP
    port: 80

resources: 
  limits:
    cpu: 100m
    memory: 128Mi
  requests:
    cpu: 100m
    memory: 128Mi
```

Commit your changes, go to your EC2 instance and let's upgrade our Helm installation with the new resources.

```
cd /home/ubuntu/umuzi-k8s/helm
git pull

# upgrades the helm installation, since we already installed it in the last chapter
helm upgrade buttons buttons

# checks the deployment and configmap created
kubectl get deployment,configmap
```

You can check the frontend deployment at `https://<your-domain>`, but the button won't be working, we still need the backend!