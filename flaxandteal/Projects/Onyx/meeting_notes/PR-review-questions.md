# 07.11 DP-API-CLIENTS-GO

Comment: perhaps it could say what it's querying for instead? It kind of is but in a roundabout way.
seems a bit noisy 

Q: Not sure what you mean though?

Comment: shouldn't you return nil to the first param if there is an error?

Q: Well you can return nil only on generic types - which is why I made it like that 
but now that you mentioned it it came to mind that I can convert model.Berlin to a pointer type and then I'll be able to return nil

not sure what would happen in dp-search-api would need to test it 



Comment:
Our normal pattern would be these are passed in to the client constructor - this could get a bit unwieldy and you could then split them down into separate clients for each api.

Not sure what Toggle and hub settings are doing here.

Q: maybe it would be easier for me if I knew the idea behind the abstraction here
my idea was that it could be reused and if someone wanted to reuse it he would need the settings at least
but yeah toggle and hub could be back in dp-search-api 
I was even thinking of writing a README but I didn't see anyone 

as for the 

