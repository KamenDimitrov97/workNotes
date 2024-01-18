
LAST DEPLOYED: Mon Oct 9 15:57:30 2023
NAMESPACE: fat-ony-dev
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: kafka
CHART VERSION: 25.3.1
APP VERSION: 3.5.1


Kafka can be accessed by consumers via port 9092 on the following DNS name from within your cluster:

```shell
my-release-kafka.fat-ony-dev.svc.cluster.local
```

Each Kafka broker can be accessed by producers via port 9092 on the following DNS name(s) from within your cluster:

```shell
my-release-kafka-controller-0.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092 my-release-kafka-controller-2.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092
my-release-kafka-controller-1.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092
```
The CLIENT listener for Kafka client connections from within your cluster have been configured with the following security settings: - SASL authentication
To connect a client to your Kafka, you need to create the 'client.properties' configuration files with the content below:

```shell
security.protocol=SASL_PLAINTEXT
sasl.mechanism-SCRAM-SHA-256
sasl.jaas.config=org.apache.kafka.common.security.scram. ScramLoginModule required \
username="user1" \
password="$(kubectl get secret my-release-kafka-user-passwords --namespace fat-ony-dev -o jsonpath='{.data.client-passwords}' | base64 -d | cut -d, -f 1)";
```

To create a pod that you can use as a Kafka client run the following commands:

```shell
kubectl run my-release-kafka-client --restart='Never' --image docker.io/bitnami/kafka:3.5.1-debian-11-r71 --namespace fat-ony-dev --command -- sleep infinity 
kubectl cp --namespace fat-ony-dev client.properties my-release-kafka-client:/tmp/client.properties
kubectl exec --tty -i my-release-kafka-client --namespace fat-ony-dev -- bash
```

PRODUCER:

```shell
kafka-console-producer.sh \
--producer.config /tmp/client.properties \
--broker-list my-release-kafka-controller-0.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092, my-release-kafka-controller-1.my-release-kafka-controller-headless.cluster.local:9092, my-release-kafka-controller-2.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092 \
--topic test
```

CONSUMER:

```shell
--topic test
kafka-console-consumer.sh \
--consumer.config /tmp/client.properties \
--bootstrap-server my-release-kafka.fat-ony-dev.svc.cluster.local:9092 \ --topic test
--from-beginning
```



elasticdump \
  --input=prod/2023-10-09-analyzer.json \
  --output=http://localhost:11200/ons1695968532644141 \
  --type=analyzer

elasticdump \
  --input=prod/2023-10-09-mapping.json \
  --output=http://localhost:11200/ons1695968532644141 \
  --type=mapping

elasticdump \
  --input=prod/2023-10-09-data.json \
  --output=http://localhost:11200/ons1695968532644141 \
  --limit=1000 \
  --type=data