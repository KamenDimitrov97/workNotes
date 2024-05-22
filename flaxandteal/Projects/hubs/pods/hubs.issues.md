# moz-haproxy

```sh
Events:
  Type     Reason     Age                    From               Message
  ----     ------     ----                   ----               -------
  Normal   Scheduled  21m                    default-scheduler  Successfully assigned fat-hubs-testing/moz-haproxy-5c49f8f749-pwnht to gke-everything-1-balanced-00feb8af-qatv
  Normal   Pulled     21m                    kubelet            Container image "haproxytech/kubernetes-ingress:1.8.5@sha256:09b59bc272e3aec5ca5b706774ed788c4bb4f184bb1d7ab99660a2b7773b0668" already present on machine
  Normal   Created    21m                    kubelet            Created container haproxy
  Normal   Started    21m                    kubelet            Started container haproxy
  Warning  Unhealthy  21m (x2 over 21m)      kubelet            Liveness probe failed: Get "http://10.8.3.123:1042/healthz": dial tcp 10.8.3.123:1042: connect: connection refused
  Warning  Unhealthy  6m53s (x5 over 9m23s)  kubelet            Liveness probe failed: Get "http://10.8.3.123:1042/healthz": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
  Normal   Killing    52s (x3 over 6m53s)    kubelet            Container haproxy failed liveness probe, will be restarted
```


# moz-hubs-ce
```sh
Events:
  Type     Reason     Age                   From               Message
  ----     ------     ----                  ----               -------
  Normal   Scheduled  21m                   default-scheduler  Successfully assigned fat-hubs-testing/moz-hubs-ce-65cd659758-s226s to gke-everything-1-balanced-00feb8af-qatv
  Normal   Pulled     21m                   kubelet            Container image "mozillareality/hubs:stable-latest" already present on machine
  Normal   Created    21m                   kubelet            Created container hubs-ce
  Normal   Started    21m                   kubelet            Started container hubs-ce
  Warning  Unhealthy  21m (x4 over 21m)     kubelet            Readiness probe failed: Get "https://10.8.3.119:8080/healthz": dial tcp 10.8.3.119:8080: connect: connection refused
  Warning  Unhealthy  7m3s                  kubelet            Readiness probe failed: Get "https://10.8.3.119:8080/healthz": net/http: request canceled (Client.Timeout exceeded while awaiting headers)
  Warning  Unhealthy  93s                   kubelet            Liveness probe failed: Get "https://10.8.3.119:8080/healthz": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
  Warning  Unhealthy  13s (x20 over 6m52s)  kubelet            Readiness probe failed: Get "https://10.8.3.119:8080/healthz": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
```

# moz-reticulum

```sh
Events:
  Type     Reason     Age                  From               Message
  ----     ------     ----                 ----               -------
  Normal   Scheduled  21m                  default-scheduler  Successfully assigned fat-hubs-testing/moz-reticulum-6cf75b6b4-shl29 to gke-everything-1-balanced-00feb8af-qatv
  Normal   Pulled     21m                  kubelet            Container image "mozillareality/ret:stable-798" already present on machine
  Normal   Created    21m                  kubelet            Created container reticulum
  Normal   Started    21m                  kubelet            Started container reticulum
  Normal   Pulling    21m                  kubelet            Pulling image "mozillareality/postgrest"
  Normal   Created    21m                  kubelet            Created container postgrest
  Normal   Pulled     21m                  kubelet            Successfully pulled image "mozillareality/postgrest" in 604.794646ms (18.363035004s including waiting)
  Normal   Started    21m                  kubelet            Started container postgrest
  Warning  Unhealthy  20m                  kubelet            Liveness probe failed: Get "http://10.8.3.116:4001/health": dial tcp 10.8.3.116:4001: connect: connection refused
  Warning  Unhealthy  20m (x13 over 21m)   kubelet            Readiness probe failed: Get "http://10.8.3.116:4001/?skipadmin": dial tcp 10.8.3.116:4001: connect: connection refused
  Warning  Unhealthy  20m                  kubelet            Liveness probe failed: HTTP probe failed with statuscode: 500
  Warning  Unhealthy  19m (x3 over 20m)    kubelet            Readiness probe failed: HTTP probe failed with statuscode: 503
  Warning  Unhealthy  70s (x11 over 7m5s)  kubelet            Readiness probe failed: Get "http://10.8.3.116:4001/?skipadmin": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
```

