---
_db_id: 1023
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/kubernetes/deploy-app-with-manifest-file/install-postgresql
ready: true
submission_type: continue_repo
tags:
- kubernetes
title: Deploy the Frontend
---

Let's get our frontend (Nginx with the `index.html` file up and running).

Our Nginx service will run only on HTTP now, since the TLS termination will happen at the Ingress, making it way simpler.

First, let's create a `nginx.conf` file under `k8s/nginx/` with the following content:

```nginx
server {
    listen 80;
    
    location / {
        root /usr/share/nginx/html/;
        index index.html;
    }
}
```

Now copy the `nginx/Dockerfile` from the `nginx/` to the `k8s/nginx/` folder and edit the its first `COPY` line to refer to the file we just created:

```
# change this:
COPY https-nginx.conf /etc/nginx/conf.d

# to this:
COPY nginx.conf /etc/nginx/conf.d
```

Finally, copy the `nginx/index.html` file to the `k8s/nginx/` folder.

We are copying the files just to make sure we have everything we need under the `k8s` folder, make it easier to deploy and debug if anything goes wrong. This is how the file structure should look so far:

```
k8s
├── cert-manager
│   └── issuer.yaml
├── harbor
│   └── values.yaml
├── ingress-nginx
│   └── values.yaml
└── nginx
    ├── Dockerfile
    ├── index.html
    └── nginx.conf
```

Commit the changes and pull them on your EC2 instance.

Let's build and push our Nginx Docker image:

```
# builds and pushes the docker image
# notice we are using a new `v2` tag!
cd /home/ubuntu/umuzi-k8s/k8s/nginx
docker build . -t harbor.<your-domain>/application/nginx:v2 --push
```

To finish it up the frontend deployment, let's create a Kubernetes Deployment (remember, it manages Pods!) pointing to our new `nginx:v2` container image.

Create a file named `deployment.yaml` under `k8s/nginx/` with the following content:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        # remember to point to your own Harbor instance!
        image: harbor.<your-domain>/application/nginx:v2
      imagePullSecrets:
        - name: your-regcred
```

Let's finish the frontend app by adding its network components.

First, let's create a `Service` to expose the Nginx port to the cluster. Add the following content under `k8s/nginx/` in a file named `service.yaml`:

```
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

And lastly, let's create an Ingress to expose the Nginx externally. The Ingress will also manage the HTTPS for us, telling `cert-manager` to generate the TLS certificates.

Create a file named `ingress.yaml` under `k8s/nginx` with the content below:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
  annotations:
    # here is how we tell cert-manager to generate the TLS certs!
    cert-manager.io/cluster-issuer: letsencrypt-prod
    
    # and we are also forcing traffic to be HTTPs-only
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    # change it to, well, your domain
    - <your-domain>
    # here is where the TLS certs will be stored
    secretName: nginx-tls-secret
  rules:
  # change it to, well, your domain
  - host: <your-domain>
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            # points to the service we created on the file above
            name: nginx-service
            port:
              number: 80
```

That's a lot of files, but we are good to go! Commit everything, push the changes to GitHub and pull them back on your EC2 instance. Once there, let's apply everything:

```
cd /home/ubuntu/umuzi-k8s

kubectl apply -f k8s/nginx/deployment.yaml
kubectl apply -f k8s/nginx/service.yaml
kubectl apply -f k8s/nginx/ingress.yaml
```

You can check everything we just create by getting multiple resources at once! Here we will also supply the output, so you can compare with yours (it will be slightly different, things like the Pod name, domain, IP addresses etc):

```
kubectl get pod,service,ingress

NAME                                   READY   STATUS    RESTARTS   AGE
pod/postgresql-0                       1/1     Running   0          54m
pod/nginx-deployment-8d6f76d6b-8slnx   1/1     Running   0          97s
pod/nginx-deployment-8d6f76d6b-7rw4h   1/1     Running   0          87s

NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes      ClusterIP   10.43.0.1       <none>        443/TCP    25h
service/postgresql-hl   ClusterIP   None            <none>        5432/TCP   54m
service/postgresql      ClusterIP   10.43.6.37      <none>        5432/TCP   54m
service/nginx-service   ClusterIP   10.43.232.235   <none>        80/TCP     74s

NAME                                      CLASS   HOSTS                ADDRESS                      PORTS     AGE
ingress.networking.k8s.io/nginx-ingress   nginx   student-1-k42s.org   172.31.9.207,3.145.168.220   80, 443   51s
```

Now you can roll to your browser, access the `https://<your-domain>` address and check your application up and running! The button won't work yet, we still need our backend!