# Local setup

You could set it up by downloading the repo thhrough apt-get 
and installing es using `sudo apt-get install elasticsearch`
but I ran into architecture and permission issues I couldn't solve

so I just downloaded the archive

Pulled the image from es website and ran it 

# Loading the dump 

```shell
curl -s -XPOST localhost:9200/_bulk --data-binary @requests
```




backup stuff in case of hard disk issues
