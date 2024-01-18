# Requirements

```bash
export ELASTIC_SEARCH_URL=http://0.0.0.0:9200
export KAFKA_ADDR=0.0.0.0:9092,0.0.0.0:9093,0.0.0.0:9094
```

url - http://localhost:25900



# Interesting bits

sets a batchHandler of type `*handler.batchHandler`
which just has a 
```go
type BatchHandler struct {
	esClient dpelasticsearch.Client
	esURL    string
}
```

registers the batchHandler with the consumer which is a custome kafka consumer 

handler recieves a batch through kafka msgs 
```json
      {
        "UID":         "my-cantabular-dataset-my-edition",
        "Edition":     "my-edition",
        "DataType":    "dataset_landing_page",
        "SearchIndex": "ons",
        "DatasetID":   "my-cantabular-dataset",
        "Keywords":    [ "keyword1", "keyword2" ],
        "ReleaseDate": "releasedate",
        "Summary":     "description",
        "Title":       "title",
        "Topics":      [],
        "PopulationType": {
          "Key": "all-usual-residents-in-households",
          "AggKey": "all-usual-residents-in-households###All usual residents in households",
          "Name":  "UR_HH",
          "Label": "All usual residents in households"
        },
        "Dimensions": [
          { "Key": "label-3", "AggKey": "label-3###label 3", "Name": "dim3.0,dim3.1", "Label": "label 3", "RawLabel": "label 3 (33 categories),label 3 (40 categories)"}
        ]
      }
```


kafka-console-producer --broker-list 0.0.0.0:19092 --topic search-data-import

kafka-console-producer --broker-list 0.0.0.0:19092 --topic search-data-import < test-msgs.txt




{
  "uid": "example_uid",
  "uri": "example_uri",
  "edition": "example_edition",
  "data_type": "example_data_type",
  "job_id": "example_job_id",
  "search_index": "example_search_index",
  "cdid": "example_cdid",
  "dataset_id": "example_dataset_id",
  "keywords": ["keyword1", "keyword2"],
  "meta_description": "example_meta_description",
  "release_date": "example_release_date",
  "summary": "example_summary",
  "title": "example_title",
  "topics": ["topic1", "topic2"],
  "trace_id": "example_trace_id",
  "date_changes": [
    {
      "date": "example_date1",
      "change_type": "example_change_type1"
    },
    {
      "date": "example_date2",
      "change_type": "example_change_type2"
    }
  ],
  "cancelled": true,
  "finalised": false,
  "provisional_date": "example_provisional_date",
  "canonical_topic": "example_canonical_topic",
  "published": true,
  "language": "example_language",
  "survey": "example_survey",
  "population_type": {
    "type": "example_population_type",
    "details": "example_population_details"
  },
  "dimensions": [
    {
      "name": "example_dimension_name1",
      "value": "example_dimension_value1"
    },
    {
      "name": "example_dimension_name2",
      "value": "example_dimension_value2"
    }
  ]
}



```json
{
  "uid": "example_uid",
  "uri": "example_uri",
  "edition": "example_edition",
  "data_type": "example_data_type",
  "job_id": "example_job_id",
  "search_index": "example_search_index",
  "cdid": "example_cdid",
  "dataset_id": "example_dataset_id",
  "keywords": ["keyword1", "keyword2"],
  "meta_description": "example_meta_description",
  "release_date": "example_release_date",
  "summary": "example_summary",
  "title": "example_title",
  "topics": ["topic1", "topic2"],
  "trace_id": "example_trace_id",
  "date_changes": [
    {
      "date": "example_date1",
      "change_type": "example_change_type1"
    },
    {
      "date": "example_date2",
      "change_type": "example_change_type2"
    }
  ],
  "cancelled": true,
  "finalised": false,
  "provisional_date": "example_provisional_date",
  "canonical_topic": "example_canonical_topic",
  "published": true,
  "language": "example_language",
  "survey": "example_survey",
  "population_type": {
    "type": "example_population_type",
    "details": "example_population_details"
  },
  "dimensions": [
    {
      "name": "example_dimension_name1",
      "value": "example_dimension_value1"
    },
    {
      "name": "example_dimension_name2",
      "value": "example_dimension_value2"
    }
  ]
}
```