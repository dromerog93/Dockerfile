FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.3.10"
LABEL description="ABySS - A de novo, parallel, paired-end sequence assembler for short reads"
LABEL source="https://github.com/bcgsc/abyss"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="short-read"

ENV ABYSS_VERSION=2.3.10
ENV BTLLIB_VERSION=1.7.5
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       git gcc g++ cmake autoconf automake \
       meson ninja-build python3-dev ca-certificates \
       zlib1g-dev libopenmpi-dev libsparsehash-dev libboost-all-dev \
       make samtools bzip2 xz-utils \
       openmpi-bin libgomp1 && \
    git clone --branch v${BTLLIB_VERSION} https://github.com/bcgsc/btllib.git /tmp/btllib && \
    git clone https://github.com/simongog/sdsl-lite.git /tmp/btllib/subprojects/sdsl-lite && \
    cd /tmp/btllib/subprojects/sdsl-lite/ && \
    cmake -B build && \
    cmake --build build && \
    cd /tmp/btllib/ && \
    ./compile --prefix=/usr/local && \
    git clone --branch ${ABYSS_VERSION} https://github.com/bcgsc/abyss.git /tmp/abyss && \
    cd /tmp/abyss && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    apt-get purge -y git gcc g++ cmake autoconf automake \
       meson ninja-build python3-dev ca-certificates \
       zlib1g-dev libboost-all-dev libsparsehash-dev libopenmpi-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["abyss-pe"]