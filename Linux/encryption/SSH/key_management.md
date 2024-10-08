# SSH Key Management

## Generate an SSH Key Pair:
```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
This generates a new SSH key pair. -t rsa specifies the RSA algorithm, and -b 4096 sets the key size to 4096 bits.

## Add Your SSH Key to the SSH Agent:
```sh
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```
This starts the SSH agent and adds your private key to it for password-less authentication.

## Copy Public Key to a Remote Server:
```sh
ssh-copy-id username@remote_host
```
This copies your public SSH key (~/.ssh/id_rsa.pub) to the remote server’s ~/.ssh/authorized_keys file, allowing password-less login.