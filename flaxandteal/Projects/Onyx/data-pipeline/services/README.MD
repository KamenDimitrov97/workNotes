# Data pipeline and how each of the services work

## dp-api-router

entrypoint to the data pipeline at /job endpoint which calls the next API 

## dp-search-reindex-api

Provides detail about search reindex jobs and enables creation of a new job and triggering the reindex of data for Search Service.
See [search service architecture docs here](https://github.com/ONSdigital/dp-search-api/tree/develop/architecture#search-service-architecture)

