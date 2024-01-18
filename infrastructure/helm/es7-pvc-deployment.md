# Description

I'm looking to setup a ES7 in our cluster. First idea was to make a regular deployment and load the data using elasticdump, but I'll have to do that everytime, so I stopped that and started researching PVC `persistent volume claim`.

# Setup

1. Create a Persistent Volume Claim (PVC):
1. Define a Persistent Volume Claim (PVC) that Elasticsearch will use to store its data. This PVC will request a specific amount of storage from the underlying storage class.

```shell
helm create ES7.10-chart
```

creates an ES7.10 chart with deployments, configurations and other stuff 