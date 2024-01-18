We had issues with where the publishing data was not showing up 
so we manually set the data as where it was on lindens machine 

so instead of setting up dp-zebedee-content 
just get the content from the content.zip file into zebedee-cms/master
afterwhich set zebedee_root to:
zebedee_root="/home/stroming/dev/github/onyx/es-pipeline/zebedee/zebedee-cms"

and it worked I'm still getting the florence bug but at least the data is available if hit zebedees
http://localhost:8082/publishedindex