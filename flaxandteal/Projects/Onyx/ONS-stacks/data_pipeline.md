# Reindexing data pipeline and how it works

# Florance 

The publishing platform used for the ONS website. It is used to create/update/delete datasets.

DEP:
    Preview: Babbage
    API: Zebedee CMS
    Preview: Sixteens
    Publishing: The Train
    Dataset upload: Import API
    Dataset upload: Recipes API

## Babbage 

Babbage is a bespoke service for translating JSON into HTML. The Zebedee-Reader reads .json files off the server for passing to Babbage. Babbage then translates them into the .html files that are used in the website.

It creates the HTML files for the pages on the website.
It creates the HTML files for the website publications in the publishing system Florence

## Zebedee 

Zebedee is the CMS used by the ONS website and the internal website publishing system. It is a JSON API and does not have a user interface. 

CMS - content management system 

it basically handles storage, creating datasets, most likely handles user roles and permissions, publishing and versioning.

there's 2 zebedees you can run:
zebedee-reader - Zebedee-reader is read-only. It's used by Babbage (the public facing web frontend of the ONS website) it returns the published site content as JSON.
zebedee-cms - THis is the one we want to run as it actually handles the creation/editing of data this is what's being hit when a reindexing is being called 
it's a json local file storage with a specific directory hierarchy 
it's not a database and is not backup by one aswell 

## Sixteen 

this is where the styling of the publishing tool and the website is being handled, not important to the reindexing pipeline

Florance readme is a bit unclear or why this is linked with publishing 

## dp-import-api

import api creates import datasets 

## dp-recipies-api

creates recipies on how datasets looks like basically a blueprint for a dataset and it's called a recipe 

is this something we should take into account since we're going to enrich existing datasets is this a blocker?
prolly not 


# search data extractor

So search data extractor listen for kafka messages that indicate a change to the datasets, which can be triggered from florance (basically the entrypoint)
could be simulated with a regular kafka msg and has testing msgs 

Kafka msgs have URIs that the service consumes and either:

requires kafka obviously


<!-- Category has a problem with the s3 credentials and Linden assumes it's on our side Phil's gonna check and get back to Linden


They're still exploring these 3:

adding more work
spreading the work 
extending the dates  -->

