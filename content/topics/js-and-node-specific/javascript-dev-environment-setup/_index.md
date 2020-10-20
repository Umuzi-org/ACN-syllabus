---
_db_id: 135
content_type: topic
ready: true
title: Node setup
---

This is a guide to help lab assistants setup a local JavaScript environment.

### Step 1 – Add Node.js PPA

```
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -


Or

 sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
```

### Step 2 – Install Node.js on Ubuntu

```
sudo apt-get install nodejs
```

### Step 3 – Check Node.js and NPM Version

After installing node.js verify and check the installed version.

```
node -v
```

v13.0.1 or the latest version

Also, check the npm version

```
npm -v
```

6.12.0 the latest version