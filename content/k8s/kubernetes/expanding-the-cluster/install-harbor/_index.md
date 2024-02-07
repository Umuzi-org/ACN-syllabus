---
content_type: topic
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/kubernetes/expanding-the-cluster/install-ingress-nginx
  soft: []
ready: true
submission_type: continue_repo
tags:
- kubernetes
title: Install Harbor
---

We will Harbor to push our application Docker containers to be used by the Cluster. On AWS you will likely end up using an external service like ECR but they serve the same function.

On the repository, create a file named `values.yaml` under `k8s/harbor` .

For simplicity, we are writing the Harbor admin password to the GitHub repository, but in production you would use a Kubernetes Secret for that. We will cover Secrets in the next chapter.

For the Harbor external URL, we will be using a subdomain named `harbor.<your-domain>`. Remember to override the field in the file below.

`k8s/harbor/values.yaml`
```
harborAdminPassword: "harbor12345"
externalURL: https://harbor.<your-domain>
expose:
  type: ingress
  tls:
    enabled: true
    certSource: auto
    auto:
      commonName: ""
    secret:
      secretName: "harbor"
  ingress:
    hosts:
      core: harbor.<your-domain>
    controller: default
    kubeVersionOverride: ""
    className: "nginx"
    annotations:
      nginx.ingress.kubernetes.io/ssl-redirect: "true"
      cert-manager.io/cluster-issuer: "letsencrypt-prod"
```

Let's add the Harbor Helm repository and update Helm's index:

```

helm repo add harbor https://helm.goharbor.io
helm repo update
```

Get the Helm template the to see what the default setting are:

```
helm -n template harbor harbor/harbor 
```

You'll notice that the default ingress points to `core.harbor.domain`. Let's change that with our custom `values.yaml`.

Run the template again but reference your `values.yaml`.

```
helm -n harbor template harbor harbor/harbor -f k8s/harbor/values.yaml
```

Now you'll see it is pointing to your `harbor.<your-domain>` .

Install the Helm chart and take a look at what it created:

```
# installs the chart
helm install harbor harbor/harbor \
  --namespace harbor \
  --create-namespace \
  -f k8s/harbor/values.yaml

# take a look at all the created components
kubectl -n harbor get pods
kubectl -n harbor get deployment
kubectl -n harbor get statefulset
kubectl -n harbor get pvc
kubectl -n harbor get ingress
kubectl -n harbor get certificate
kubectl -n harbor describe order
kubectl -n harbor get secret harbor-core -o yaml
```

For Kubernetes to be able to pull containers from Harbor we need to setup a Kubernetes Secret containing the login details.

A Secret is a Kubernetes resource used to store sensitive data, like passwords or tokens. Keep in mind that its content is not encrypted, just hashed using Base64.

```
kubectl create secret docker-registry your-regcred \
  --docker-server=harbor<your-domain> \
  --docker-username=admin \
  --docker-password=harbor12345
```