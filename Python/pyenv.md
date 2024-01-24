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

# Usage

1. Navigate to the project you wish to install a specific python version in and run:
```shell
pyenv install 3.8.12
```
2. Then run this cmd to create an env which will be stored inside .pyenv/python/version/you/want
```shell
pyenv virtualenv 3.8.12 <env_name>
```
3. To activate 
```
pyenv activate <env_name>
```
4. To deactivate the env that you're currently in 
```shell
pyenv deactivate
```
5. To uninstall a vir env:
```shell
pyenv uninstall <env_name>
```

## Issues I encountered 

1. can't load virtual env you've created 

    - Check if virtualenv plugin is installed correctly
    ```shell
    pyenv virtualenv-init - | grep virtualenv
    ```
    - If plugin not installed
    ```shell
    git clone https://github.com/pyenv/pyenv-virtualenv.git $PYENV_ROOT/plugins/pyenv-virtualenv
    ```
    - If installed and runs correctly 
    ```shell
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    ```
    See if cmd runs correctly
    ```shell
    pyenv virtualenv-init -
    ```
    - Restart terminal and try again
    ```shell
    pyenv activate /path/to/virtualenv
    ```