# Description 

1. api/ff_fasttext_api/scripts/ff_fasttext.py

The main function loads a FastText model from a file called 'test_data/wiki.en.fifu' using the load function. It then enters a loop where it prompts the user for input by printing "Sentence? " and waiting for the user to enter text. The user's input is stripped of whitespace and passed to the test method of the category_manager object, which returns a list of tuples containing a score and a list of categories. The categories are then formatted into a string with the score and printed to the console, with the top five results being shown.

poetry run uvicorn ff_fasttext_api.server:create_app --host 0.0.0.0 --port 3003

why wouldn't a separate api with the data not work - 
Effectively it's maintaining a separate api - extra work 

sort in an image that we attach to the first dockerimage

how to attach a separate image like volume to nomad  

build and scale the taxonomy and fifu to less gb 
https://stackoverflow.com/questions/51416510/cutting-down-the-size-of-a-fasttext-bin-file







changing the weightings to see if we can improve the search results 


do some tests on Phils implementation of the vars 


either we do it  live or cache the information somewhere 


load the cache in an s3 bucket and then download in the app at runtime



GET /ons1639492069322/_count [status:406 request:0.178s]

error 