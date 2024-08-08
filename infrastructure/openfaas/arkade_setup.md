# Setup arcade

```sh
kubectl port-forward svc/gateway -n openfaas 8080:8080
```

# Setup openfaas with arkade

arkade install openfaas --direct-functions

https://github.com/openfaas/workshop/blob/master/lab1b.md#run-on-gke-google-kubernetes-engine


# Authenticate
export OPENFAAS_URL="127.0.0.1:8080" # Populate as above

PASSWORD=$(kubectl get secret -n openfaas basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode; echo)
echo -n $PASSWORD | faas-cli login --username admin --password-stdin 127.0.0.1:8080
