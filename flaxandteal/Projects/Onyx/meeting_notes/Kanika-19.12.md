So what we sort of aggreed on with Kanika is this 

# What needs to happen

## Phase 1: Data enrichment
For enriching the pieces of content to be loaded to elasticsearch I'm going to call Berlin with a simple string query of a location - `co2 emissions in London`
which I will take from the title of the dataset to be loaded. The berlin call will be made in dp-search-data-importer.
if a location in the query exists I want the codes for that precise location to be returned - for example - give example - 
afterwhich I will enrich the datasets with the codes I've recieved.

### Questions on Phase 1:
How do we know it's the precise location if we don't have a country or something to pinpoint the exact location?
Should I search for locations in another field? Description, keywords maybe or something else? 
    - Should I ask ONS about this?
    - currently if you send a really long string to berlin with a location inside it it won't return the codes for that location.
What should we use for the location codes identifiers?
    - is this`"UN-LOCODE-ca:lod"` enough to differentiate between the locations? 
Can we add a new field to the dataset called `location` to the mappings for elasticsearch? 
    - or should the location be added to keywords? -kinda seems unlikely-
    - if not where should it be stored? 
I was thinking of calling Berlin in the handler where the data is being unmarshalled and sent to ES. My reasoning is that there will be no difference in the format of the dataset(dataset-api or zebedee)? 

### Overall AP: 
- Subject to change based on the answer to the questions 
1. Make a call to berlin to get precise location details - questions about that above
2. Store the locations in the datasets
3. Updated ES mapping (possibly?)
4. Load data into ES successfully


## Phase 2: User search by locations
Once a user searches for a query using a location `co2 emissions in Belfast` dp-search-api is going to call scrubber, berlin, category as per usual. 
Kanika will split berlin into 2 endpoints - 1st will be for phase 1 and the 2nd will be for phase 2. 
1st endpoint will give back only 1 precise location per query so I search for `co2 emissions in London` I get the codes for London - (question that arises from this is in the questions section of phase 1) 

2nd endpoint will give a `n` number of closest locations (e.g. 50) which we'll add to the search query to ES. E.g. 
`co2 emissions in London` but there is no article that matches that title and that location
we could use the should clause with an array of the 50 top closest locations and Painless scriptings to weigh the results correctly per sorted berlin response 


### Questions on Phase 2:
'Ow Da fuq is dis suppose to work?
Is 50 too much and what happens when the closest location exceeds the first 50? 
How do we pinpoint possible locations? 
How do we differentiate between category weighing and berlin weighing - category is obviously with higher priority(Painfull scripting?)

### Overall AP:
TO-DO - not sure this is suppose to happen

## Legend:
Pieces of content - data in the format of zebedee or datasets in their raw form before being formated and sent to ES
dataset - data already formated and ready to be stored in ES
ES mappings - a schema of what fields should the data of ES consist of 
Painless - language designed specifically for ES Scripting (pretty sure it won't be that painless)



Done? 

Dataset example: 
```json
      {
        "update":{
          "_id":"cphi01-timeseries"
        }
      }
      {
        "doc":{
          "type":"cantabular",
          "uri":"some_uri",
          "job_id":"",
          "search_index":"",
          "cdid":"",
          "dataset_id":"cphi01",
          "edition":"timeseries",
          "keywords":[],
          "meta_description":"",
          "summary":"",
          "title":"",
          "location":"london", // wanted to add this field
          "topics":[],
          "cancelled":false,
          "finalised":false,
          "published":false,
          "canonical_topic":"",
          "population_type": {
            "key": "pop-label",
            "agg_key": "pop-label###Pop Label",
            "name":  "popName",
            "label": "Pop Label"
          },
          "dimensions": [
 		        {
              "key": "label-1",
              "agg_key": "label-1###Label 1",
 		          "name":      "dim1,dim2",
 		          "label":     "Label 1",
              "raw_label": "Label 1 (10 categories),Label 1 (20 categories)"
 		        }
 		      ]
        },
        "doc_as_upsert":true
      }
```