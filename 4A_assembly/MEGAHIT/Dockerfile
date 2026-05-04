FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.2.9"
LABEL description="MEGAHIT - Ultra-fast and memory-efficient assembler for NGS short reads"
LABEL source="https://github.com/voutcn/megahit"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="metagenome"

ENV MEGAHIT_VERSION=1.2.9
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       git make cmake g++ ca-certificates \
       zlib1g-dev bzip2 gzip libgomp1 python-is-python3 && \
    git clone --branch v${MEGAHIT_VERSION} https://github.com/voutcn/megahit.git /tmp/megahit && \
    cd /tmp/megahit && \
    git submodule update --init --recursive && \
    cmake -B build && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git make cmake g++ ca-certificates zlib1g-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["megahit"]

