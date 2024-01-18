# Search Data Importer - Write event to Search Data Imported Kafka Topic

As a developer, I want the Search Data Importer to send an event when a batch of
documents from a reindex job has been processed (sent to ES) so that downstream apps
(search reindex tracker) can take necessary action on this information.

The search data importer will need to produce an event to search-data-imported topic after a
reindex job batch has been successfully sent to ES

Acceptance Criteria
1. Produce message to search-data-imported
1. Message includes:
    1. job_id
    1. number_of_search_documents - this is the number of documents imported
1. Event Header to include trace_id (this should be equal to the batch_id)
1. Update healthcheck to include kafka producer
1. Update graceful shutdown to include producer closure


# Questions:

1. What's the message/event about?
    1. keep informing the tracker-api that there's a reindexing in process and when the final batch arrives to make sure the tracker-api knows it's the final batch?
    1. How should this message be consumed by the tracker-api
    1. Or is simply for logging purposes?

# Answers:
    Tracker has an expected count of documents, so this msg should let tracker keep track if the documents imported = docs expected. 
    If it doesn't match it should switch the index.
    Design at the moment is expecting those numbers to match reindexing failed if there's a mismatch between docs imported and docs expected.
    Do as is we can revisit this if there's an issue.

# Possible tasks:

1. Produce message to search-data-imported - not sure how much time kafka msgs take -
1. Update healthcheck to include kafka producer - 1d  -- ask for an example clarify who's the producer.
- prolly if kafka is available at url
1. Update graceful shutdown to include producer closure 1d

# Estimates:

Quick - 0.5d
Full - 2.5d
Full - 4d for pr reviews, merges, comments