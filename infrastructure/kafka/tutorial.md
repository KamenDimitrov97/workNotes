I pulled this img `docker pull confluentinc/cp-kafka`

```shell
docker pull confluentinc/cp-kafka
docker run --name kafka -p 9092:9092 --env ADVERTISED_HOST=localhost --env ADVERTISED_PORT=9092 --env confluentinc/cp-kafka
```

got err

```shell
===> User
uid=1000(appuser) gid=1000(appuser) groups=1000(appuser)
===> Configuring ...
Running in Zookeeper mode...
KAFKA_ZOOKEEPER_CONNECT is required.
Command [/usr/local/bin/dub ensure KAFKA_ZOOKEEPER_CONNECT] FAILED !
```

This is most likely because I'm missing zookeeper 

added zookeper on http://localhost:2181/ but got new error 

KAFKA_ZOOKEEPER_CONNECT=http://http://localhost:2181

```shell
docker run --name kafka -p 9092:9092 --env ADVERTISED_HOST=localhost --env ADVERTISED_PORT=9092 --env KAFKA_ZOOKEEPER_CONNECT=http://http://localhost:2181 confluentinc/cp-kafka
```

KAFKA_ADVERTISED_LISTENERS missing 

```shell
===> User
uid=1000(appuser) gid=1000(appuser) groups=1000(appuser)
===> Configuring ...
Running in Zookeeper mode...
KAFKA_ADVERTISED_LISTENERS is required.
Command [/usr/local/bin/dub ensure KAFKA_ADVERTISED_LISTENERS] FAILED !
```

```shell
docker run --name kafka -p 9092:9092 --env ADVERTISED_HOST=localhost --env ADVERTISED_PORT=9092 --env KAFKA_ZOOKEEPER_CONNECT=http://127.0.0.1:2181 --env KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 confluentinc/cp-kafka
```


docker run --name kafka \
    -p 9092:9092 \
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
    -e KAFKA_BROKER_ID=1 \
    -e KAFKA_CREATE_TOPICS=my_topic:1:1 \
    -e KAFKA_AUTO_CREATE_TOPICS_ENABLE=false \
    -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
    confluentinc/cp-kafka

*******************************************************
screw that
*******************************************************

```shell
tar -xzf kafka_2.13-3.5.0.tgz
cd kafka_2.13-3.5.0
```

```shell
# Start the ZooKeeper service
bin/zookeeper-server-start.sh config/zookeeper.properties
```

Open another terminal session and run:

```shell
# Start the Kafka broker service
bin/kafka-server-start.sh config/server.properties
```


creating a topic 

```shell
bin/kafka-topics.sh --create --topic testing-producer-consumer --bootstrap-server localhost:9092
```

describe topic 

```shell
bin/kafka-topics.sh --describe --topic testing-producer-consumer --bootstrap-server localhost:9092
```

listing topics 

```shell
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```

writing events to a topic 

```shell
bin/kafka-console-producer.sh --topic testing-producer-consumer --bootstrap-server localhost:9092
```

consuming events from a topic 

```shell
bin/kafka-console-consumer.sh --topic testing-producer-consumer --from-beginning --bootstrap-server localhost:9092
```

kubectl create rolebinding my-release-kafka:psp:trusted --clusterrole=psp:trusted --namespace fat-ony-dev --serviceaccount=fat-ony-dev:my-release-kafka


--direction=load --input=prod --output=http://localhost:9200 --ignoreChildError=true --includeType=settings,mapping,alias,analyzer,data