---
content_type: topic
prerequisites:
  hard:
  - docker/intro-to-docker
ready: false
title: Troubleshooting Docker Desktop for Windows
---

Docker on Windows can be quite tricky to setup and get working, and a number of errors can occur when trying to get it up and running. In this topic, we will try and provide solutions to some of the problems you may encounter when dealing with Docker Desktop.

## Hyper-V
Docker Desktop requires Hyper-V to be installed as well as enabled on your machine. This installation is in the form of a feature. Click [here](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v) and follow the instructions to ensure Hyper-V is enabled on your machine.

### Help! I dont see Hyper-V on my list of Programs and features!
You are probably running a version of windows which does not have Hyper-V as a standard feature. Fear not because there is a way you can add it manually.

In order to do this, you will need to create a file, anywhere, using a text editor and copy the following into that file:

{{% code_snippet "hyperv.bat" %}}

Now save that as hyperv.bat from your text editor. The desktop or download folder are good destinations for which to save and easily located for the next step.

After exiting the editor, open file manager and right mouse click the file and choose run as administrator.

Once complete it will reboot your machine and you can turn on Hyper-v from programs and features.

Once this is done, it should allow you to run Docker Desktop without giving you any errors about Hyper-V

## Virtualization
If you are still getting some errors, your PC might have virtualization disabled. In order to run docker, or rather, any Virtual Machine on your Local Machine, you need to enable virtualization. Unfortunately this involves you going into the BIOS and enabling it there. The method can differ depending on what hardware you are using and you may need to delve a little deeper.

Here is a basic [link](https://www.minitool.com/news/enable-virtualization-windows-10.html) to get you started. If this method does not work for you, you will need to google your own hardware in order to enable virtualization on your machine.

## None of these helped me. I'm still stuck!
At this point Docker Desktop on Windows may not be compatible with your current setup. 
Your alternatives are

1.) Use WSL 2 as mentioned in the intro to docker Topic. Follow the instructions to install WSL and docker very carefully as missing one step may lead to Docker not working as expected.

2.) As an absolute last resort, installing a Linux Virtual Machine is an alternative as well. There are many free tools that allow for this such as [VMware](https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html). You will need to also download a Linux Operating System for it to use as well. Linux is open source, so this shouldnt be hard to find with some searching online. An easy search term for example would be "Ubuntu vmware image download".

3.) If you are unable to install a Virtual Machine on your current hardware setup, please contact a staff member to assist with your setup. DO NOT LEAVE THIS UNSOLVED!