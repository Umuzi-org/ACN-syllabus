---
title: Creating the Ingress
content_type: topic
---

Now let's create our Ingress for the frontend and backend, as we did previously.

In the `helm/buttons/values.yaml` file, add the following below. Remember to substitute `<your-domain>` for the domain given to you by Umuzi.

```yaml
ingress:
  enabled: true
  className: nginx
  annotations: 
     nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
     cert-manager.io/cluster-issuer: letsencrypt-prod
  hosts:
    - host: <your-domain>
      paths:
        - path: /
          pathType: Prefix
          service:
            name: nginx
            port: 80
        - path: /api
          pathType: Prefix
          service:
            name: python
            port: 5000
  tls: 
   - secretName: nginx-tls-secret
     hosts:
       - <your-domain>
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
