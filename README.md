# `nvidia-docker-compose`
`nvidia-docker-compose` is a simple python script that wraps [`docker-compose`](https://docs.docker.com/compose/) to allow `docker-compose` to work with GPU enabled Docker containers as made available with [`nvidia-docker`](https://github.com/NVIDIA/nvidia-docker)!

## Dependencies
`nvidia-docker-compose` requires following dependencies to be installed on the system:
* Docker engine
* `nvidia-docker`
* `docker-compose`

also it depends on `PyYAML` Python package which would be installed automatically during the installation step described below.

## Installing
To install the script, simply run:
```bash
$ pip3 install nvidia-docker-compose
```
If you are using system Python, it may be necessary to run the above command with `sudo` upfront.

## Using `nvidia-docker-compose`
The `nvidia-docker-compose` is a drop-in replacement for the `docker-compose`. Simply run as you would run `docker-compose`:
```bash
$ nvidia-docker-compose ...
```
Depending on how your system is configured, you may need to run the script with `sudo` (i.e. if you usually need `sudo` to run `docker`, you will need `sudo`).

Running `nvidia-docker-compose` generates a new YAML config file `nvidia-docker-compose.yml` locally. It is safe to delete this file in-between usages and I recommend you add this to your `.gitignore` file if you are going to use `nvidia-docker-compose` withint a Git repository. Once generated, you can also use the `nvidia-docker-compose.yml` directly to launch GPU enabled containers directly with the standard `docker-compose`. You can do so as:
```bash
$ docker-compose -f nvidia-docker-compose.yml ...
```

## How it works
`nvidia-docker-compose` is a simple Python script that performs two actions:
* parse `docker-compose` config file (defaults to `docker-compose.yml`) and creates a new config YAML `nvidia-docker-compose.yml` with configurations necessary to run GPU enabled containers. Configuration parameters are read from `nvidia-docker-plugins`.
* run `docker-compose` with the newly generated config file `nvidia-docker-compose.yml`

