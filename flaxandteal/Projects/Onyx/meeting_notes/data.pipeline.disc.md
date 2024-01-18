So we're doing the tasks that are detailed in trellow that will be the scope for the data pipeline 
Linden said we could finish what's already set as tasks and stories and if it doesn't work as expected we can re-evaluate 

as for timeframe 
Nothing written down, but Linden would say Rajul could do it in 2-3 sprints - there might be issues hiding underneath

Linden will help me a bit to get started 

do a service and ingress for Alana and hrisi to check stuff out 

1. Detailed tasks in trellow to be given to our team

2. Linden said we could finish what's already set as tasks and stories and if it doesn't work as expected we can re-evaluate

3. Linden suggested that Rajul(as a person intimately familiar with ons stuff ) could do it in 2-3 sprints 

4. Linden will be available for questions on the tickets 

5. I should do a service and ingress on dp-search-api or some frontend thing for Alana and Hrisi if testing is needed

6. Linden will send me the internal diagrams for the data pipeline how it worked and how it's suppose to work

7. There are 2 types of content being stored and used in the data pipeline 

    a. Zebedee content
    a. and datasets from dataset-api 

8. To be discussed: Where the extension of content through berlin will happen - possibilities are:
    a. Dataset/zebedee 
    b. search-data importer (which is where the formating of the data so that it could be bulk imported into ES is stored)

9. All apps/services exists nothing new to create

10. Trigger to ES data pipeline start from searchdatareindex api with an empty post request to /job endpoint

11. Rajul left off at Ticket №3 which is for reindex tracker api. It's suppose to keep track of jobs
    a. Only one job at a time - requirement

12. Create a new stack in dp-compose/v2/stacks/ I suggested publeshing-stack - Linden said he'll get back to me

13. I will work with forks as the nlp stuff

14. Phil suggested to make 2 assessments of how long it'll take: one for a fully completed polished work and a rougher version 

vue router mount to nginx router 
you can specify the endpoitns in the conf to be part of the query string 

search-data-extractor is being called when kafka msg is sent 
2 types of content 1 from zebedee 1 datasets from datasets api 

kafka msg reindex-requested search-data-finder which goes to zebedee or dataset api to collect the content 
generates the same exact format kafka msg to say upgrade this

checks if the datapipeline 

everything should be in docker-compose - best way to spin the whole thing is added in dp-compose as a stack 

think of a rough or lite version 
and a polished version 

ticket 4: 



Alun will give the tasks together