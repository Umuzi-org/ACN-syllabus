---
content_type: topic
tags:
- kubernetes
ready: true
title: Continues deployment using fluxcd
---


Flux empowers seamless application deployment (CD) and progressive delivery (PD) with automated reconciliation, complemented by Flagger. This dynamic tool extends its capabilities to automatically push updates, including image scanning and patching, back to Git.

The beauty of Flux lies in its holistic approach to system management. Define your entire system's desired state in Git, encompassing applications, configurations, dashboards, monitoring, and more. YAML ensures conformance to this declared system, eliminating the need for manual kubectl operations—changes sync automatically.

The entire process is orchestrated through pull requests, offering a Git history that serves as a comprehensive record of transactions. This history facilitates state recovery from any snapshot, ensuring robust version control.

Security is at the forefront of Flux's design. Operating on the principles of pull versus push, adhering to the least amount of privileges, and integrating tightly with Kubernetes security policies, Flux ensures a secure deployment environment. Its seamless collaboration with security tools and best practices further reinforces its commitment to a robust security framework. For more insights, delve into our detailed security considerations.