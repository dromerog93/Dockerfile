FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.31.1"
LABEL description="Bedtools - A powerful toolset for genome arithmetic"
LABEL source="https://github.com/arq5x/bedtools2"
LABEL bioinfo.category="general"
LABEL bioinfo.subcategory="general"

ENV BEDTOOLS_VERSION=2.31.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make g++ ca-certificates python3 \
        zlib1g-dev libbz2-dev liblzma-dev && \
    git clone --branch v${BEDTOOLS_VERSION} https://github.com/arq5x/bedtools2.git /tmp/bedtools && \
    cd /tmp/bedtools && \
    make && \
    make install && \
    apt-get purge -y git make g++ ca-certificates \
        zlib1g-dev libbz2-dev liblzma-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["bedtools"]