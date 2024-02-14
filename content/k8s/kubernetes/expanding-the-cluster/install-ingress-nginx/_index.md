---
_db_id: 1016
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/kubernetes/expanding-the-cluster/install-cert-manager
ready: true
submission_type: continue_repo
tags:
- kubernetes
title: Install ingress-nginx
---

Let's install ingress-nginx using a Helm chart. It will manage the ingress for us (instead of the default Traefik supplied by K3s, which we disable when creating the cluster). The Ingress will be used to allow external access to internal applications managed by Kubernetes.

Instead of injecting values from the command line using the `--set` flag like twe did for `cert-manager`, we will use a values file to overwrite the default configuration given by the Helm chart.

On the GitHub repository, under the `k8s/ingress-nginx` create a file named `userSuppliedValues.yaml`.

Change `<ip-address>` to the IP address given to you by Umuzi. Remember surround it with double quotes.

`k8s/ingress-nginx/userSuppliedValues.yaml`
```
controller:
  admissionWebhooks:
    certManager:
      enabled: "true"
  service:
    externalIPs: ["<ip-address>"]
```


Commit the file and push the changes.

Let's install the ingress-nginx.


```
# adds the nginx-ingress repository
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

# updates the Helm index
helm repo update
```


Now install the Ingress with your own values`.yaml` file.


```
helm install ingress ingress-nginx/ingress-nginx \
    --namespace ingress \
    --create-namespace \
    -f k8s/ingress-nginx/values.yaml
```


Now that we have the Ingress Controller installed, let's check if the Pod is healthy and confirm the public IP address.

```
# keeps getting the pods until we CTRL+C
kubectl -n ingress get pods --watch

# check if the correct public IP address is listed
kubectl -n ingress get svc
```

You'll notice a Service with the ClusterIP type and a LoadBalancer Service with the external IP. Although we added our Ingress here, in production you might use the AWS NLB to load balance requests from outside the cluster.