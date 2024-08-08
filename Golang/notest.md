# The go scheduler

How it works - 
P - representation of cpu , num of ps the scheduler has 
can have status current concurrent  current m  list of free goroutines 
M - the machine ) asscoiated Current goroutine  and current P  - may have some situations where it's not associated with the processors
Sched - has a list of idle Ms or Ps  list of global runnable goroutines, global of free 

G the goroutine - stack 2048 bytes program counter, status , current , wait reason, other metadata 



Life of the goroutine 
Runnable running syscall waiting preempted copystack

Runnable - > running - go routine is calling the scheduler ->  find a goroutine to run asign it to the M mark as Running executes the code 
if fnot it's go to the netpool - check if something is already done and use that goroutine, steal work from the other processors 

Running -> waiting - Park itself, detatch from M, Run the scheduler - wait reasons in the src code - summarize -> GC - garbage collector, mutex semaphore channel sleep I/O - why they wait for something

running to syscall and running to runable -> on every syscall entersyscall is executed moving to syscall state 
syscall is executed exitsyscall is execcuted mvoing back to running runable 

Running to copystack and back 
More stack needed 
change running to copystack grow the stack change back to running 

Waiting -> runnable 
goready is called is added to the queue try to get a P

Running to preemtp waiting to runnable 

preempt flag is set -> change to preempted next gc change to waiting do the gC scan change the runnable add it back to the queue 

pass data to channel -> 

wait group - >  spawnn 3 goroutines  -> the last one is going to call done to the waiti group and see if it's = 0 if so call ready to the scheduler

# death of a goroutine

Normaly dies when it finishes the work -nothing else to execute - most of the data to the daata 
disconnect the goroutine of the M 

check the scheduler 

check about Cgo gb 
illustrated tales of go runtime scheduler 

scheduling in GO 

# How to contribute to GO 

githuab.com/golang/proposal 

make a proposal 

# Kubernetes operators 

Challenges with containers at scale 

Orchestration
Security 
Monitoring and registration
Scalability
Data storage and persistance

Advantages of kubernetes 
Deployemtn automation
Automatically scale based on demand 
Application portability 
self-healing - what instances are failing and try to restart them - don't deploy until it's healthy 
Good option of microservices

Node containes multiple pod 

kubelet - start/stop monitoring the containers kube-proxy - facilitate networking between the pods

Kuberentes operators - Stateless application scaling 

kubectl scale deploy/staticweb  --replicas=4 

kubernetes was made for stateless applications
What about apps that store data

Kubernetes application lifecycle 

Day 0 -> planning and development 
Day 1 -> Operations and escalation
Day 2 -> Kube operators

Extend the kubernetes API 

Creating a custom resource deployment 
crontab 

cronspec "******/5"
Custom controller - > desired state == current state of the cluster

Operator framework -> guide with an SDK and all the steps to create your own operators!, operatorhub.io - find all the operators you want -- check it out 
automate  you  cluster shit 

Capability Model  

1. Basic install
2. Seamless upgrades
3. Full lifecycle
4. Deep insights 
5. Auto Pilot


# Differential fuzzing,\

OSS-Fuzz = check that shit out 

Fuzzin 
go test -fuzz

tries hundreds of thouseds of random inputs 

use a fuzzing engine - instructt it .  u can add inputs from unit tests 

They don't make assertions - checks  if the server crashes 

check inversible functions  
Examples:
Encoder/Decoder 
Marshal/Unmarshal

Differential fuzzin g- > random input to the 2 different implementations of the same problem  and check if it's the same 

Use an old implementation 
there's a c lib that can be used 
and CGO to call it 

Lexbor -  web engine   

Running test in CI 

ClusterFuzzLite inadequately supports native go fuzz tests problems with understanding extracting failing inputs 
inconvinietnt 

go-ci-fuzz 

form3tech-oss/go-ci-fuzz/ci 

hello@mionskowski.pl

go.dev/doc/tutorial/fuzz
google/oss-fuzz-gen
wiki/fuzzing
clusterfuzzlite
go-ci-fuzz
unmasking-go-html-parser-bug

How much time does it to run CI 

did u say that it caches the most common edge cases in the CI? 

provide a starting purpose - takes the basic input and changes it a bit 
go caches  captures the input  it will start from that point 

can we contribute to this?

commit test-data
