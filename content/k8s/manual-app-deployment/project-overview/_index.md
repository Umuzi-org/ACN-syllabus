---
_db_id: 995
content_type: project
flavours:
- none
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/introduction
ready: true
submission_type: repo
tags:
- kubernetes
title: Manual App Deployment – Project Overview
---

The project involves setting up a secure web infrastructure by implementing these key components:

1. Obtain an SSL certificate from Let's Encrypt using Certbot - vital for encrypting your site and API with HTTPS. [https://certbot.eff.org/](https://certbot.eff.org/)
2. Use Nginx as a web server and reverse proxy. It manages traffic efficiently, serving as the gateway between clients and Python API. [https://www.nginx.com/](https://www.nginx.com/)
3. Develop a Flask API that handles client requests and provides services over HTTPS. [https://flask.palletsprojects.com/en/3.0.x/](https://flask.palletsprojects.com/en/3.0.x/)
4. Set up a reverse proxy within Nginx pointing to your Flask app, ensuring smooth communication.

By integrating these components, your project will offer secure client access, host a Python (Flask) API, and maintain stable performance in various environments.

**The deliverable of each module will be the URL from your live deployment**.

**We will also be checking the Git commits from the GitHub repositories**.