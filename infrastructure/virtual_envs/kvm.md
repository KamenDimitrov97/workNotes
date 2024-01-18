KVM (for Kernel-based Virtual Machine) is a full virtualization solution for Linux on x86 hardware containing virtualization extensions (Intel VT or AMD-V).

It consists of a loadable kernel module, kvm.ko, that provides the core virtualization infrastructure and a processor specific module, kvm-intel.ko or kvm-amd.ko. It has received huge adoption on enterprise over the last few years.

# Install

you can go through this guide: https://computingforgeeks.com/install-kvm-centos-rhel-ubuntu-debian-sles-arch/

For the Ubuntu system, all packages required to run KVM are available on official upstream repositories. Install them using the commands:

```shell
sudo apt update
sudo apt -y install qemu-kvm libvirt-dev bridge-utils libvirt-daemon-system libvirt-daemon virtinst bridge-utils libosinfo-bin libguestfs-tools virt-top
```

Load and enable the modulevhost-net.

```shell
sudo modprobe vhost_net
sudo lsmod | grep vhost
echo "vhost_net" | sudo tee -a /etc/modules
```

cheat sheet: https://computingforgeeks.com/virsh-commands-cheatsheet/

books on the subject:
https://www.amazon.co.uk/dp/1784399051/ref=as_li_tl?ie=UTF8&linkCode=gs2&linkId=e4e16b6c501b69634d21b5ea568be048&creativeASIN=1784399051&tag=computingforg-21&creative=9325&camp=1789

https://www.amazon.co.uk/dp/1119267722/ref=as_li_tl?ie=UTF8&linkCode=gs2&linkId=8d888087d6c8b5584d3b65cb91615adf&creativeASIN=1119267722&tag=computingforg-21&creative=9325&camp=1789


# Usage

## Starting minikube on KVM

Add user to libvirt group 
```shell
sudo usermod -aG libvirt $USER
newgrp libvirt
```

Set KVM as default driver:
```shell
minikube config set vm-driver kvm2
```

