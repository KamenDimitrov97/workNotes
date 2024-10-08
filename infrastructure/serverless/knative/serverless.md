# Creating a serverless function that uses knative

## Manually create a serverless function
Should I? 

## Using the Func CLI

### Installation

https://knative.dev/docs/functions/install-func/#installing-the-func-cli comprehensive guide on how to install func CLI

Essentially 
1. Download the binary 
2. Add it to your bin path `/usr/local/bin`
3. Test with `func version`

### Quickstart guide

1. `func create -c` - Interactively create a base project to move your project to.
- Pick a Path
- Pick a Language
- Pick a Template - most commonly HTTP
2. In handle.py/go/*, handle method
Insert your logic, 

3. `func build` - test your build
4. `func deploy` - builds and deploys
5. `func invoke` - tests the function in the cluster

### func.yaml

Should I delve deeper into what func yaml is for 

```yaml
specVersion: 0.36.0
name: retter-maroon
runtime: python
registry: registry.gitlab.com/flaxandteal/retter-maroon-automation-ii
image: registry.gitlab.com/flaxandteal/retter-maroon-automation-ii:latest
namespace: srv-mrn-fn
created: 2024-08-16T16:19:10.378011036+03:00
build:
  builder: pack
run:
  envs:
  - name: CASSANDRA_HOST
    value: '{{ secret:retter-cassandra-host:retter-cassandra-host }}'
  - name: CASSANDRA_PASSWORD
    value: '{{ secret:retter-cassandra-password:retter-cassandra-password }}'
deploy:
  namespace: srv-mrn-fn
  image: registry.gitlab.com/flaxandteal/retter-maroon-automation-ii@latest
  imagePullSecrets:
    - name: gitlab-registry
```