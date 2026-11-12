<!-- Q: Compare Docker containers and virtual machines. -->

Containers share the host's kernel and isolate processes; VMs run a full guest OS on virtualized hardware, so containers are lighter and faster, while VMs isolate more strongly.

| | Docker container | Virtual machine |
|---|---|---|
| Isolation | Process-level (namespaces, cgroups) | Hardware-level (hypervisor) |
| Kernel | Shared with host | Own kernel per VM |
| Startup | Sub-second to seconds | Tens of seconds to minutes |
| Size | MBs (image layers) | GBs (full OS disk) |
| Overhead | Near-native | Reserved RAM/CPU for the guest OS |
| OS flexibility | Must match host kernel type (Linux containers need a Linux kernel) | Any guest OS (Windows, Linux, BSD) |
| Security boundary | Weaker: a kernel exploit can reach the host | Stronger: attacker must also escape the hypervisor |
| Portability | Same image runs anywhere with a container runtime | Disk images are heavier and tied to hypervisor formats |

**Choose containers when** you deploy many small services, need fast scaling, or want reproducible dev and CI environments.

**Choose VMs when** you run untrusted or multi-tenant workloads, need a different OS or kernel version, or need strict compliance isolation.

They also combine well. Most cloud container platforms run containers inside VMs, so you get the VM's isolation boundary and the container's packaging and speed. On your Mac, Docker Desktop does exactly this: it runs a small Linux VM and puts your containers inside it.

If you tell me your workload, I can recommend one for it.
