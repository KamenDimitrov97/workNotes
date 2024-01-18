# Update API Router to include search reindex API endpoints

As a developer, I want to be able to create a new reindex job, so that I can trigger a search
reindex

On publishing subnet only, so add to list of private endpoints in the API router the Search
Reindex Jobs endpoints

# Possible tasks: 

1. Update api router with POST /search-reindex-jobs endpoint 
1. Update search router with GET /search-reindex-jobs
1. Update tests for api-router 
1. Update docs for api-router

# Questions:

Is there some specific authorisation required as I noticed the AC quotes :"As a TL "

# Answer: 

Same thing as ticket 9

# Estimates:

Quick - 1d
Full - 2d