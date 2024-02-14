# Variables needing to be set

```bash
# export KAFKA_ADDR=http://localhost:9092,http://localhost:9093,http://localhost:9094
export ELASTIC_SEARCH_URL=http://localhost:9200
export KAFKA_ADDR=0.0.0.0:9092,0.0.0.0:9093,0.0.0.0:9094
export MONGODB_BIND_ADDR=0.0.0.0:27017
export SERVICE_AUTH_TOKEN=e19e7f47d1ec5347b7e8bb7b8b9e86379269fa82fa0b1cdf87e7b4bf834a2dca
export ROOT_SEARCH_API=/home/kamen/dev/work/github/onyx/dp-search-api # dp-search-api dir if it's not it the same dir as dp-compose
export SEARCH_API_URL=http://localhost:23900
export ZEBEDEE_URL=http://localhost:8082
export zebedee_root="~/dev/work/github/es-pipeline/es/es-pipeline/zebedee/zebedee-cms"
```

# Kafka

## Produce messages
onyx run kafka-producer -ti --image=bitnami/kafka:latest --rm=true --command -- kafka-console-producer.sh --broker-list my-release-kafka:9092 --topic testing-topic

## Consume messages
onyx run kafka-consumer -ti --image=bitnami/kafka:latest --rm=true --command -- kafka-console-consumer.sh --bootstrap-server my-release-kafka:9092 --topic testing-topic --from-beginning


docker cp /home/stroming/notes/flaxandteal/Projects/Onyx/data-pipeline/services/test-msgs.txt search_kafka-2_1:/bin/test-msgs.txt 


kafka-console-producer.sh --broker-list my-release-kafka:9092 --topic test-topic --producer-property security.protocol=PLAINTEXT
kafka-console-producer --broker-list 0.0.0.0:19092 --topic search-data-import --producer-property security.protocol=PLAINTEXT

helm upgrade my-release bitnami/kafka --set security.enabled=false -n fat-ony-dev

LAST DEPLOYED: Fri Dec  8 12:46:33 2023
NAMESPACE: fat-ony-dev
STATUS: deployed
REVISION: 2
TEST SUITE: None
NOTES:
CHART NAME: kafka
CHART VERSION: 26.4.3
APP VERSION: 3.6.0

** Please be patient while the chart is being deployed **

Kafka can be accessed by consumers via port 9092 on the following DNS name from within your cluster:

    my-release-kafka.fat-ony-dev.svc.cluster.local

Each Kafka broker can be accessed by producers via port 9092 on the following DNS name(s) from within your cluster:

    my-release-kafka-controller-0.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092
    my-release-kafka-controller-1.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092
    my-release-kafka-controller-2.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092

The CLIENT listener for Kafka client connections from within your cluster have been configured with the following security settings:
    - SASL authentication

To connect a client to your Kafka, you need to create the 'client.properties' configuration files with the content below:

security.protocol=SASL_PLAINTEXT
sasl.mechanism=SCRAM-SHA-256
sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required \
    username="user1" \
    password="$(kubectl get secret my-release-kafka-user-passwords --namespace fat-ony-dev -o jsonpath='{.data.client-passwords}' | base64 -d | cut -d , -f 1)";

To create a pod that you can use as a Kafka client run the following commands:

    kubectl run my-release-kafka-client --restart='Never' --image docker.io/bitnami/kafka:3.6.0-debian-11-r2 --namespace fat-ony-dev --command -- sleep infinity
    kubectl cp --namespace fat-ony-dev /path/to/client.properties my-release-kafka-client:/tmp/client.properties
    kubectl exec --tty -i my-release-kafka-client --namespace fat-ony-dev -- bash

    PRODUCER:
        kafka-console-producer.sh \
            --producer.config /tmp/client.properties \
            --broker-list my-release-kafka-controller-0.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092,my-release-kafka-controller-1.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092,my-release-kafka-controller-2.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092 \
            --topic test

    CONSUMER:
        kafka-console-consumer.sh \
            --consumer.config /tmp/client.properties \
            --bootstrap-server my-release-kafka.fat-ony-dev.svc.cluster.local:9092 \
            --topic test \
            --from-beginning




I created a client.properties file with the shit above

then I ran this:
```bash
kubectl run my-release-kafka-client --restart='Never' --image docker.io/bitnami/kafka:3.6.0-debian-11-r2 --namespace fat-ony-dev --command -- sleep infinity
kubectl cp --namespace fat-ony-dev client.properties my-release-kafka-client:/tmp/client.properties
kubectl exec --tty -i my-release-kafka-client --namespace fat-ony-dev -- bash
```



inside the pod I tried this:

```bash
kafka-console-producer.sh \
    --producer.config /tmp/client.properties \
    --broker-list my-release-kafka-controller-0.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092,my-release-kafka-controller-1.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092,my-release-kafka-controller-2.my-release-kafka-controller-headless.fat-ony-dev.svc.cluster.local:9092 \
    --topic test
```


```bash
kafka-console-consumer.sh \
    --consumer.config /tmp/client.properties \
    --bootstrap-server my-release-kafka.fat-ony-dev.svc.cluster.local:9092 \
    --topic test \
    --from-beginning
```


It works 
and services need to connect to the brockers not the client pod client pod is used for testing purposes mainyl I think


diFFERENT kafka brocker pods are used for different security protocols 9092 - is plaintext no bulshit

```bash
port-forward the brockers
onyx port-forward my-release-kafka-0 9091:9092
onyx port-forward my-release-kafka-1 9092:9092
onyx port-forward my-release-kafka-2 9093:9092
```












As a developer I want to call Berlin and get area data in the format of area codes and locodes about a specific locaiton.



API testing ?


kafka-console-producer --broker-list 0.0.0.0:19092 --topic search-data-import --producer-property security.protocol=PLAINTEXT

kafka-console-producer --broker-list 0.0.0.0:19092 --topic search-data-import --property value.serializer=io.confluent.kafka.serializers.KafkaAvroSerializer < ton.avro


kafka-console-consumer \
  --bootstrap-server <kafka-broker> \
  --topic <your-topic> \
  --from-beginning \
  --property print.key=true \
  --property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer \
  --property value.deserializer=io.confluent.kafka.serializers.KafkaAvroDeserializer \
  


  kafka-console-producer \
  --broker-list 0.0.0.0:19092 \
  --topic search-data-import \
  --property parse.key=true \
  --property key.schema='{
  "type": "record",
  "name": "search-data-import",
  "fields": [
    {"name": "uid", "type": "string", "default": ""},
    {"name": "uri", "type": "string", "default": ""},
    {"name": "data_type", "type": "string", "default": ""},
    {"name": "job_id", "type": "string", "default": ""},
    {"name": "search_index", "type": "string", "default": ""},
    {"name": "cdid", "type": "string", "default": ""},
    {"name": "dataset_id", "type": "string", "default": ""},
    {"name": "edition", "type": "string", "default": ""},
    {"name": "keywords", "type": {"type":"array","items":"string"}},
    {"name": "meta_description", "type": "string", "default": ""},
    {"name": "release_date", "type": "string", "default": ""},
    {"name": "summary", "type": "string", "default": ""},
    {"name": "title", "type": "string", "default": ""},
    {"name": "topics", "type": {"type":"array","items":"string"}},
    {"name": "trace_id", "type": "string", "default": ""},
    {"name": "cancelled", "type": "boolean", "default": false},
    {"name": "finalised", "type": "boolean", "default": false},
    {"name": "published", "type": "boolean", "default": false},
    {"name": "language", "type": "string", "default": ""},
    {"name": "survey",   "type": "string", "default": ""},
    {"name": "canonical_topic",   "type": "string", "default": ""},
    {"name": "date_changes", "type": {"type":"array","items":{
      "name": "ReleaseDateDetails",
      "type" : "record",
      "fields" : [
        {"name": "change_notice", "type": "string", "default": ""},
        {"name": "previous_date", "type": "string", "default": ""}
      ]
    }}},
    {"name": "provisional_date", "type": "string", "default": ""},
    {"name": "dimensions", "type": {"type": "array", "items": {
      "name": "Dimension",
      "type" : "record",
      "fields": [
        { "name": "key", "type": "string", "default": "" },
        { "name": "agg_key", "type": "string", "default": "" },
        { "name": "name", "type": "string", "default": "" },
        { "name": "label", "type": "string", "default": "" },
        { "name": "raw_label", "type": "string", "default": "" }
      ]
    }}},
    {"name": "population_type", "type": {
      "name": "PopulationType", "type": "record", "fields": [
        { "name": "key", "type": "string", "default": "" },
        { "name": "agg_key", "type": "string", "default": "" },
        { "name": "name", "type": "string", "default": ""},
        { "name": "label", "type": "string", "default": ""}
      ]
    }}
  ]
}' \
  --property key.separator=, \
  < ton.avro


