FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="4.2.0"
LABEL description="SPAdes - Genome assembler for single-cell, standard and metagenomic NGS data"
LABEL source="https://github.com/ablab/spades"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="short-read"

ENV SPADES_VERSION=4.2.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make cmake gcc g++ ca-certificates \
        zlib1g-dev libbz2-dev python3 python3-distutils libopenmpi-dev && \
    git clone --branch v${SPADES_VERSION} https://github.com/ablab/spades.git /tmp/spades && \
    cd /tmp/spades/src && \
    cmake -B build -DSPADES_ENABLE_PROJECTS="spades;hpcspades;hammer;corrector;spades_tools;binspreader;spaligner" && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git make cmake gcc g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

WORKDIR /data

ENTRYPOINT ["spades.py"]