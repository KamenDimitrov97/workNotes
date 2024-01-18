# DOCKER CE

Docker is a container runtime engine which allows you to package an application with all of its dependencies into a standardized unit for software development.

Docker containers wrap up a piece of software in a complete filesystem that contains everything it needs to run: code, runtime, system tools, system libraries – anything you can install on a server. This guarantees that it will always run the same, regardless of the environment it is running in.

Here we’ll cover installation of Docker CE on Ubuntu, Debian, Fedora, and CentOS and Arch Linux distributions.

# Install

The last item to install is the Docker machine driver for KVM. Download the binary and make it executable.

```shell
curl -LO https://storage.googleapis.com/minikube/releases/latest/docker-machine-driver-kvm2
chmod +x docker-machine-driver-kvm2
sudo mv docker-machine-driver-kvm2 /usr/local/bin/
```