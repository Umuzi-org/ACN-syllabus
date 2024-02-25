---
_db_id: 1010
content_type: topic
flavours:
- none
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/containers-with-docker/containers-overview
ready: true
tags:
- kubernetes
title: Install Docker and Docker Compose
---

To setup Docker and Docker Compose on your EC2 instance, run the following commands:

<pre><code># updates the packages index
sudo apt update

# installs necessary dependencies
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y

# configures the Docker apt repository
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" -y

# installs docker
sudo apt install docker-ce -y

# check docker status
sudo systemctl status docker    

# installs docker compose
<strong>sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
</strong>sudo chmod +x /usr/local/bin/docker-compose

# checks the docker compose installation
docker-compose --version

# allows the `ubuntu` user  to run Docker commands
# so we don't need to use `sudo` all the time!
sudo gpasswd -a ubuntu docker

# let's log out from the session and then SSH again into the server
# to refresh the user's permissions
logout
ssh -i &#x3C;key-file> ubuntu@&#x3C;your-domain>
</code></pre>

Some useful commands to use with Docker:

```
# lists containers
docker ps

# gets a container logs
docker logs -f <container>

# connects to the container (like SSH, but not really!)
docker exec -it <container> sh
```