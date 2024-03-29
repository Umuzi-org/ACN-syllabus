---
_db_id: 1000
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/manual-app-deployment/nginx-installation
ready: true
submission_type: continue_repo
tags:
- kubernetes
- postgresql
title: PostgreSQL Installation
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