FROM python:3-slim

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
    vim-tiny && \
    apt-get clean

RUN pip install pyyaml requests yamllint
RUN wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/local/bin/yq && chmod +x /usr/local/bin/yq

WORKDIR /home

ENTRYPOINT [ "/bin/bash" ]
