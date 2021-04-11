FROM alpine:3.13.4

RUN apk update && \
    apk add jq && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["/usr/bin/jq"]
