
# Usage

1. Navigate to the project you wish to install a specific python version in and run:
```shell
pyenv install 3.10
```
2. Then run this cmd to create an env which will be stored inside .pyenv/python/version/you/want
```shell
pyenv virtualenv 3.10 cat
```
3. To activate 
```sh
pyenv activate cat
```
4. To deactivate the env that you're currently in 
```shell
pyenv deactivate
```
5. To uninstall a vir env:
```shell
pyenv uninstall <env_name>
```
