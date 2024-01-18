# Search Reindex Tracker - Consume search data imported events -- redacted

As a Developer, I want the search reindex tracker to consume events from
search-data-imported topic so that the tracker can update the job with the number of
documents imported into Elasticsearch index for particular job (via search reindex API)

The search reindex tracker will need to consume events from search-data-imported topic
and log the message and it's attributes that were consumed.

Acceptance Criteria
1. Consume message from search-data-imported 
1. Info log of message and attributes (to confirm message has been received) - 0.5d
1. Update healthcheck to include kafka consumer 1d
1. Update graceful shutdown to include consumer and consumer group closure 1d

# Questions:

1. Is this message only for logging purposes or is it suppose to trigger something in the tracker-api?

# Answer: 

So that we know when to switch the index

# Estimates:

Quick - 0.5d
Full - 3d
Full - 4.5d for pr reviews, merges, comments