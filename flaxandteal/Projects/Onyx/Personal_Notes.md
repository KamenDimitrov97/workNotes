Here are the notes from the Friday meeting, correct if I got anything wrong -
ConcourseCi  is how onyx does pipelines - https://concourse-ci.org/docs.html 
dp-concourse was mentioned I think for an example of ci pipelines in onyx repos but  I couldn't find it which means either I don't have access or I got something wrong there
docker images will be uploaded to docker-hub but Nathan will check they'll be public or not and who'll have access to those.

There needs to be a discussion for coding standards for python and rust - Nathan mentioned an internal discussion and for the rust maybe with Chris 
dp-standards - https://github.com/ONSdigital/dp-standards , is where the python/rust standards will be put in once discussed

A infrastructure feature flag to be implemented  to quickly change between the NLP and regular search in case of issues in prod
Also it was discussed to maybe have the feature flag in nlp-hub to easily switch-off certain functionalities which might break
That maybe a way to mitigate bugs/queries that bring bugs 

We discussed that the beta should be finished 4 months in so that we have the rest of time to polish the Beta
They're using AWS, and there are 3 environments - dev(sandbox), staging(automated) and production(manual)

Phil already started with building a concourse repo

Change concourse job to nomad job - manifest dp-config
Nomad will deploy the app 

Get cpu and memory metrics for apis from google analytics(maybe)

Image configuration - AWS S3 container registry 
Two ways were discussed - build the model in - where images will be larger 
and other option was - mounted volumes, statefulsets - which has potentional corruption 


7th March 
For Python standards: 
Poetry, flask, pipin 
Proceed with nlp-hub with the standards we discussed for Scrubber.

Gracie Lewis, Nathan, Rahul are leaving by the end of the month.Discovery packages with Gracie and Nathan next week. 

When in a meeting with Nathan ask for Linden!

Tokenisation 
https://www.petefreitag.com/cheatsheets/regex/character-classes/

separate scrubber in detection and matching 
add 1 override feature like a optional query sring for scrubber


Remove all errors that might get to the user 

So nathan is going to create a library that's going to use specific codes so that user readable error msgs are dealt with codes 

{
  "errors": [{
	"error": <code for specific/generic error>, // can leave this blank for now this is different error codes that could be left blank
	"message": <human readable message>, - generic msg that doesn't describe what the underline issue is only the generic issue
  }],
	"trace_id": <trace_id value from app>,
}


error logging should be handled top level

for linting check stuff in dp-hello-world-api

16th of March

api router proxy for auditing and security 

# 28th of March 2023  

Phil implemented concorse to the python apis 

Phil is starting to create an allowace 
if we introduce a version of the package that has vulnerability ci will give errors


feature/ci has link to concorse with all of the tests added 

Rob wants to have a catch-up meeting of where we are and what've done so far what we\]re siuppose to do next week 

# 29th of March 2023  

For our test infrastructure Phil's gonnaa point me 


march 30th 2023

A/B testing means testing on live

team A is publishing team
team B is the data team 
What's 
PMD - publish my data open data store swirl all the data 
ESS - uses pmd as data driven 
IDS - 

deadmans chest gitlab f&t repo

tsa 


on friday talk to Phil about when we're going to do the meeting with linden 
I suggested tuesday morning Linden say he's available between 10-13 







Manage the new people coming, they need to know their place


rob will  have some more info for the projcet on 23th of june 



Discuss with Lidnen 18 of july:
Clean up branches merge everything into the develop branches sync them up 
and then delete all the unnecessary branches

datasets 



ability to register a callback 
self-registration 

somehow dynamic reg of additional callbacks or automate some tagging may be superseeded by one of the ess stuff 

trying to identify potential geospatial location to datasets that're not already marked 

another service could come along and say 


external services are providing enrichment based on location in existing datasets

Linden thought we were creating our own datasets 

series of asks from miranda there was a discussion with nathan and miranda wherther or not continue living with 
move some but not all 

extending the data pipelines with enriched datasets 

our job: 
ability to register enrichment callbacks 

geography search one postcode search 

area search text based search of an area 


es efficient way of enriching datasets on reindex, that;s a prerequiset do create anything 

linden needs an intermidieat branch so that the tests run 




uvicorn in category - we already have a more modern async flask setup which requires uvicorn 
uvicorn is wrapper to gunicorn 
guunicorn in berlin 


weekly feedback 