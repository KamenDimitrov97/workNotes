# Basic SSH Commands

## Connect to a Remote Server:
```sh
ssh username@remote_host
```
This command connects to a remote server using the default SSH port (22). Replace username with your remote user and remote_host with the server’s IP address or hostname.

## Connect to a Remote Server on a Custom Port:
```sh
ssh username@remote_host -p port_number
```
If the SSH service is running on a non-default port, you can specify the port with the -p option.

## Run a Command on a Remote Server:
```sh
ssh username@remote_host "command"
```
## You can execute a single command on the remote server without logging in interactively. For example:
```sh
ssh username@remote_host "ls -l /var/www"
```
## Copy a File from Local to Remote:
```sh
scp /path/to/local/file username@remote_host:/path/to/remote/directory
```
```sh
scp (Secure Copy) is used for transferring files between local and remote systems over SSH.
```

## Copy a File from Remote to Local:
```sh
scp username@remote_host:/path/to/remote/file /path/to/local/directory
```
## Copy a Directory Recursively:
```sh
scp -r /path/to/local/directory username@remote_host:/path/to/remote/directory
```
The -r option is for copying directories recursively.

## Copy Files Using rsync:
```sh
rsync -avz /path/to/local/file username@remote_host:/path/to/remote/directory
```
rsync is an alternative to scp that offers features like bandwidth control and resume interrupted transfers. The -a flag is for archiving, -v for verbose output, and -z for compression.