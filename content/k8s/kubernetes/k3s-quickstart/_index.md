---
_db_id: 1015
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/containers-with-docker/running
  - k8s/manual-app-deployment/project-overview
ready: true
submission_type: continue_repo
tags:
- kubernetes
title: K3s Quick Start
---

Let's install K3s.

On your EC2 instance, run the following commands:

```
# installs k3s
curl -sfL https://get.k3s.io | sh -

# gives read access to the `k3s.yaml` file
# which contains the credentials to access the cluster
sudo chmod 644 /etc/rancher/k3s/k3s.yaml
```

This will start the master node with a SQLite database. Check if it worked:

```
# gets the node information
kubectl get node

# `describe` gives more detailed information
kubectl describe node
```

The default K3s installation comes with a couple of components, including Traefik, a reverse proxy (same purpose as Nginx).

Use the following command to see all the Pods running:

```
# gets all running Pods
# `-A` means all namespaces
kubectl get pod -A
```

With Traefik, we can already access its default web page externally.

On your browser, access the domain given to you by Umuzi on `https://<your-domain>` .

You should see:

```
404 page not found
```

***

Now let's create some Kubernetes resources to run a Nginx service and expose it publicly.

### Pod

A Pod is the smallest deployable computing unit in Kubernetes. It is a group of one or more containers sharing network and storage resources, like an IP address and volumes.

On your EC2 instance, create the following files named `pod.yaml`.

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
    - name: nginx-container
      image: nginx
```

To create the Pod, _apply_ the YAML file:

```
kubectl apply -f pod.yaml
```

Here are some useful commands to interact with Pods:

```
# gets minimum amount of information about the Pod
kubectl get pod

# gets a bit more information about the Pod
kubectl get pods -o wide

# gets descriptive, human readable output
kubectl describe pod nginx-pod

# gets the whole YAML manifest
kubectl get pod nginx-pod -o yaml

# watches the logs from the Pod
kubectl logs -f nginx-pod

# logs into the Pod (like SSH but not really!)
kubectl exec -it nginx-pod sh
```

### Service

A Service is a network Kubernetes resource which exposes a network application running inside one or multiple Pods. The default Service type – ClusterIP – creates DNS entries for each Pod matching the Service's selectors and load balance network requests between them.

A Service creates a DNS entry `<myservicename>` inside the cluster both addresses would be reachable from withing the cluster: `http://nginx-service:80` and `http://nginx-service.<namespace>.svc.cluster.local:80`.

A Service routes on the selector and needs to correspond to the label in the Deployment. If you have multiple Deployments using the same label you'll add all the Pods to the Service load balancer.

On your EC2 instance, create the following files named `service.yaml`.

```
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  # connects the Service and the Pod
  # the Pod should have a label app=nginx
  # we will fix that in a bit
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

To create the Service, _apply_ the YAML file:

```
kubectl apply -f service.yaml
```

```
# gets the services, `svc` is short for `service`
kubectl get svc

# gets descriptive, human readable output
kubectl describe svc nginx-service

# you should see the Pod IP address here
kubectl get endpoints nginx-service
```

Notice that the last command returned `<none>` where the Pod IP address should be. It means the Service and the Pod aren't connected.

To fix this, let's add a `label` to the Pod, the same key/value (`app: nginx`) pair we configured inside the Service `selector` .

Edit the `pod.yaml` file with the following content:

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  # same value in the Service.spec.selector
  labels:
    app: nginx
spec:
  containers:
    - name: nginx-container
      image: nginx
```

Apply the file and look at the Endpoints again:

```
kubectl apply -f pod.yaml
kubectl get endpoints nginx-service
```

You should see the Pod's IP address.

You can test the Service DNS entry by executing a `curl` command from within the Pod:

```
# logs into the Pod
kubectl exec -ti nginx-pod sh

# runs a `curl` command to the Service name
curl http://nginx-service:80
```

### Ingress

An Ingress exposes HTTP/HTTPS services to outside of the cluster.

It needs an Ingress Controller. K3s comes with Traefik by default, but later we will install the Nginx Ingress Controller.

Create a file named `ingress.yaml` :

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
spec:
  rules:
    # replace with your domain
    - host: <your-domain>
      http:
        paths:
          # URL path poiting to the Nginx Pod
          - path: /nginx
            pathType: Prefix
            backend:
              # connects to the Service we just created
              service:
                name: nginx-service
                port:
                  number: 80
```

Apply the file:

```
kubectl apply ingress.yaml
```

Some useful commands:

```
# gets a list of ingress resources
kubectl get ingress

# gets more information aobut the `nginx-ingress`
kubectl describe ingress nginx-ingress
```

In your browser, navigate to `https://<your-domain>/nginx` and you should see the default Nginx page.

We just deployed an application and exposed it externally!

### Deployment

What happens if a service fails? It usually should be restarted (at least a couple of times) before manual intervention.

Unfortunately Pods won't to that. When they fail, they simply stop.

Let's delete the Pod we created (simulating a failure).

```
# deletes a Pod
kubectl delete pod nginx-pod
```

The Pod is gone. Forever.

Deployments provide a declarative configuration for Pods. It allows configuring Pod's replicas (so more than one are running), update the images from the containers running inside the Pod and rollout these changes gradually.

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