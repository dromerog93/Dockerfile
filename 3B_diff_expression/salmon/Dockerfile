FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.10.3"
LABEL description="Salmon - Accurate transcript-level quantification from RNA-seq data"
LABEL source="https://github.com/COMBINE-lab/salmon"
LABEL bioinfo.category="differential-expression"
LABEL bioinfo.subcategory="pseudoaligner"

ENV SALMON_VERSION=1.10.3
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       git cmake g++ make ca-certificates curl unzip \
       zlib1g-dev libcurl4-openssl-dev libbz2-dev liblzma-dev libboost-all-dev libtbb-dev && \
    git clone --branch v${SALMON_VERSION} https://github.com/COMBINE-lab/salmon.git /tmp/salmon && \
    cd /tmp/salmon && \
    cmake -B build -DCMAKE_INSTALL_PREFIX=/usr/local -DNO_VERSION_CHECK=ON && \
    cmake --build build && \
    cmake --install build && \
    apt-get purge -y git cmake g++ make ca-certificates curl unzip \
       libcurl4-openssl-dev libboost-all-dev  && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["salmon"]
