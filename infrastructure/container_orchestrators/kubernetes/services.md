```yaml
apiVersion: v1
kind: Service
metadata:
  name: example-service
spec:
  selector:
    app: example-app  # This should match the labels in your Deployment
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: ClusterIP
```
or try cmd

```shell
aub expose deployment aubergine-website --port=8000 --target-port=8000 --name=aubergine-website-main --type=ClusterIP
```

onyx expose pod elasticsearch-master-0 --port=9200 --target-port=9200 --name=elasticsearch-master-0 --type=ClusterIP
