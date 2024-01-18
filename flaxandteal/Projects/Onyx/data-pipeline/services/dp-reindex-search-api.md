



## Usage

### Getting started

Run `make help` to see full list of make targets, otherwise read the following:

* Set up dependencies locally as follows:

In dp-compose repo run `docker-compose up -d` to run MongoDB on port 27017. 

NB. The above command will also run Site Wide ElasticSearch, on port 11200, which is required by the Search API.

Run `vault server -dev` (this is required by Zebedee)

In the zebedee repo run `./run.sh` to run Zebedee

In the dp-search-api repo set the ELASTIC_SEARCH_URL environment variable as follows (to use the Site Wide ElasticSearch):

`export ELASTIC_SEARCH_URL="http://localhost:11200"`

Also in the dp-search-api repo run `make debug`

Make sure that you have a valid local SERVICE_AUTH_TOKEN environment variable value;
if not then set one up by following these instructions: https://github.com/ONSdigital/zebedee

* Then in the dp-search-reindex-api repo run `make debug`

### Dependencies

* Requires MongoDB running on port 27017 
* Requires Kafka running on port 9092  
* Requires Zebedee running on port 8082
* Requires Search API running on port 23900  
* No further dependencies other than those defined in `go.mod`



# Questions: 

When the initialiser is empty like in main.go, where does it take the methods from?
A:  in initialise.go there's 2 receivers - externalservicelist and init-a so just ducking scroll down 
Q: Why does it try to find mongodb on 127.0.0.53:53 when the global variable is mongodb:27017? 

# Global Variables needed
```bash
export ELASTIC_SEARCH_URL=http://0.0.0.0:9200/
export MONGODB_BIND_ADDR=0.0.0.0:27017
export KAFKA_ADDR=0.0.0.0:9092,0.0.0.0:9093,0.0.0.0:9094
export SERVICE_AUTH_TOKEN=e19e7f47d1ec5347b7e8bb7b8b9e86379269fa82fa0b1cdf87e7b4bf834a2dca
export ROOT_SEARCH_API=~/dev/github/onyx/dp-search-api # dp-search-api dir if it's not it the same dir as dp-compose
export SEARCH_API_URL=0.0.0.0:23900
export ZEBEDEE_URL=0.0.0.0:8082
```

- these services need to run before reindex-api so make sure they 

```yaml
depends_on:
    - mongodb
    - kafka-1
    - kafka-2
    - kafka-3
    - dp-search-api
```