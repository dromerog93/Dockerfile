FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.8.3"
LABEL description="Raven - Fast and memory-efficient assembler for long error-prone reads"
LABEL source="https://github.com/lbcb-sci/raven"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="long-read"

ENV RAVEN_VERSION=1.8.3
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make cmake g++ ca-certificates \
        zlib1g-dev && \
    git clone --branch ${RAVEN_VERSION} https://github.com/lbcb-sci/raven.git /tmp/raven && \
    cd /tmp/raven && \
    cmake -B build -DRAVEN_BUILD_EXE=1 -DCMAKE_BUILD_TYPE=Release && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git make cmake g++ ca-certificates zlib1g-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /root/.cache /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["raven"]

