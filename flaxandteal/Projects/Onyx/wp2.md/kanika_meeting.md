# 

so the data is separated in c code country pc code and pc 


new model that berlin has to use from now on 


area codes
parlimentries


exactly what's happening in berlin - how the models are being used and if you can add another model


use the new models to check each piece of content from the data importer if it contains a location 
if it does enrich it with locodes and country codes and shiet 

# Enriching ES datasets with area codes

Kanika has created more models that will be used in berlin to enrich the piece of content that comes from zebedee and dataset api.
Models containing different types of area codes for the different countries in the UK. 

So far we have decided that inside the pipeline after the formating of zebedee/dataset data and before the importing of the data into ES, we'll make a call to berlin, updated with the 2 new models.

The idea of the call is to enrich each piece of data with new locodes and area codes. 

Once that is complete we can update berlin to also be able to find the closest location to a given location.
So if there's no available articles for Blackpool it would find available articles for the closest location to Blackpool. 

Area profiles need to be made

# QA

1. Where is the locodes model being loaded from (s3?)? 
1. I'll most likely need access there if we need to upload the new models? Unless kanika manages to merge them all into one big model in which case I'll still need to upload that or you'll have to.

1. What happens to the postcodes functionality? - fck it it's on Phil
1. Are we making an Area api? - have a discussion with ONS to not have area profiles.. We're focusing on t he ESS stuff
1. Is the areas mmodel that kanika has created, replace the need for an area api or is it going to be used in area api?
1. As I keep reading searching by place name is optional and searching by postcodes is a requirement?
1. Who's the geography team? Are we the geography team? - explorer national statistics ask Rob, they're doing a project to markup data 

We discussed 15-18 weeks where I asked for 3 weeks of buffer zone for wp2, personally(we discussed this) I was hoping to work it out for 10-12 weeks so 6-8 weeks for wp2 
now I'm left with 10 weeks to work with - so 2-3w for the data pipeline and 7-8w for wp2 

geography tags from the geography team? 0 rob 
json schema example 
what's in  the datasets take a look how  it looks 

Aciton points:
talk to Linun priority data pipeline
re-estimate data pipeline 
reschedule with Phil to see new estimate 