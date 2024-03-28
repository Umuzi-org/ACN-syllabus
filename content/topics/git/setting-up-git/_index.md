---
content_type: topic
title: "Introduction to Git and GitHub Part: 1"
ready: True
---

# Introduction to Git and GitHub

Git is a free, open-source version control system that's designed to manage projects of all sizes with speed and efficiency. GitHub, meanwhile, is a cloud-based service that lets you host Git repositories. While Git tracks the changes in your files, GitHub provides a platform for sharing those files and collaborating with others.

### The Value of Git in Professional Workflows

- **Efficiency**: Git makes technical workflows more streamlined, simplifying the management of complex data science and DevOps projects.
- **Documentation**: A complete history of your project's changes is documented in an accessible and understandable way.
- **Collaboration and Open Source**: GitHub has become a hub for collaborative projects and open-source contributions, offering vast opportunities for learning and sharing.

## Installing and Configuring Git for the First Time

To start using Git and GitHub, you first need to set up Git on your computer. Here's how:

### Installation

1. **Windows**:
   - Download the Git installer from [git-scm.com](https://git-scm.com/).
   - Run the installer and follow the instructions. The default settings are usually fine unless you have specific needs.

2. **Mac**:
   - Install the Xcode Command Line Tools by running `xcode-select --install` in the terminal.
   - Alternatively, download the Git installer from [git-scm.com](https://git-scm.com/).

3. **Linux**:
   - Use your distribution's package manager. For Ubuntu or Debian, for example, run `sudo apt-get install git`.

### Configuration

Once Git is installed, configure it with your username and email address. This step is crucial because Git uses this information to identify who makes changes to the files.

Open a terminal or command prompt and type the following commands, replacing "Your Name" and "your_email@example.com" with your own details:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```