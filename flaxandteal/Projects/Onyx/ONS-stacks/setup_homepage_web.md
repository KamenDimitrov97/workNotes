# To setup only the homepage locally using docker-compose 

1. clone repo dp-compose - https://github.com/ONSdigital/dp-compose/tree/main
    1. check inside v2/stacks/homepage-web to see which repos you need to run the homepage
    2. clone them 
2. once you have them all, you need:
    1. zebedee data - you need the zebedee contents which I have and you need to place them in the right dirs
    2. setup the data
    3. zebedee_root var exported in your environment - `export zebedee_root=full/path/to/zebedee-cms`
3. go back to v2/stacks/homepage-web and `make start-detached`
## possible issues:
    - dp-frontend-homepage-controller can't find go-bindata binary. Go is not added to the path
    so in order to fix this make sure you're calling bindata in the makefile this way: ../.go/path/bin/go-bindata as this is used in the docker container

# To setup the rest of the pages

1. inside dp-compose/v2/stacks/homepage-web/core-ons.yml add:
    - babbage - which generates the rest of the htmls
    - renderer - which renders error msgs if you get any
2. in /babbage run `make build` so that folder `./target/dependency` is created as it is used in building the docker container

## Things to add:
core-ons.yml
```yaml
  babbage:
    extends: 
      file: ${PATH_MANIFESTS}/core-ons/babbage.yml
      service: babbage
  dp-frontend-renderer:
    extends:
      file: ${PATH_MANIFESTS}/core-ons/dp-frontend-renderer.yml
      service: dp-frontend-renderer
```

## possible issues:

dp-frontend-homepage-controller has an endless log and is calling zebedee on endpoint `v1/data` which doesn't exist:

zebedee is also having an endless log:

checking that out - So basically 2 more apis should  be added to thhe stack to make it work and those are - babbage  and dp-frontend-renderer