1. Change README.md if anything has changed with:
   - Usage of the API
   - Examples provided in the README
   - new dependencies added - most likely you can explain the updated http client in this section
2. Changes to the makefile
   - any new scripts added 
3. Swagger docs
   - any changes to the API functionality






make a hello-world heml-files 
install minikubes and stuff 
deploy a controller 
deploy a secret 
start from the simplest shit and go above



















DEPLOYMENT with phil and linden 
we pull bunch of meta data average word vectors for names 
word vectors per taxonomy item - that's a startup

we should cache that - if we could pull this into cached jsons data small enough to fit in a docker image or a config map
or we can pull it on start from mount cps volume or an s3 bucket 

if you had half a dozen config files where would you store it ?

- they certainly use s3 buckets so that's okay 
- linden will call a collaegue 


how often will the data be updated 
they wouldn't need to be updated between runs 
in a perfect world the category apy vector waiting nlp would reflect the current status what's in es it's a bit optimistic 
it should be static for container that's running 

category:
option 1: caching database like redis - we could have an endpoint for triggering a recache would need access to elasticsearch

option: 2: static set of config files that's gonna 

berlin: 

1 change the format of the input data - from very raw data (currently) to json structure 
and to extend it to weighted relationships like for example london 



category api is generating a model(config ) which is large and needs to be stored somewhere 5gb


phil was suggesting:

subsample version for testing currently

reading progressively - finalfusion libraries - in terms of a memory footprint it shouldn't be bad 
initially for checking it works it'll read it from disk 
we can cap the memory usage 

how are you dealing with the file storage in kubectl
for the moment we just got in the container just to get it tested 
or pull the model from min.io or a persistant volume 

our version of nomad is a beta version of nomad - very out of datee 

andy chan 


moving data to static removes the dependency to elasticsearch

using cachingdatabase - redis or something


category has a dependency - 1st version would be good to have static data for first live version we don't need live connection to ES but we'll need to build the data staticaly 

berlin also has some static files - location data but it's not huge 




linden suggests using redis recaching thing 



we're going with static files for the first iteration