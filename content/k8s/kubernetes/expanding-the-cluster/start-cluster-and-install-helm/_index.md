---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/kubernetes/k3s-quickstart
  - k8s/manual-app-deployment/project-overview
  soft: []
ready: true
submission_type: continue_repo
tags:
- kubernetes
title: Start the Cluster & Install Helm
---

Let's use a fresh EC2 instance and install K3s and Helm.

Normally you would install the necessary tools to manage the Kubernetes cluster and its environment – `kubectl`, `helm` and `fluxcd` – on your machine and communicate with the cluster remotely. Here we will install them on the EC2 instance to make sure everyone has the same environment.

Use the command bellow to install K3ds with Traefik disabled. We will install `nginx-ingress` later with a Helm chart.

```
# installs k3s
sudo curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server --disable=traefik" sh -

# gives read access to the `k3s.yaml` file
# which contains the credentials to access the cluster
sudo chown ubuntu:ubuntu /etc/rancher/k3s/k3s.yaml
sudo chmod 600 /etc/rancher/k3s/k3s.yaml
```

Install Helm on the EC2 instance:

```
# installs helm
sudo snap install helm --classic

# sets the environment variable used by Helm to access the cluster
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

# lists the charts, should be empty
helm list
```

Add the environment variable to the `.bashrc` file to be defined every time you login.

```
echo "export KUBECONFIG=/etc/rancher/k3s/k3s.yaml" >> ~/.bashrc
```