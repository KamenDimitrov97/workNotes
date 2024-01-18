Minikube is a tool that allows you to run a single-node Kubernetes cluster on your local machine. It provides a lightweight, easy-to-use platform for testing and developing Kubernetes applications. With Minikube, you can quickly set up a Kubernetes environment on your laptop or desktop computer, and use it to experiment with Kubernetes features, test application deployment and scaling, and learn more about the Kubernetes ecosystem. Minikube is often used by developers and DevOps teams as part of their local development workflows.

# install

```shell
wget https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube-linux-amd64
sudo mv minikube-linux-amd64 /usr/local/bin/minikube
```

# Usage 

minikube start 

kubectl cluster-info

location of minkube config shit
~/.minikube/machines/minikube/config.json

access minikube-  `minikube ssh`

To stop a running local kubernetes cluster, run:

$ minikube stop

To delete a local kubernetes cluster, use:

$ minikube delete


## Tutorial 

minikube start

minikube dashboard

This command creates a Kubernetes deployment named "hello-node" with a single replica using the container image "registry.k8s.io/e2e-test-images/agnhost:2.39".

The container runs the "agnhost" binary with the argument "netexec" and sets the http port to 8080. The "agnhost" binary is a tool that simulates various network and storage services commonly used in Kubernetes testing environments.

Overall, this command sets up a basic deployment running a containerized application on a Kubernetes cluster.

```shell
kubectl create deployment scrubber --image=192.168.39.26:9153/scrubber:latest -- /agnhost netexec --http-port=3003
```

gets deployments for each node: 

```shell
kubectl get deployments
```


```shell
kubectl get pods
```

gets events 
```shell
kubectl get events
```

```shell
kubectl config view
```

This command creates a Kubernetes Service named "hello-node" and exposes it outside the cluster as a LoadBalancer on port 8080. The service is associated with the deployment named "hello-node" created in the previous command.

By creating a service, you can make the deployment available to other pods in the same Kubernetes cluster. By exposing the service as a LoadBalancer, you can make the deployment available to external clients outside of the Kubernetes cluster as well.

When you create a LoadBalancer service, the Kubernetes cluster will create an external load balancer that routes traffic to the service. Depending on the cloud provider or infrastructure being used, this may involve creating a public IP address or allocating a port on a load balancer.

Overall, this command allows you to access the deployment running the "hello-node" application from outside the Kubernetes cluster on port 8080.

```shell
kubectl expose deployment hello-node --type=LoadBalancer --port=8080
```

```shell
kubectl get services
```

```shell
kubectl delete service hello-node
kubectl delete deployment hello-node
```




Here are the high-level steps to follow:

    Run a local Docker registry:

    arduino

docker run -d -p 5000:5000 --name registry registry:2

This command starts a Docker container running a local Docker registry.

Tag your local Docker image with a name that includes the registry address and a version/tag:

bash

docker tag scrubber localhost:5000/scrubber:1.0

This command tags your local "scrubber" image with the name localhost:5000/scrubber:1.0.

Push the tagged image to the local Docker registry:

bash

docker push localhost:5000/scrubber:1.0

This command pushes the tagged "scrubber" image to the local Docker registry running at localhost:5000.

Use the image in your Kubernetes deployment:

bash

kubectl create deployment scrubber --image=scrubber:latest -- /agnhost netexec --http-port=3002

This command creates a Kubernetes deployment using the Docker image localhost:5000/scrubber:1.0.

should connect to docker in the minikube VM
$ eval $(minikube docker-env)


## uploading images to minikube 

1. one way is to build it inside minikube
    1. Enter minikube
```shell
minikube ssh
```
    2. inside minikube run docker build -t <image_name> <github url> (e.g. github.com/flaxandteal/scrubber#branchname:directory, branchname and directory not required)
https://minikube.sigs.k8s.io/docs/handbook/pushing/ reference




## Bugs

I've got the image uploaded to ssh in several ways but can't pull it when creating a deployment
I'm trying to make credentials now using 
```shell
kubectl create secret docker-registry my-registry-creds --docker-server=<registry-url> --docker-username=<username> --docker-password=<password> --docker-email=<email>
```
didn't try that yet

Phil made a PR to update the berlin and bonn-py packages 
robb is off until the 11th