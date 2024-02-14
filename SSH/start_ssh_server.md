# Linux (Ubuntu, Debian, CentOS, etc.)
Install SSH Server:

```bash
sudo apt update
sudo apt install openssh-server
```

```bash
sudo systemctl start ssh
```
To ensure that the SSH server starts automatically at boot, enable the service:

```bash
sudo systemctl enable ssh
```

# Mac

Enable Remote Login:

Open "System Preferences."
Navigate to "Sharing."
Check the "Remote Login" option.
This activates the built-in SSH server on macOS.