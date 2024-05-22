# Connecting to other linux machines remotely

generate ssh key

```shell
ssh-gen 
```

```shell
ip addr show | grep "inet "
```

Get your ip address that's available for a local network machine

```sh
ssh user@thatIp + password 
```

or you could use to copy something over


```sh
scp file kamen@192.168.1.28:~/dev/work/github/onyx/onyx-dp-nlp-category-api/data/
scp -r dir kamen@192.168.1.28:~/dev/work/github/onyx/onyx-dp-nlp-category-api/data/
```

# mac 
deactive wall - need to reactivate it firewall system settings

remote login - turn off


I'm running into an error on dp-search-api when trying to run go mod tidy
GO: go version go1.21.7 linux/amd64
OS: Fedora 39
```
~/dev/work/github/onyx/dp-search-api$ go mod tidy
go: downloading github.com/ONSdigital/dp-api-clients-go/v2 v2.256.0
... 
verifying github.com/ONSdigital/log.go/v2@v2.0.9/go.mod: checksum mismatch
	downloaded: h1:9w+SkChyhtIK7XCha+cq6bq2DpTaK16Q4LofgoEGMSk=
	go.sum:     h1:VyTDkL82FtiAkaNFaT+bURBhLbP7NsIx4rkVbdpiuEg=

SECURITY ERROR
This download does NOT match an earlier download recorded in go.sum.
The bits may have been replaced on the origin server, or an attacker may
have intercepted the download attempt.

For more information, see 'go help module-auth'.
```

I've tried removing go.sum file so that it's re-generated but I get this err
```
go: github.com/ONSdigital/dp-api-clients-go@v1.43.0 requires
	github.com/ONSdigital/dp-net@v1.2.0 requires
	github.com/ONSdigital/log.go@v1.1.0 requires
	github.com/ONSdigital/dp-net@v1.0.5-0.20200805150805-cac050646ab5: invalid version: unknown revision cac050646ab5
```

I've tried:
reinstalling the listed packages 
downgrading my golang version: go version go1.21.1 linux/amd64
removing the cache using -modcache flag
removing the cache manually 
removing all github downloads in the go dir
tried completely wiping golang from my computer and reinstalling it a couple of times
tried wiping everything go related from extensions to configs
switching to different commits of this repo: F&T develop, ONS develop
tried freshly cloning the repos in separate dirs
this error keeps poping up 



Doesn't