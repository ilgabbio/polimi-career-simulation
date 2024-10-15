# ARGOVision × POLIMI: anomaly detection in industry

In this workshop we will tackle a problem of anomaly detection like we would in a real world scenario.

## TOC

* [Requirements](#requirements)
* [Workspace setup](#workspace-setup)
* [Workspace description](#workspace-description)
* [Enjoy](#enjoy)

## Requirements

To the aim of use this repo you need to:

- install both `docker` and `docker-compose`.
- (optionally) Copy the `MVTec` in `workspace/datasets`. This will save some time later.
- (optionally) You can run the notebook in Colab in case of troubles (you will need a Google account).

## Workspace setup

0. Check that `docker` and `docker-compose` are installed and correctly working:

    ```sh
    docker --version
    docker compose version
    ```

1. Build and run the Docker image:

    ```sh
    docker compose up --build
    ```

    The provided `compose.yml` starts a `jupyter` service, you can connect to that service using the
    browser and the link provided at startup (it looks like `http://127.0.0.1:8888/tree?token=...`).


## Workspace description

Once the environment setup is completed, you will have the mounted `workspace` folder to interact
with the Docker machine and persist your work (you might need _sudo_ permissions to write).

## Enjoy

Follow the instructions on the notebook. Don't hesitate to ask in case of troubles.