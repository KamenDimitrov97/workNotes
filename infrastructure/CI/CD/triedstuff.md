1. Tried changing 

resources:
- name: dp-nlp-search-scrubber
  type: git
  webhook_token: ((webhook-token))
  source:
    repository: flaxandteal/onyx-dp-search-scrubber-api
    branch: ci-test
    access_token: ((github-access-token))

to without a timer

got an err: 
selected worker: srv-concourse-worker-0

fatal: repository '/tmp/git-resource-repo-cache' does not exist -- IDK but I assume it's got something to do with resources alocated for the pipeline

selected worker: srv-concourse-worker-1

invalid payload (missing repository)

so what I learned is that:
like in github actions there's a lot of community made resource types for concourse
the one ONS is using most likely for security reasons is pull-request because it allows you to use github tokens which are easier
the issue I've found is that I can't tell it what branch to listen to and I can't change the way it triggers a pipeline which is by a pull-request
right now it sees ci-test as the HEAD branch and develop as the one it's being push to because that's what I did 
I wonder if it'll go the other way around aswell ? (not 100% certain but I did try out a merge from ci to dev)

A: It works if you make a pull request the other way around 

I made a pull-request from ci-test to develop didn't work I'll try to merge it

i got missing inputs which is because it's requiring input in the ci yaml files in the scrubber repository itself


if you commit to an existing pull request it will not get those changes 
if you close and reopen the pr it will GET THOSE CHANGES