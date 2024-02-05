---
title: Start cluster & install helm cli
content_type: topic
tags: 
- kubernetes
flavours:
- none
prerequisites:
  hard: 
  - k8s/kubernetes-quickstart/k3s-quickstart
  soft: []
ready: true
---

# Start cluster & install helm cli

Let's use a fresh EC2 instance and install K3s and Helm.

Normally you would install the necessary tools to manage the Kubernetes cluster and its environment – `kubectl`, `helm` and `fluxcd` – on your machine and communicate with the cluster remotely. Here we will install them on the EC2 instance to make sure everyone has the same environment.&#x20;

Use the command bellow to install K3ds with Traefik disabled. We will install `nginx-ingress` later with a Helm chart.

<pre><code><strong># installs k3s
</strong><strong>sudo curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server --disable=traefik" sh -
</strong><strong>
</strong># gives read access to the `k3s.yaml` file
# which contains the credentials to access the cluster
sudo chown ubuntu:ubuntu /etc/rancher/k3s/k3s.yaml
sudo chmod 600 /etc/rancher/k3s/k3s.yaml
</code></pre>

Install Helm on the EC2 instance:

<pre data-overflow="wrap"><code><strong># installs helm
</strong><strong>sudo snap install helm --classic
</strong><strong>
</strong><strong># sets the environment variable used by Helm to access the cluster
</strong>export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

# lists the charts, should be empty
helm list
</code></pre>

Add the environment variable to the `.bashrc` file to be defined every time you login.

```
echo "export KUBECONFIG=/etc/rancher/k3s/k3s.yaml" >> ~/.bashrc
```