# Search API - Include new endpoint to handle Index Alias swapping

As a developer, I want to be able to switch the ons alias from one search index to another
so that when a new index is populated the automated system can redirect backend requests
for ES data without any downtime.

Extend Search API with new POST /search/<index_name>/aliases/<alias_name> that can

take a query param delete_current_aliased_index=true
```json
    Method: POST
    Path: /search/<index_name>/aliases/<alias_name>
    Headers: Authorisation
    Query Params:
    delete_current_aliased_index = bool (true/false)
    Body: None
```

This endpoint is a private one, so request needs to be authorised, hence authorisation
header.

Acceptance Criteria

Create POST /search/<index_name>/alias endpoint
Handle query parameter
Update Swagger Spec
Extend Component Tests to cover new endpoint
Extend SDK client package

# Possible tasks:

1. Create a new POST endpoint - 1d
1. Handle query parameter
1. Update Logs and Swagger Spec - 0.5d  -- will add logs, won't add swagger docs
1. Update tests with new endpoint - 0.5d - no tests
1. Update SDK client package - 1d - no sdk update
 
# Questions:

What should the authorisation look like?
Redirect to a previous index I guess?

# Answers:

Service authentication - https://github.com/ONSdigital/dp-net/blob/main/request/identity.go

use 
```go
// AddServiceTokenHeader sets the given service token on the given request
func AddServiceTokenHeader(r *http.Request, serviceToken string) {
	if len(serviceToken) > 0 {
		r.Header.Add(AuthHeaderKey, BearerPrefix+serviceToken)
	}
}
```

SetServiceToken should be set to the serviceToken env var used in the above method for local testing purposes
SERVICE_AUTH_TOKEN - there's an extensive guide on how to set this locally,
first try to set this token to a random string and if there's an issue use this repo with Phil or Sharon

https://github.com/ONSdigital/dp-operations/blob/main/guides/generate-service-auth-token.md

# Estimates:

Quick - 3d 
Full - 5d 

check with Linden is there anything we might need to validate the authentication that we don't have and is it used anywhere in a separate service we can check -- maybe like certificates 

Validation authentication