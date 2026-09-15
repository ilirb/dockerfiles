FROM python:3-slim-buster

RUN apt-get update && apt-get install --no-install-recommends -y \
    ca-certificates \
    curl \
    wget \
    sudo \
    # git \
    gzip \
    tar \
    jq \
    openssh-client \
    sshpass \
    bash-completion \
    iputils-ping \
    dnsutils \
    yq \
    vim-tiny && \
    apt-get clean

RUN pip install pyyaml requests yamllint

# COPY --from=docker:20.10 /usr/local/bin/docker /usr/local/bin/docker
WORKDIR /home

ENTRYPOINT [ "/bin/bash" ]
