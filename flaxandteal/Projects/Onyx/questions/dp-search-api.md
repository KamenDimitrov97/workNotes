Q: Why do they want a separate http client for each api I'm doing if the http client is going to be roughly the same?

Q: What does the SDK bring to the table if we're going to use a separate http client for each api anyway?



count - number of articles as a summery of the resulst 

https://github.com/ONSdigital/dp-frontend-search-controller/blob/develop/config/config.go


1. creates the client inside service.go run method `elasticHTTPClient := dphttp.NewClient()` dphttp is imported http repo
1. create dp-esclient which is located inside dp-elasticsearch repo our equivalent will be inside dp-search-api
1. creates a querybuilder you can use that to build your query later
1. Registers the handlers and gives them everything they might need like querybuilders transformers etc.
1. runs the server finally 

1. registers handler using everything initialized inside service.go/run()
1. in the handler it first get the url params and then uses CreateRequests()
1. which basically returns the query parameters needed and other ES specific stuff so you'll have to do your own




AP: Maybe build a query.Builder for the NLP first 


in service.go I'll create an NLP client and get the baseURLS for the apis 
pass the client to the handler and he'll do the requests 