---
title: 1.1 Setup EC2
content_type: topic
tags: 
- kubernetes
prerequisites:
  hard:
  - k8s/bare-bones-deployment/project-overview
ready: false
---

TODO: Content to be reviewed if we automate the EC2 instance creation.

**Create a Key Pair:**

If you don't have an existing key pair, you'll need to create a new one. This key pair is used to securely access your instance.

**Launch Instances:**

After creating or selecting a key pair, click "Launch Instances."

**View Instances:**

Once your instance is launched, go to the EC2 Dashboard, and under "Instances," you should see your new instance.

By default, instances launched in a public subnet should receive a public IP address. Ensure that your security group allows inbound traffic on the required ports, and your subnet is associated with a route to the internet (e.g., through an Internet Gateway in your VPC).

Keep in mind that AWS services and the user interface may change over time, so it's a good idea to refer to the AWS documentation for the most up-to-date information.
