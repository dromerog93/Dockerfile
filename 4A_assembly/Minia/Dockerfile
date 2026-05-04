FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="3.2.6"
LABEL description="Minia - Memory-efficient short-read genome assembler based on Bloom filters"
LABEL source="https://github.com/GATB/minia"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="short-read"

ENV MINIA_VERSION=3.2.6
ENV GATB_CORE_VERSION=1.4.2
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       git cmake make g++ ca-certificates \
       zlib1g-dev && \
    git clone --branch v${MINIA_VERSION} --recurse-submodules https://github.com/GATB/minia.git /tmp/minia && \
    cd /tmp/minia && \
    cmake -B build && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git make cmake g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["minia"]