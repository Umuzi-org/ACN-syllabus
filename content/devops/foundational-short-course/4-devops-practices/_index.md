---
content_type: topic
ready: true
title: DevOps Practices
---

The DevOps mantra is “automate everything!”. By applying DevOps practices, one can truly reach that.

## Continuous Integration (CI)
Is the practice of frequently merging software changes into a central repository. These changes are then built and tested. The objectives are finding errors and bugs quickly, improving the software quality, increasing collaboration and releasing new features and updates faster.

## Continuous Delivery (CD)
Expands the Continuous Integration practices by creating an artifact ready to be deployed at every software change merged into a central repository. It can be achieved by automatically rolling out and testing the artifact into different environments, like dev and staging, before considering it ready to go.

## Infrastructure as Code (IaC) & Configuration Management
Provisioning, maintaining and decommissioning data center components, such as servers, databases and network devices using software development techniques, like version control, automated testing, continuous integration and continuous delivery. IaC evolved rapidly with the proliferation of cloud providers, allowing infrastructure changes to be made via API calls. Most known tools are Terraform, Puppet, Ansible etc.

## Observability
Continually monitoring metrics and logs from applications and infrastructure is key for a smooth DevOps experience. Collecting and visualizing data will enable all the stakeholders to understand how their applications are being used, quickly find and fix errors, identify bottlenecks and develop needed features. On top of data, alerts can be set to identify situations where manual engineering intervention is needed to fix urgent issues.