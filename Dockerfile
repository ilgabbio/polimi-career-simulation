FROM ubuntu:22.04

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
        make \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libffi-dev \
        liblzma-dev \
        git

WORKDIR /work

COPY Pipfile Pipfile.lock utils.py workshop.ipynb .

RUN apt install python3-pip -y
RUN pip install pipenv
RUN pipenv sync

COPY startup.sh /

ENTRYPOINT bash /startup.sh
