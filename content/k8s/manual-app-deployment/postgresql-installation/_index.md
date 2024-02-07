---
title: PostgreSQL Installation
content_type: project
tags:
- kubernetes
- postgresql
prerequisites:
  hard: 
  - k8s/manual-app-deployment/nginx-installation
  soft: []
ready: true
submission_type: continue_repo
from_repo: k8s/manual-app-deployment/project-overview
---

Let's install PostgreSQL.

```
# updates the package manager
sudo apt update

# installs PostgreSQL
sudo apt install postgresql postgresql-contrib -y
```

The following commands will prepare PostgreSQL to be used by the Flask app.

To avoid any issues with PostgreSQL shell, please type the commands below one by one.

```
# logs in as the `postgres` user
sudo -i -u postgres

# opens the PostgreSQL shell
psql

# creates the databse
CREATE DATABASE yourdb;

# creates the user/password
CREATE USER youruser WITH PASSWORD 'yourpassword';

# allows the user access to the databse
GRANT ALL PRIVILEGES ON DATABASE yourdb TO youruser;

# exits the PostgreSQL shell
exit

# logs back to your instance user
logout
```