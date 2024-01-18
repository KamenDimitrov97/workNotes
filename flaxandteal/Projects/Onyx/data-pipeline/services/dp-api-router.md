# How it works 

## main.go: 

General stuff:
1. creates error and signal channels  
1. gets configuration
1. creates and runs the service 

which leads us to: => 

## Service.go

1. creates service struct, with cfg and empty serviceList
1. creates a zebedee clienter
1. creates a kafka audit producer - which is just a kafka producer with a audit flag - true in the service list 
1. creates router: 
    1. gorilla muxer
    1. heavy usage of addTransitionalHandler which takes a - router, apiProxy and a url path
        1. which creates mux handler with a url using fmt.Sprintf something of the sort /v1/scrubber/ (if LegacyHandler without the v1) and a handler function called LegacyHandle or Handle(same file) which is basically just a handler func that calls the actual api with middleware before that
        1. What's an API PROXY: 
    1. creates a legacyHandler for topic api and all of it's endpoints
    1. creates a legacyHandler for codelist api and all of it's endpoints
    1. creates a legacyHandler for dataset api and all of it's endpoints
    1. creates a legacyHandler for filter api and all of it's endpoints
    1. creates a legacyHandler for filterFlex api and all of it's endpoints
    1. creates a legacyHandler for hierarchy api and all of it's endpoints
    1. creates a legacyHandler for search api and all of it's endpoints
    1. creates a legacyHandler for dimensionSearch api and all of it's endpoints
    1. creates a legacyHandler for image api and all of it's endpoints
    1. creates a legacyHandler for search api and all of it's endpoints
    1. creates a Handler for areas api and all of it's endpoints if EnableAreasAPI config is set to true
    1. creates a Handler for releaseCalendar api and all of it's endpoints if EnableReleaseCalendarAPI config is set to true
    1. creates a Handler for feedback api and all of it's endpoints if config for that api is set to true
    1. creates a legacyHandler for populationTypesAPI api and all of it's endpoints if config for that api is set to true
    1. creates a Handler for mapsProxy api and all of it's endpoints if config for that api is set to true
    1. creates a Handler for geodataAPIproxy api and all of it's endpoints if config for that api is set to true
    1. creates a legacyHandler for downloadService api and all of it's endpoints if config for that api is set to true
    1. creates a legacyHandler for filesAPI api and all of it's endpoints if config for that api is set to true
    1. creates a Handler for filesAPI api and all of it's endpoints if config for that api is set to true
    1. creates a Handler for filesAPI api and all of it's endpoints if config for that api is set to true
    1. creates a Handler for filesAPI api and all of it's endpoints if config for that api is set to true
    1. A lot of other apis aswell but the one we care the most about is: importAPI
    1. importAPI is created if EnablePrivateEndpoints is true so is: recipe, dataset, uploadServiceAPI using the LegacyHandler and searchReindexAPI using regular Handler

## Usage

Just run `make debug`


# dependencies to run 

For the data pipeline it requires jsut reindex_api 


# Must
I need to create the endpoint to call reindex_api

