---
title: Install cert-manager
content_type: topic
tags: 
- kubernetes
flavours:
- none
prerequisites:
  hard: 
  - k8s/expanding-the-cluster/start-cluster-and-install-helm-cli
  soft: []
ready: true
---

cert-manager is a Kubernetes Controller used to manage certificates. It will substitute the `certbot` we used on the previous chapters.

Let's install it using Helm:

```
# adds the cert-manager Helm repository
helm repo add jetstack https://charts.jetstack.io

# updates the helm index
helm repo update

# installs cert-manager
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.13.2 \
  --set installCRDs=true \
  --set prometheus.enabled=false
```

You will notice that the `--set` flags inject values into the Helm chart, customizing it. You can also run the `template` sub command to see what the manifest file looks like.

```
# gets the Helm chart full YAML content
# massive output!
helm template jetstack/cert-manager
```

Remember the `umuzi-k8s` GitHub repository? Let's start using it again to keep track of the YAML files we will create to setup our Kubernetes Cluster.

Create a file under `k8s/cert-manager/` name `issuer.yaml`. Here we will define `ClusterIssuer` resource, which will communicate with Let's Encrypt when we request a certificate later own.

`k8s/cert-manager/issuer.yaml`
```
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
  namespace: cert-manager
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    # replace with your own email
    email: <your-email>
    
    # secret resource that will be used to store the account's private key
    privateKeySecretRef:
      name: letsencrypt-prod    
    solvers:
      - http01:
          ingress:
            ingressClassName: nginx
```


On the EC2 instance, pull the changes from the repository and apply the file:

```
# pull the changes
cd /home/ubuntu/umuzi-k8s
git pull

# applies the file
kubectl apply -f k8s/cert-manager/issuer.yaml
```

Let's take a look at what we have created:

```
# gets the clusterissuers resources
kubectl get clusterissuer

# gets the namespaces
# see that we have a new one, `cert-manager`
kubectl get namespace

# gets the pods under the `cert-manager` namespace using the `-n flag
kubectl -n cert-manager get pods

# gets the pods under the `kube-system` namespace
kubectl -n kube-system get pods
```

