I started setting up zebedee as that's something that's needed by florance and data-extractor 

To setup zebedee you need: 
1. setup zebedee-content
    1. clone zebedee-content
    1. make install
    1. copy csm-content.zip as a zip into zebedee repo root dir
    1. then run dp-zebedee-content generate -c=~/path_where_you_want_the_content_to_be_generated
1. setup maven and jave 8 jdk
1. setup dataset-api
    1. setup mongodb and neo4j
    1. configure neo4j (if ubuntu conf file is here: /etc/neo4j/neo4j.conf) with  `dbms.security.auth_enabled=false`
    1. setup dp-auth-api-stub
        1. dropped it for now
1. I ran into errors regarding missing env variables called:

```shell
export zebedee_root="zebedee-cms/src/main/java/com/github/onsdigital/zebedee"   
export content_dir="/content"
```
    1. then a missing auth token > I disabled the authentication feature as it was available to do so 
    and I already got testing content I don't see why I need authentication 





decided to drop setting it up locally until they agree that we're gonna work on them 
as for now I'm to run the homepage-publishing stack by downloading all the repos and running it in docker 

repos besides the ones I already had 
The-train   -------  make sure you build the jar before you run the stack from dp-compose
dp-topic-api
dp-router-api
dp-image-api
dp-design-api
sixteens
dp-image-importer
dp-frontend-homepage-controller
dp-frontend-router

Linden meeting notes:
Most important thing is that you need:
 a root variable called zebedee_root="full/path/to/zebedee-cms/zebedee"
setup the whole stack, there's a step by step guide 
https://github.com/ONSdigital/dp-compose/tree/main/v2/stacks/search

and this works I managed to set it up and start up florence with the whole stack running 
only issue is that the create/update dataset feature(the one we needed ) is broken and doesn't work 

investigating 
