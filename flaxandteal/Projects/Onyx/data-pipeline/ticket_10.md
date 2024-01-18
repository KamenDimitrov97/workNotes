# Search Reindex API - make request to Search API to swap alias on indexes

As a developer, I want the Reindex API to enforce index alias swap when the reindex job is
set to completed, so that the Search service automatically starts using the newly populated
search index
Extend Search Reindex API to send an authenticated request to the Search API on POST
/search/<search_index>/aliases/<alias_name> when the total_inserted_search_documents
is equal to the total_search_documents.
As part of request set the delete_current_aliased_index to true
Request:
1. Headers: Authorisation
1. Method: POST
1. Path: /search/<search_index from job>/aliases/ons
1. Query Parameters: ?delete_current_aliased_index=true
1. Body: N/A

On failure or success update job resource state with failed or completed respectively; (also
update respective timestamps).

# Possible tasks: 

1. Set the job to complete could use patch put /jobs/<job_id> 
1. Send POST request to attach alias name ons to Elasticsearch index created for
reindex job
1. On success or failure update job resource state to completed or failed and
timestamps have been updated

# Estimates:

Quick - 2d 
Full - 4d