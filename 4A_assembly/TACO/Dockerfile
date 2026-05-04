FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.7.3"
LABEL description="TACO - Transcriptome Aggregation and Construction (multi-sample transcriptome assembler)"
LABEL source="https://github.com/tacorna/taco"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="transcriptome-merge"

ENV TACO_VERSION=0.7.3
ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_NO_CACHE_DIR=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget ca-certificates && \
    wget https://github.com/tacorna/taco/releases/download/v${TACO_VERSION}/taco-v${TACO_VERSION}.Linux_x86_64.tar.gz -O /tmp/taco.tar.gz && \
    tar -xzf /tmp/taco.tar.gz -C /tmp/ && \
    cp /tmp/taco-v${TACO_VERSION}.Linux_x86_64/taco* /usr/local/bin/ && \
    apt-get purge -y wget ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /root/.cache /tmp/* /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["taco_run"]

