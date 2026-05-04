FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.5.0"
LABEL description="Racon - Consensus module for raw de novo genome assembly of long uncorrected reads"
LABEL source="https://github.com/lbcb-sci/racon"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="polishing"

ENV RACON_VERSION=1.5.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git cmake make g++ ca-certificates \
        zlib1g-dev && \
    git clone --branch ${RACON_VERSION} https://github.com/lbcb-sci/racon.git /tmp/racon && \
    cd /tmp/racon && \
    cmake -B build -DCMAKE_BUILD_TYPE=Release && \
    cmake --build build && \
    cmake --install build && \
    apt-get purge -y git cmake make g++ ca-certificates zlib1g-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["racon"]

