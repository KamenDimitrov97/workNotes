# Search Data Importer - Each job_id should have it's own batch

As a Developer, I want the search data importer to handle multiple batches in parallel based
on the search search_index value consumed so that the batch sent to Elasticsearch is sent
to the correct index

The Search Data Importer should instantiate a new batch on consumption of a message if
there is not already a batch available for that search_index. This is so we can send batches
of data to the correct index.

Acceptance Criteria:
1. Search Data Importer creates a new batch object for processing if a batch doesn't
already exist for the search index provided by message consumed from
search-data-import
1. Things to continue happening:
    1. Every batch will be processed (e.g. sent to ES) once 500 documents are in
    batch or 5 seconds have passed since batch was created
    1. Batch IDs should be created for each batch and used in the logs


# Questions:

1. What's the definition of a batch? Does one job constitute multiple batches?
    1. I'd recieve kafka msg with the search_index value being the index this content receive from data-extractor should be sent to?
    1. Or is the batch just up to 500 pieces of data that's to be sent to ES7? 
2. Is the point of this to start multiple parallel batches so that the data is imported faster?
    1. So 500 pieces of content come in from either zebedee or dataset-api and every 500 pieces of content or 5 sec past need to be sent ES7 and start a new batch to sent to ES7 with the same idea?
3. Can ES take multiple bulk post requests of data simulataneously?
# Answers:

1. Issue is not running the on demand pipeline in the same time 

# Possible tasks:

1. Consume Kafka msg - 0.5 making sure it all works together and where it needs to happens
1. Create a batch object creator - needs to take a value, send a request to correct ES index - 3.5d 
1. Set batch creator to create a batch per 500 pieces of content or 5 sec past - parallel programming - 3d
1. log the batch start process and sent - 0.5d
1. Automated testing - 1.5d

# Estimates:

Quick - 7d
Full - 9d
Fully and deal with annoying issues that come up - tidying it up - 12d 


maybe do the testing in parallel with GoConvey BDD 



Hi Linden,
I've got a question about handling the batches in parallel based on the request index if you've got a minute to talk




As a Developer, I want the search data importer to handle multiple batches in parallel based
on the search search_index value consumed so that the batch sent to Elasticsearch is sent
to the correct index

Search-data-extractor produces single data msgs, I've made the consumer group(search-data-import) take in batches of 500 or 5s 
and I was wondering if it was possible for those single msgs to be on a different index 
for example 
reindexing pipeline is started - index ons1 while it's being process 
on demand pipeline is being started - index ons2 


Will dp-search-data-import get msgs of the sort 


data for ons1
data for ons1
data for ons1
data for ons2
data for ons2
data for ons1
data for ons1
data for ons2
