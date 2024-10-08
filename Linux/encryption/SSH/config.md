# SSH Configuration
## Edit the SSH Config File:
```sh
nano ~/.ssh/config
```
In the SSH config file, you can create shortcuts for SSH connections. For example:

```sh
Host myserver
    HostName remote_host
    User username
    Port 2222
    IdentityFile ~/.ssh/id_rsa
```

## Now, you can connect to the server with:
```sh
ssh myserver
SSH Troubleshooting and Management
```

## Check SSH Service Status (on the server):
```sh
sudo systemctl status ssh
```
This checks whether the SSH service is running on the server.

## Restart SSH Service (on the server):
```sh
sudo systemctl restart ssh
```

## Change SSH Port: To change the default SSH port, edit the /etc/ssh/sshd_config file and modify the Port directive:
```sh
sudo nano /etc/ssh/sshd_config
```

## Then restart the SSH service:
```sh
sudo systemctl restart ssh
```

## SSH Verbose Mode (Debugging):
```sh
ssh -v username@remote_host
```
The -v option enables verbose output, which helps in debugging connection issues. You can increase verbosity with -vv or -vvv.

## Check SSH Connection Fingerprint: When you first connect to a remote server, SSH saves the server’s fingerprint in ~/.ssh/known_hosts. You can check it with:
```sh
ssh-keygen -l -f ~/.ssh/known_hosts
```