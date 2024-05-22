# Installation:

1. Install necessary dependencies

```shell
sudo apt-get update
sudo apt-get install git curl libssl-dev libreadline-dev zlib1g-dev libbz2-dev libsqlite3-dev
```

2. Install pyenv locally - This cmd will create a folder .pyenv inside $HOME and install pyenv there
```shell
curl https://pyenv.run | bash
```
## Installer

you could also use installer
https://github.com/pyenv/pyenv#automatic-installer


3. Add it to to your $PATH 

    ```shell
    sudo nano ~/.bashrc
    ```
    - inside add the following: 
    `PYENV_ROOT="$HOME/.pyenv"`
    - update your $PATH var
    `PATH=$PATH:/your/folders/bin:$PYENV_ROOT/bin`
    - source your ~/.bashrc file
    ```shell
    source ~/.bashrc
    ```
4. check if installation was successful `pyenv --version`
