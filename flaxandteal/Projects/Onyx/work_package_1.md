# Work Package 2

1. Extending the import pipelines to include new area profile data to be indexed into Elasticsearch
 - Search, import data and reindex elasticsearch
 - The ability to store and update semantic location information, ready for querying by ONS (search) API
 - The ability to reindex area profile data when reindexing all other data and content
 - Enable callback feature, so development teams can trigger data updates to their content or data without reworking the existing data pipelines
 - Improving geo-location search 
 - ○ Area search and geo-tagging - users should be able to search with postcodes, geographical codes, and place names

## Possible questions: 
1. Enable callback feature, so development teams can trigger data updates to their content or data without reworking the existing data pipelines.
    - Should this be a separate API or just a separate endpoint to search-api? 
2. Area search and geo-tagging - users should be able to search with postcodes, geographical codes, and place names
    - What standard should we use for geographical codes - ISO 3166-1, FIPS, NUTS or maybe multiple?
    - Should the post codes be UK standards only?
    - example post-codes: BT9 5AB, BT1 1AA
3. The ability to store and update semantic location information, ready for querying by ONS (search) API
    - what is semantic location information?
    A: Semantic location information refers to data that describes the meaning or context of a particular location. It goes beyond just the physical coordinates of a place and includes additional information that helps to identify and describe the place in a more meaningful way.
    - What information should be included? 





## Metting notes 

Pipelines from ONS sides were failing 
So ONSs concourse ci actually asks if the last commit is verified by github and then asks if the gpg key that it's verified by is inside ONSs keyring 
in order to trigger
Workaround is for linden to create a dummy commit after every merge on our side
but I could create a gpg key and send it to github and ONS?


I had a deployment meeting with Andy Chan.

* Linden finished the pipeline that's going to do the deploy on their testing sandbox
* The pipeline was failing. 
    - ONS concourse pipeline, before the checkout repo step, asks if the last commit that it's checking out is verified by github(first pic related),
    then asks if the the gpg related to the github verification is also inside their internal keyring, only if it does it continues with the CI/CD.
    - Someone removed Nathans gpg public key(which they shouldn't have) and now all of Nathans repos don't work.
    - Our repo's only commit in the master branch is Nathans. 
* Andy said he will try to dig around and see why Nathans gpg key was removed and try to re-add it and run the pipeline 
* He asked that if there's anythin specific for the scrubber he might need for the deployment ----- told him no (Phil can correct me if I'm wrong)
    - the data is bundled in the image.

     low scoring categfories 


demo requested to ONS possibly last week of july 


linden's off and due to the outage the previous week Andy is unable to help with berlin and category for now 


we need to get elasticsearch 7 indexing to our cluster tell Phil for next week 











QUERIES TO USE: 
unemployment - still irrelevant
conceptions
Mortality rates



Questions:

Should I keep the nlp/search endpoint as a testing endpoint or nah?
log in dp-search-api and add a debug toggle

Feature flag should be a query parameter or a config variable?
A: config variable

In order to test it using convey should I abstract this


dp-api-clients-go










queries:

1. co2 emissions in London
1. Suicide statistics for England and Wales
1. Registered voters in UK
1. buildings built in london 2021
1. GDP per capita
1. Average cost of living London 2021
1. Registered voters
1. Cost of living


err handling and testing 
we've made significant improvements to our systems by updating how errors are managed and testing all our APIs. This means we've strengthened how our software handles issues and made sure that all the different parts of our systems are thoroughly checked to work smoothly.

rewriting scrubber
We recently rewrote the DP-Scrubber API in Go, ensuring strict adherence to your internal Go API policies. This involved reconstructing the API using the Go programming language while making certain it aligned with your established guidelines and standards for Go-based APIs. This approach ensured consistency and compliance within your development practices, resulting in a more uniform and maintainable codebase for our DP-Scrubber API."


We enhanced the search capabilities of the DP-Search-API by implementing more advanced query functionalities for Elasticsearch, including incorporating Facebook's wiki model. This involved leveraging the Facebook wiki model to improve the API's search capabilities, enabling more sophisticated query functionalities within your system.


We successfully deployed our APIs to the ONS internal environment. This involved the successful transfer and installation of our APIs into the ONS internal environment, allowing for their operation and utilization within that specific system. 


We effectively addressing and resolving the feedback provided by ONS regarding our APIs. This involved taking proactive measures to handle and rectify the issues and suggestions communicated


start
we're going to demonstrate how our NLP (Natural Language Processing) APIs can make a noticeable difference in the search experience. We'll compare search queries before and after activating our NLP APIs to show you how these tools can enhance the search results, making them more accurate and relevant.


Revolution
Our aim here isn't to completely overhaul the search engine or make it a hundred times better,x but rather to enhance it without disrupting the current search results. We aim to improve the search experience without causing a drastic shift in the way it operates. Our NLP APIs are meant to seamlessly complement the existing search functionality, adding more context and accuracy without significant disruptions

the aim is to fine-tune our solutions to act more as silent enhancers, quietly improving the performance without making drastic or disruptive changes. By adjusting the parameters effectively, we strive to make incremental improvements that seamlessly integrate into the existing system, enhancing its capabilities without causing significant upheaval.