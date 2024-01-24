# handling multiple client errors:

Current way: If there's issues with adding checkers to hc then it'll only return the first thing that Errors.
This will not effect any errors that are returned from the checkers themselves only hc.AddCheckers() err.
Meaning all checkers errors will be displayed regardless of approach.

![currently](image-2.png)

I want to wrap each subsequent error using the helper function below

![proposal](image-1.png) 

the idea is to get all errors at once instead of fixing one error and waiting for the next

this is how it would look like 

if the AddCheck - which stops the whole service - returns an error:

![AddCheck Returns error adding all 3 checks](image-3.png)

if the Checkers return errors - which doesn't exit the service :

![Berlin checker](image-4.png)
![Scrubber checker](image-5.png)
![Category checker](image-6.png)