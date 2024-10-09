# POC Proposal for Implementing Karpenter in Our Kubernetes Clusters

## What is Karpenter?
Karpenter’s an open-source autoscaling tool that’s quicker and smarter than the default Kubernetes Cluster Autoscaler. It’s designed for optimizing cost and resource usage in cloud environments.

## Why is it better than manual autoscaling and preempetive Nodes:
- Faster scaling: Adds nodes quicker than Cluster Autoscaler when workloads spike.
- Cost optimization: Automatically uses cheaper spot instances but falls back to on-demand if needed.
- Efficient: right-sizes nodes to reduce resource waste.
- Flexible: picks the best instance types based on workload needs.
- Simple: no need for pre-defining node groups or configuring scaling policies manually.

## pros/cons

### +
- Open Source
- Heard that sumup is currently migrating to it and it's being used by big companies.
- Uses native APIs, which makes it easy to use.
- Supports different instance types and pricing models, including Sharons suggestion to use pre-perchased storage commitmants.
- Improved scheduling compared to cluster autoscaler.

### -

- New concepts mean a need to test this out. Some time needed for the team to get up to speed.
- It’s a newer tech so there may be unexpected issues. Might hit edge cases or bugs
- Not as configurable as doing it manually.
- Relies on cloud provider APIs changes there could impact it.

## Game Plan for the POC

### Phase 1: Setup

Use a dedicated POC fresh cluster, as Sharon suggested.
Could be Matilda/Monolith(whichever one was not prod) if they’re free.
Have to dig in if minikube is also an option.
Set up Karpenter with basic config, integrate with the cloud provider, and configure IAM roles.
#### Q: Not sure about what access rights are required?

### Phase 2: Testing

Deploy a basic app to simulate workloads.
Test different scaling scenarios: bursts, steady growth, resource-heavy tasks.
Tweak Karpenter settings (e.g., spot usage, instance types) and observe the response.
#### S: Might need support for testing different scenarios. 
#### S: Will definitely need support for configuring pricing models.



### Question: 
- Q: Access rights: I'll definitely need someone with access rights for certain situations.
- Q: Should we implement a monitoring tool like Grafana/Prometheus to monitor.
- Q: Chaos engineering? Maybe? Yes?
- Q: What concerns would you give trying this on our development cluster once setup and testing pass? 

