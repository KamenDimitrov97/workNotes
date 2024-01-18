    Looks to be missing build_time as part of the response.
    Passing uptime to the healthcheck initialiser seems misleading to me given it's actually just the start time but not in UTC
    Is timestamp required? I couldn't see it on the spec
    From reading the code, it looks to me that you're returning time in seconds and not ms as per the spec.
    Specifically for the category-api - this will need a healthcheck on ES, there's one in Go here: https://github.com/ONSdigital/dp-elasticsearch/blob/main/client/elasticsearch/v710/healthcheck.go to have a look at. 


    Well start_time is when the service was started and uptime is how long has passed since it started 

    status	"OK"
    version	
        version	"0.1.0"
        language	"python"
        language_version	"3.9.16 (main, Mar 21 2023, 13:35:43) \n[GCC 11.3.0]"
    uptime	"6 m, 45 s"
    start_time	"2023-04-30T13:40:42.882671"
    checks	[]


    TRY SETTING UP THE CACHE FOR CATEGORY API 
    ALUN is off next week 
    2 weeks of july ROB 

    Remind Phil to tell hrisi to make a holiday calendar 

    Try presenting better next time Informed client is a happy client 

    Presentation is key 

    What is going to be moved around:
    in july we do more category parameter refinement 



the client is either created or enhanced by passing it by dp-net module and it's effectively gives a client width preconfigured headers
every request u do will contain the credentials .aws.credentials files
aws access key 
aws secret key 
aws sdk 
