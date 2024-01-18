# What can  it be used for

## Description

Persistent volume is a kubernetes resource like cpu and ram so it's configured on cluster creation by admin.
created via yaml as everything else 

- For databases
- For specific directories

Volumes - if you need data that doesn't depent on the pod lifecylce and can persist through pod destruction. `IF YOU NEED PERSISTENT DATA`
in order to connect the new pod to the volume you need to know it's node and since we don't know on which node the pod restarts
we need the volume to be available to all nodes `STORAGE MUST BE AVAILABLE TO ALL NODES`
lastly you need `STORAGE THAT CAN SURVIVE CLUSTER CRASH`

Piece of storage that has been provisioned in a cluster. It's a way to abstract and manage storage resources independently from Pods. PVs can be dynamically created or pre-provisioned, and they provide a stable, long-term storage solution that survives the lifecycle of Pods. PVs are managed by the cluster administrators and can be mounted into Pods using Persistent Volume Claims.

## PV


```yaml
kind: PersistentVolume
metadata:
  name: pv-name
spec:
  capacity:
    storage: 5Gi
```
### Where does the storage come from?

- Local Disk
- cloud-storage
- nfs server

example nfs:
```yaml
kind: PersistentVolume
metadata:
  name: pv-name
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  storageClassName: slow
  mountOptions:
    - hard
    - nfsvers=4.0
  nfs:
    path: /dir/path/on/nfs/server
    server: nfs-server-ip-address
```

example nfs

```yaml
kind: PersistentVolume
metadata:
  name: pv-name
  labels: 
    failure-domain.beta.kubernetes.io/zone: us-central1-a__us-central1-b
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  gcePersistentDisk:
    pdName: my-data-disk
    fsType: ext4
```

example local

```yaml
apiVersion: vl
kind: PersistentVolume
metadata:
  name: example-pv
spec:
  capacity:
    storage: 100Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Delete 
  storageClassName: local-storage local
  path: /mnt/disks/ssd1 
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname 
        operator: In 
        values: 
        - example-node
```

### NOT namespaced

Persistent volumes are `NOT NAMESPACED` which means they're available to the whole cluster
Q: Do I have access to do that shit?

- Local Volume Type: 
Local volume type is `NOT TIED TO 1 SPECIFIC NODE`.
Local volume type `DOES NOT SURVIVE CLUSTER CRASHES`.
- Remote Storage Type
can survive cluster crashes


