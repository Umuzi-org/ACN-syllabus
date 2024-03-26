---
title: Virtualization
content_type: topic
ready: True
---

Virtualization is the act of creating a virtual version of something. Here, it means creating a virtual version of a **server**, called a virtual machine (VM).

A virtual machine (or *guest machine*) acts like a real computer with a real operating system and applications, but runs *on top of* a bare metal machine, also known as the *host* or *hypervisor*. For example, a server running Ubuntu Linux could host a Microsoft Windows virtual machine, or vice versa.

Some virtualization technologies are:  
-VirtualBox  
-KVM  
-VMware  

Nowadays we have technology to virtualize other IT components as well, like storage and networks.

Know more:  
-[The two types of hypervisor](https://en.wikipedia.org/wiki/Hypervisor#Classification)  

The benefits of virtualization over bare metal include:  
-**Efficient resource use**: one server can run multiple VMs with different applications, better using its resources and having fewer physical machines.  
-**Automation**: now that servers are virtual, one can build and use software to manage the VMs.  
-**High availability and disaster recovery**: with VMs, backups become faster and easier (one can backup a whole virtual machine!), they can also be easily cloned and moved to another location in case of disaster, making them more portable.  

Although virtualization brings many benefits to the table, it also comes with challenges, like increasing the tooling cost, learning curve and increased attack surface (hypervisor level).

The main issue with virtualization is that the VM *still* runs its own operating system, consuming gigabytes of memory and disk and much CPU resources.

Instead of running Linux as the host with multiple Linuxes as VMs, could one share the underlying Linux kernel and basic building blocks, creating only a thin layer of isolation for each VM?
