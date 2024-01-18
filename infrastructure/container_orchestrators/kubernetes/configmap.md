
## Description

A ConfigMap in Kubernetes is a way to store configuration data that can be used by your application pods.
It's typically used to separate configuration from your application code, making it easier to manage and update settings without modifying the actual application container.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-configmap
data:
  key1: value1
  key2: value2
  key3: value3
```

you use it here

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: es7-10-pod
spec:
    // contains the 
  volumes:
    - name: my-configmap
      configmap:
        path: path/to/configmap
    - name: es7-10-pod-volume
      persistentVolumeClaim:
        claimName: elasticsearch-pvc-es7.10-pvc
  containers:
    - name: elasticsearch-7-10-container
      image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
      ports:
        - containerPort: 9200
      volumeMounts:
        - mountPath: "/usr/share/elasticsearch/data"
          name: es7-10-pod-volume
        - mountPath: /path/to/config-map.yml
          name: my-configmap
```
