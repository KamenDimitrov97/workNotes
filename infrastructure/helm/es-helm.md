# Installing es7 charts

helm install deprecatedes --version 6.4.2 elastic/elasticsearch

helm upgrade --install elasticsearch elastic/elasticsearch --version 7.7.0 --namespace namespace-name

helm install elasticsearch-deprecated elastic/elasticsearch -n fat-aub-fe-dev --version 6.4.2 \
  --set=installCRDs=true \
  --set=managedNamespaces='fat-aub-fe-dev' \

helm install my-elasticsearch elastic/elasticsearch --version 6.5.0 -n fat-aub-fe-dev

NODE_TLS_REJECT_UNAUTHORIZED=0 multielasticdump --direction=load --input=elasticsearch-dump --output=http://localhost:9200 --ignoreChildError=true --includeType=settings,mapping,alias,analyzer,data