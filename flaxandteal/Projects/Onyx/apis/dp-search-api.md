Phil's implementation so far:

Gets 2 queries "q" and "c"
creates nlpCriteria and Settings
unmarshals nlpSettings which are a inside a env variable
gets nlpSettings as a query parameter from the url

so basically it takes the nlpSettings from either an
env variable or from the url as a query
then we go into AddNlpToSearch method
make a call to nlp hub 
get resp 
takes nlp criteria by looping through the categories 


why does it take the subdivision of only the first element from the response in

