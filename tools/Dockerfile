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
    vim-tiny && \
    apt-get clean

RUN pip install yamllint

COPY --from=mikefarah/yq:4 /usr/bin/yq /usr/local/bin/yq
# COPY --from=hashicorp/terraform:0.14.10 /bin/terraform /usr/local/bin/terraform
COPY --from=lachlanevenson/k8s-kubectl:v1.19.9 /usr/local/bin/kubectl /usr/local/bin/kubectl
COPY --from=lachlanevenson/k8s-helm:v3.5.3 /usr/local/bin/helm /usr/local/bin/helm
COPY --from=docker:20.10 /usr/local/bin/docker /usr/local/bin/docker
COPY --from=hairyhenderson/gomplate:v3.9.0 /gomplate /bin/gomplate
COPY --from=bitnami/git:2.31.1 /opt/bitnami/git/bin /opt/bitnami/git/bin

ENV PATH="/opt/bitnami/git/bin:${PATH}"

WORKDIR /home

ENTRYPOINT [ "/bin/bash" ]
