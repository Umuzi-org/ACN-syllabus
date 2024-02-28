---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/helm-deployment/chart
ready: true
submission_type: continue_repo
tags:
- kubernetes
- helm
title: Creating the Ingress
---

Now let's create our Ingress for the frontend and backend, as we did previously.

In the `helm/buttons/values.yaml` file, add the following below **and complete the missing parts!**

```yaml
ingress:
  enabled: # make true to enable
  className: # run `kubectl get ingressclass` and use the value form there
  annotations: 
     nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
     cert-manager.io/cluster-issuer: # use the value from `kubectl get clusterissuer`
  hosts:
    - host: # this one you'll know by now
      paths:
        - path: /
          pathType: Prefix
          service:
            name: nginx
            port: 80
        - path: # add your prefix here for the backend
          pathType: Prefix
          service:
            name: # your backend service name
            port: # what port do you want to forward traffic on your backend?
  tls: 
   - secretName: nginx-tls-secret
     hosts:
       - # what is the domain you should use here?
```

Now create a new file, `helm/buttons/templates/ingress.yaml` and add the following YAML content:

```yaml
{{- if .Values.ingress.enabled -}}
{{- $fullName := include "button.fullname" . -}}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ $fullName }}
  labels:
    {{- include "button.labels" . | nindent 4 }}
  {{- with .Values.ingress.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
spec:
  ingressClassName: {{ .Values.ingress.className }}
  {{- if .Values.ingress.tls }}
  tls:
    {{- range .Values.ingress.tls }}
    - hosts:
        {{- range .hosts }}
        - {{ . | quote }}
        {{- end }}
      secretName: {{ .secretName }}
    {{- end }}
  {{- end }}
  rules:
    {{- range .Values.ingress.hosts }}
    - host: {{ .host | quote }}
      http:
        paths:
          {{- range .paths }}
          - path: {{ .path }}
            pathType: {{ .pathType }}
            backend:
              service:
                name: {{ .service.name }}
                port:
                  number: {{ .service.port }}
          {{- end }}
    {{- end }}
{{- end }}
```

Commit your changes, go to your EC2 instance and let's upgrade our Helm installation with the new added Ingress.

```
cd /home/ubuntu/umuzi-k8s/helm
git pull

# generates the template for visualization, now with the ingress
helm template buttons buttons

# upgrades the helm installation, since we already installed it in the last chapter
helm upgrade buttons buttons

# checks if the ingress was created
kubectl get ingress
```