FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.1.11"
LABEL description="DIAMOND - Fast protein aligner for high-throughput sequencing data"
LABEL source="https://github.com/bbuchfink/diamond"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="general"

ENV DIAMOND_VERSION=2.1.11
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git ca-certificates make cmake g++ \ 
        zlib1g-dev perl && \
    git clone --branch=v${DIAMOND_VERSION} https://github.com/bbuchfink/diamond.git /tmp/diamond && \
    cd /tmp/diamond && \
    cmake -B build && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git ca-certificates make cmake g++ && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["diamond"]
