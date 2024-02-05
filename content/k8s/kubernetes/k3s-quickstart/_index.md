---
title:  K3S Quick Start
content_type: topic
tags:
- kubernetes
prerequisites:
  hard:
  - k8s/containers-with-docker/running
flavours:
- none
ready: true
---

Deployments provides a declarative configuration for Pods. It allows configuring Pod's replicas (so more than one are running), update the images from the containers running inside the Pod and rollout these changes gradually.

Under the hood, Deployments control ReplicaSets which in turn control Pods. We won't get this deep here, but it is good to know!

On your EC2 instance, create a file named `deployment.yaml`.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  # how many Pods will be running
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      # connecting to the Service resource
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx-container
        image: nginx
```

Apply the file with the following command:

```
kubectl apply -f deployment.yaml
```

When you get the Pods, you'll see 2 replicas:

```
kubectl get pod
```

When you get the Endpoints, you'll see 2 IP addresses, one for each replica. The Service will load balance the network requests between both replicas.

```
kubectl get endpoints nginx-service
```

You can also see more information about the Deployment itself:

```
# gets the deployment
kubectl get deployment nginx-deployment

# more descriptive information
kubectl describe deployment nginx-deployment
When you delete a Pod, it will restart automatically:
# gets the pods
kubectl get pods

# pick one and delete
kubectl delete pod <pod-name>

# returns two pods again
kubectl get pods
```

If there's a new Nginx version and you want to update your service, Kubernetes will, by default, roll one replica at a time.

Let's update the image we are using for our container:

```
# edits the Kubernetes resource in-place
# good to play around, bad for production
kubectl edit deployment nginx-deployment

```

Find the `image: nginx` line and change it to `image: nginx:alpine3.18` and save the content.

If you quickly run kubectl get pod, you will see the rollout in progress. Kubernetes will create a third Pod with the new image, remove Pod with the old image, create another new Pod and delete the last old one. The output could look something like:

```
kubectl get pod

NAME                                READY   STATUS              RESTARTS   AGE
nginx-deployment-f4f77479-p9wlm     1/1     Running             0          9m22s
nginx-deployment-f4f77479-k9ldc     1/1     Running             0          9m22s
nginx-deployment-7b67b95f7b-zcc8b   0/1     ContainerCreating   0          2s
```