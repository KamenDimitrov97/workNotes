# Search Reindex Tracker - Update Job with number of documents imported to ES -- redacted

As a Developer, I want the search reindex tracker to update reindex job with the data
consumed from search-data-imported topic, so that the job information is up to date (and
future actions against job can happen)

When the search reindex tracker has consumed an event from search-data-imported topic,
instead of logging the event contents, make multiple calls to update the search reindex API
with the correct total_search_documents against a given reindex job
1. Make GET request to jobs/<job_id>
1. Use the current total_inserted_search_documents for reindex job and add to it the
total_search_documents from kafka event
1. Make a PATCH request to jobs/<job_id> to update the job with the following:
    1. total_inserted_search_documents - should add to this the
    1. total_search_documents from kafka message to the current value

For the Patch request use the ETag from previous GET request in an IF-Match header on
PATCH; if there is a conflict, try GET and PATCH again. Reason is to prevent race conditions
between updating the same resource multiple times and PATCH method is not idempotent.

Acceptance Criteria
1. Remove Info log of message and attributes (to confirm message has been received)
1. Update job information with the use of PATCH endpoint

# Questions:

# Tasks:

1. Make GET request to jobs/<job_id> 1d 
1. Make a PATCH request to jobs/<job_id> to update the job 1d 
1. Update automated testing 1d 
1. Update logs and docs 0.5d 

# Estimates :
Quick - 2d
Full - 3.5d

# Risks:

If those 2 endpoints don't exist then we can create example toy endpoints 