# Hello, Astronomer! - The Enterprise Framework for Apache Airflow

## Installing Astronomer CLI with Homebrew

```sh
brew install astronomer/tap/astro
```

## Initializing Airflow Project

```sh
mkdir astro && cd astro
astro dev init
```

## Starting Airflow on Local

```sh
astro dev start
```

If you get an error similar to this below:
```
buildkit not supported by daemon
Error: command 'docker build -t astro_e24539/airflow:latest failed: failed to execute cmd: exit status 1
```

Try this:
```sh
DOCKER_BUILDKIT=0 astro dev start
```

Reference: [‘buildkit not supported by daemon Error: command ‘docker build -t airflow-astro_bcb837/airflow:latest failed: failed to execute cmd: exit status 1](https://forum.astronomer.io/t/buildkit-not-supported-by-daemon-error-command-docker-build-t-airflow-astro-bcb837-airflow-latest-failed-failed-to-execute-cmd-exit-status-1/857)