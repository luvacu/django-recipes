# Recipes Django demo

This project contains a Django app for demo purposes.

## Prerequisites

### 1. Install pyenv + pyenv-virtualenv

Install `pyenv` to manage multiple versions of Python in the same machine, and `pyenv-virtualenv` to manage virtual environments:

#### Option A
Follow the [pyenv-installer](https://github.com/pyenv/pyenv-installer).

#### Option B
Run the following in your machine:

```bash
brew update
brew install pyenv
brew install pyenv-virtualenv
```

Next allow `pyenv` to automatically activate/deactivate environments when moving directories, by adding the following lines to your `.zshrc`, `.bashrc`, or `.bash_profile`:


```bash
# Load pyenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

This will load `pyenv` & `pyenv-virtualenv` when opening a new Terminal session, and automatically activate the virtualenv defined in the `.python-version` file in this directory.


### 2. Install pip dependencies

With the virtualenv activated from the previous step, install all the pip dependencies.

```bash
pip install -r requirements.txt
````

You can add more dependencies by adding them to the `requirements.in` file, and then let `pip-compile` to build the `requirements.txt` file:

```bash
pip-compile requirements.in 	# Updates requirements.txt
pip install -r requirements.txt # Installs the dependencies
```

### 3. Install Docker

You'll run the Django app in a Docker container. 


## How to run the project

After installing all the tools listed before, you can now run the project with `docker-compose`:

```bash
docker-compose up --build
```

Notice you can skip the build step by removing the `--build` option.

