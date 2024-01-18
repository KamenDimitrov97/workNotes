# Setup

To setup zebedee you need: 
1. setup zebedee-content
    1. clone zebedee-content
    1. make install
    1. copy csm-content.zip as a zip into zebedee repo root dir
    1. then run dp-zebedee-content generate -c=~/path_where_you_want_the_content_to_be_generated
1. setup maven and jave 8 jdk
1. setup dataset-api
    1. setup mongodb and neo4j
    1. configure neo4j (if ubuntu conf file is here: /etc/neo4j/neo4j.conf) with  `dbms.security.auth_enabled=false`
    1. setup dp-auth-api-stub
        1. dropped it for now
1. I ran into errors regarding missing env variables called:

```shell
export zebedee_root="path/to/zebedee/zebedee-cms"   
```
    1. then a missing auth token > I disabled the authentication feature as it was available to do so 
    and I already got testing content I don't see why I need authentication 


You need to get `zebedee_content.zip` from either Phil, Kamen or Linden



## Notes 

zebedee must be a Java EE application as I see a lot of javax.servlet.http.HttpServlet extensions



nothing is created, might be just creating the templates, 