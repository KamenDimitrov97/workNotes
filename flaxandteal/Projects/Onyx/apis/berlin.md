berlin: 
berin data is publicly available data from open data sources some of it github repos and so-on 
the licenses of it are unclear what's compatable with ONS 
swame situation with taxonomy.js from category 




I had an issue building berlin image -- screenshot available
'HTTPResponse' object has no attribute 'strict'

That's the error I got once I get to the `RUN poetry install --no-dev` step

I could reproduce it locally by upgrading my poetry version to 1.2.1 and above (og was 1.1.12)
What I found was it's a dependency issue, maybe conflicting packages specifically requests and more 
specifically urllib3 or conflicting with the version of python being used in docker

poetry install stoped at package MarkupSafe, but I don't think the issue is with that package

googling told me to checkout pipdeptree where I saw urlib3 version differences so I change those 

So  I tried: 
I noticed that my local poetry was 1.1.12 and the docker one was 1.2.1:
so I decided to change the poetry version in docker
that didn't help.
Changing python version used in docker also didn't help
and when I changed urlib3 to 1.26 it worked

TL.DR.

I changed the dockerfile in berlin to get urllib3==1.26.12 and poetry==1.1.12
previous were 2.0.2 and 1.2.1



testing files what's the point of yield ?





Berlin
we can get extedend word vectors for the locations and do something similar to category for berlin (s3 bucket ?)
geospatial data into a word vector 



vectoring data
so the  idea is to convert all the geospatial data to vectors for the locations 
so that once we have the locations and distance of each location (from the core of the earth) there's an algorithm that will calculate the dot product of all locations and bring back the closest ones and bump the scoring of that location so that it's prioritized more 

that's one of 3 components 

