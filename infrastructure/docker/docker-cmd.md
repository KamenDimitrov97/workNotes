`docker inspect image | jq` 

`docker rm $(docker ps -l -q)`

```
alias dive="docker run -ti --rm  -v /var/run/docker.sock:/var/run/docker.sock wagoodman/dive"
dive nginx:1.20-alpine
```