Ask kanika to improve the algorithms of

python -m list

go run pip install for linden 



workflow diagram on what we need to get the 

internal api - one that's only takes internal requests 

everything into their staging how do we do it



Should discuss with Linden for api/search.go:30 error 204 instead of 500 why 

Should discuss with Linden for the error codes library

I'm not sure how I feel about storing this data in csv files - why was this approach selected? how often will this data change?

Prefixmap functionality 

This stripping of spaces seems slightly misleading - given your json files don't have spaces in, one could make the assumption that the response isn't supposed to either...but it is.

A: it was easier than trying to find which space was the difference between the two 


Ask rob if this feature was in scope but it wasn't 



unmarshal jsons into structs to see in steps/steps.go


won't be anyone monday to tuesday