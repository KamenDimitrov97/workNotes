# Fix errors seen in Search Data Extractor for Reindex Job

Search Data Importer throwing errors for reindex job; these need to be resolved so the
extracted data based on these urls can be sent to the search-data-import kafka topic
The trace id was overwriting the search index field, this will need to be corrected but I don't
think this is the issue with handling the urls.

Acceptance Criteria
1. Fix the errors in the Search data importer when we trigger a search reindex

# Questions:

Are the errors defined anywhere?
Are they logged as buggs somewhere?
I'll need to set the whole project to get an idea of how many errors and what's their debth before I can create tasks or estimate.

# Answers:

No logs, no comments will have do an investigation of what the errors are.

# Estimates:

I'm going to need 1 day to figure out what bugs I need to fix and add it to the estimates