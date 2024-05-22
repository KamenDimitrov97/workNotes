# BUILD FAILED (Fedora Linux 39 using python-build 2.3.36)

BUILD FAILED (Fedora Linux 39 using python-build 2.3.36)

Inspect or clean up the working tree at /tmp/python-build.20240214135603.69284
Results logged to /tmp/python-build.20240214135603.69284.log

## Found on fedora

### Check Dependencies

```sh
sudo dnf groupinstall "Development Tools"
```

### update pyenv
```sh
pyenv update
```

you should get a modules not found errors: 

```sh
sudo dnf install bzip2-devel ncurses-devel libffi-devel readline-devel sqlite-devel tk-devel
```
check out what kind of modules you're missing 

hopefully it should have been fixed

# CAN'T LOAD VENV CREATED
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