<!-- Q: Compare Docker containers and virtual machines. -->

# Docker Containers vs. Virtual Machines

| Aspect | Containers (Docker) | Virtual Machines |
|---|---|---|
| **Isolation level** | Process-level; share the host OS kernel | Hardware-level; each VM runs its own full OS and kernel |
| **Architecture** | Container engine on top of host OS | Hypervisor (Type 1 or 2) on top of hardware/host OS |
| **Size** | Typically tens to hundreds of MB | Typically several GB (full OS image) |
| **Startup time** | Milliseconds to seconds | Tens of seconds to minutes |
| **Resource overhead** | Low; no guest OS to run | Higher; each VM reserves RAM/CPU for its guest OS |
| **Density** | Many per host (hundreds) | Fewer per host (tens) |
| **Performance** | Near-native | Slight to moderate overhead from virtualization |
| **Security** | Weaker boundary: a kernel exploit can affect the host and other containers | Stronger boundary: a compromise generally stays within the guest |
| **OS flexibility** | Must match host kernel type (Linux containers need a Linux kernel) | Any guest OS (Windows, Linux, BSD) regardless of host |
| **Portability** | Very high: image runs the same anywhere with a compatible engine | Portable but heavy; image formats vary by hypervisor |
| **Persistence** | Ephemeral by default; use volumes for data | Persistent disks by default |
| **Management/tooling** | Docker, Compose, Kubernetes, CI/CD-friendly | VMware, Hyper-V, KVM, VirtualBox, cloud instance tooling |

## Key Differences

- **What's virtualized:** VMs virtualize *hardware*; containers virtualize the *operating system* (namespaces and cgroups on Linux).
- **Kernel sharing:** This is the root of nearly every other difference. Sharing the kernel makes containers light and fast, but also limits isolation and OS choice.

## When to Use Which

**Containers are a good fit for:**
- Microservices and cloud-native apps
- CI/CD pipelines and reproducible dev environments
- Rapid scaling and high-density deployments
- Packaging an app with its dependencies

**VMs are a good fit for:**
- Running different operating systems on one host
- Strong isolation (multi-tenant workloads, untrusted code, compliance requirements)
- Legacy or monolithic applications that expect a full OS
- Workloads needing custom kernels or kernel modules

## Combining Them

They're not mutually exclusive. Most production container deployments run *inside* VMs (e.g., Kubernetes nodes on cloud instances), gaining VM-level isolation plus container-level agility. Technologies like Kata Containers and Firecracker blur the line further by running each container in a lightweight microVM.

**Note for macOS:** Docker Desktop on a Mac actually runs Linux containers inside a lightweight Linux VM, since containers need a Linux kernel.
