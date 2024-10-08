# Tunneling and Port Forwarding

## Local Port Forwarding:
```sh
ssh -L local_port:localhost:remote_port username@remote_host
```
## This forwards a local port to a port on the remote server. For example, to access a database running on port 3306 of a remote server:
```sh
ssh -L 3306:localhost:3306 username@remote_host
```
You can then access the database locally on localhost:3306.

## Remote Port Forwarding:
```sh
ssh -R remote_port:localhost:local_port username@remote_host
```
This forwards a remote port on the server to a local machine.

## Dynamic Port Forwarding (SOCKS Proxy):
```sh
ssh -D local_port username@remote_host
```

## This sets up a SOCKS proxy, which can be used for tunneling traffic through the SSH connection. For example:
```sh
ssh -D 8080 username@remote_host
```
