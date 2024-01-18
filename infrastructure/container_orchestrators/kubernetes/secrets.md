
## Description

Secrets in Kubernetes are used to securely store sensitive information, such as passwords, API keys, and certificates. 
They provide a way to separate sensitive data from application code and configuration. Secrets are stored in the Kubernetes cluster and can be mounted as files 
or environment variables in pods, ensuring that sensitive data remains protected and is not exposed directly in the application's code or configuration files.


## Secrets work by encoding the data to base64

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
data:
  key1: base64-encoded-value1
  key2: base64-encoded-value2
  key3: base64-encoded-value3
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
    - name: my-secret
      configmap:
        path: path/to/configmap
  containers:
    - name: elasticsearch-7-10-container
      image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
      ports:
        - containerPort: 9200
      env:
        - name: ENV_VAR
        valueFrom:
          secretKeyRef:
            name: my-secret
            key: key1
```


## Usefule cmds

```shell
onyx describe secret category-secrets
onyx get secret category-secrets -o jsonpath='{.data.CATEGORY_API_FIFU_FILE}' | base64 --decode
```
## QUESTIONS:

Q: If it's as easy as encoding a secret to base64, is it really secure? Can't I just copy the string and decode it?


