---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/github-setup
  - k8s/manual-app-deployment/project-overview
ready: true
submission_type: continue_repo
tags:
- kubernetes
- certbot
title: Install Certbot
---

Nowadays, one prerequisite to run a web application is the Transport Layer Security, or TLS, a security protocol which ensures that the data exchanged between the user and server is encrypted. A web application running with TLS becomes a more secure application: HTTP + TLS = HTTPS.

The basis of TLS lies on the TLS certificate, also known as SSL certificate, which is issued by a certificate authority who can guarantee that the person or organization running the application is who they claim to be.

In this chapter we will be using a tool called [certbot](https://certbot.eff.org/) to generate the TLS certificates with the [Let's Encrypt](https://letsencrypt.org) certificate authority and use them in our web application.

You can read more about TLS [here](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/).

Let's install certbot and run in `certonly` mode to generate the certificates. Take note of the paths it spits out where it stores the certificate, it should something like:

```
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/<your-domain>/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/<your-domain>/privkey.pem
```

```
# updates the package manager
sudo apt update

# installs the certbot
sudo apt install certbot -y

# initiates interactive certbot process
# choose `1: Spin up a temporary webserver (standalone)`
# enter the domain given to you by Umuzi and your email address
sudo certbot certonly

# generates the DH key to be used by NGINX
# this might take a while
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
```

What just happened?

Certbot facilitates the acquisition of SSL/TLS certificates by creating a temporary web server on the user's system. When initiated, Certbot responds to challenges from the Let's Encrypt Certificate Authority to verify domain ownership. The process involves the exchange of specific tokens, demonstrating control over the specified domains. Once validated, Let's Encrypt issues the certificates, and Certbot can automatically configure popular web servers for HTTPS. Certbot's automation extends to periodic certificate renewal, ensuring ongoing security. In essence, Certbot streamlines the complex process of obtaining and managing SSL/TLS certificates by automating the required tasks, making it user-friendly for implementing secure connections on websites.