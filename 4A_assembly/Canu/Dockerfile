FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.3"
LABEL description="Canu 2.3 - Long-read assembler for PacBio and Oxford Nanopore reads"
LABEL source="https://github.com/marbl/canu"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="long-read"

ENV CANU_VERSION=2.3
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git g++ make ca-certificates perl \
        zlib1g-dev pkg-config liblzma-dev libssl-dev libcurl4-openssl-dev libbz2-dev \
        libgomp1 && \
    git clone --branch v${CANU_VERSION} https://github.com/marbl/canu.git /tmp/canu && \
    cd /tmp/canu/src && \
    make -j$(nproc) && \
    mkdir -p /opt/canu && \
    cp -r /tmp/canu/build/* /opt/canu/ && \
    ln -s /opt/canu/bin/canu /usr/local/bin/canu && \
    apt-get purge -y git g++ make ca-certificates \
        zlib1g-dev pkg-config liblzma-dev libssl-dev libcurl4-openssl-dev libbz2-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /root/.cache /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["canu"]

