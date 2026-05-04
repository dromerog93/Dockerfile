FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.9.6"
LABEL description="Flye - Fast and accurate de novo assembler for long noisy reads"
LABEL source="https://github.com/mikolmogorov/Flye"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="long-read"

ENV FLYE_VERSION=2.9.6
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git g++ make ca-certificates \
        zlib1g-dev libcurl4-openssl-dev && \
    git clone --branch ${FLYE_VERSION} https://github.com/fenderglass/Flye.git /tmp/flye && \
    python /tmp/flye/setup.py install --prefix /usr/local && \
    apt-get purge -y git g++ make ca-certificates \
        zlib1g-dev libcurl4-openssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /root/.cache /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["flye"]

