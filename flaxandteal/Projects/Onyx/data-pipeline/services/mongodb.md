nabled=true --namespace fat-ony-dev
NAME: dp-mongodb
LAST DEPLOYED: Thu Dec  7 11:21:25 2023
NAMESPACE: fat-ony-dev
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: mongodb
CHART VERSION: 14.4.1
APP VERSION: 7.0.4

** Please be patient while the chart is being deployed **

MongoDB&reg; can be accessed on the following DNS name(s) and ports from within your cluster:

    dp-mongodb.fat-ony-dev.svc.cluster.local

To get the root password run:

    export MONGODB_ROOT_PASSWORD=$(kubectl get secret --namespace fat-ony-dev dp-mongodb -o jsonpath="{.data.mongodb-root-password}" | base64 -d)

To connect to your database, create a MongoDB&reg; client container:

    kubectl run --namespace fat-ony-dev dp-mongodb-client --rm --tty -i --restart='Never' --env="MONGODB_ROOT_PASSWORD=$MONGODB_ROOT_PASSWORD" --image docker.io/bitnami/mongodb:7.0.4-debian-11-r0 --command -- bash

Then, run the following command:
    mongosh admin --host "dp-mongodb" --authenticationDatabase admin -u $MONGODB_ROOT_USER -p $MONGODB_ROOT_PASSWORD

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace fat-ony-dev svc/dp-mongodb 27017:27017 &
    mongosh --host 127.0.0.1 --authenticationDatabase admin -p $MONGODB_ROOT_PASSWORD


manually changed the bindIp to 0.0.0.0 because I was getting MongoNetworkError: connect ECONNREFUSED 10.75.5.253:27017


helm install dp-mongodb \
    --set auth.rootPassword=admin,auth.username=admin,auth.password=admin,auth.database=sample \
    oci://registry-1.docker.io/bitnamicharts/mongodb \
    --namespace fat-ony-dev



    new test 


    --set auth.rootPassword=admin,auth.username=admin,auth.password=admin,auth.database=sample \
    oci://registry-1.docker.io/bitnamicharts/mongodb \
    --namespace fat-ony-dev
Pulled: registry-1.docker.io/bitnamicharts/mongodb:14.4.1
Digest: sha256:3218dc9168e8f5bb980b7755b777aed8e344a6ea855fdbd4d1a336254a250621
NAME: dp-mongodb
LAST DEPLOYED: Thu Dec  7 16:55:12 2023
NAMESPACE: fat-ony-dev
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: mongodb
CHART VERSION: 14.4.1
APP VERSION: 7.0.4

** Please be patient while the chart is being deployed **

MongoDB&reg; can be accessed on the following DNS name(s) and ports from within your cluster:

    dp-mongodb.fat-ony-dev.svc.cluster.local

To get the root password run:

    export MONGODB_ROOT_PASSWORD=$(kubectl get secret --namespace fat-ony-dev dp-mongodb -o jsonpath="{.data.mongodb-root-password}" | base64 -d)

To get the password for "admin" run:

    export MONGODB_PASSWORD=$(kubectl get secret --namespace fat-ony-dev dp-mongodb -o jsonpath="{.data.mongodb-passwords}" | base64 -d | awk -F',' '{print $1}')

To connect to your database, create a MongoDB&reg; client container:

    kubectl run --namespace fat-ony-dev dp-mongodb-client --rm --tty -i --restart='Never' --env="MONGODB_ROOT_PASSWORD=$MONGODB_ROOT_PASSWORD" --env="MONGODB_ROOT_USER=$MONGODB_ROOT_USER" --image docker.io/bitnami/mongodb:7.0.4-debian-11-r0 --command -- bash

Then, run the following command:
    mongosh admin --host "dp-mongodb" --authenticationDatabase admin -u $MONGODB_ROOT_USER -p $MONGODB_ROOT_PASSWORD

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace fat-ony-dev svc/dp-mongodb 27017:27017 &
    mongosh --host 127.0.0.1 --authenticationDatabase admin -p $MONGODB_ROOT_PASSWORD
