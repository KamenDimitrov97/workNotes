Starting service
fatal: detected dubious ownership in repository at '/go'
To add an exception for this directory, call:

	git config --global --add safe.directory /go
fatal: detected dubious ownership in repository at '/go'
To add an exception for this directory, call:

	git config --global --add safe.directory /go
HUMAN_LOG=1 DEBUG=1 go run -tags 'debug' -race -ldflags "-X main.BuildTime=1711038717 -X main.GitCommit= -X main.Version=" main.go
go: errors parsing go.mod:
/go/go.mod:5: unknown directive: toolchain


# fatal: detected dubious ownership in repository at '/go' 

['Avoiding Dubious Ownership in Dev Containers'](https://www.kenmuse.com/blog/avoiding-dubious-ownership-in-dev-containers/)

just re-clone the repository

check the version used locally to the version used in the container of golang e.g.