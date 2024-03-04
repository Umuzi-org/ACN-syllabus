
---
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/fluxcd/uninstall-k3s
ready: true
submission_type: continue_repo
tags:
- kubernetes
- fluxcd
title: Setup postgressql backend

---

# Setup postgressql backend

When no flags are used when starting k3s it uses a sqlite backend that's not very stable and quickly fails. To give us a more sturdy backend let's use postgressql instead.

```
# logs in as the `postgres` user
sudo -i -u postgres

# opens the PostgreSQL shell
psql

# creates the databse
CREATE DATABASE kubernetes;

# creates the user/password
CREATE USER k3s WITH PASSWORD 'yourpassword';

# allows the user access to the databse
GRANT ALL PRIVILEGES ON DATABASE kubernetes TO k3s;

# exits the PostgreSQL shell
exit

# logs back to your instance user
logout
```