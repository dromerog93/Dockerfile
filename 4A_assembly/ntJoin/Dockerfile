FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.1.5"
LABEL description="ntJoin - Reference-guided scaffolding using k-mer mapping and compact graphs"
LABEL source="https://github.com/bcgsc/ntJoin"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="scaffolding"

ENV NTJOIN_VERSION=1.1.5
ENV BEDTOOLS_VERSION=2.29.2
ENV SAMTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV BTLLIB_VERSION=1.7.5
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git cmake make gcc g++ ca-certificates \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev \
        bzip2 xz-utils libgomp1 && \
    git clone --branch v${BEDTOOLS_VERSION} https://github.com/arq5x/bedtools2.git /tmp/bedtools && \
    cd /tmp/bedtools && \
    make && \
    make install && \
    git clone --branch ${HTSLIB_VERSION} https://github.com/samtools/htslib.git /tmp/htslib && \
    cd /tmp/htslib && \
    git submodule update --init --recursive && \ 
    make && \
    make install && \
    git clone --branch ${SAMTOOLS_VERSION} https://github.com/samtools/samtools.git /tmp/samtools && \
    cd /tmp/samtools && \
    make && \
    make install && \
    git clone --branch v${BTLLIB_VERSION} https://github.com/bcgsc/btllib.git /tmp/btllib && \
    git clone https://github.com/simongog/sdsl-lite.git /tmp/btllib/subprojects/sdsl-lite && \
    cd /tmp/btllib/subprojects/sdsl-lite/ && \
    cmake -B build && \
    cmake --build build && \
    cd /tmp/btllib/ && \
    ./compile --prefix=/usr/local && \
    pip install /usr/local/lib/btllib/python/ && \
    git clone --branch v${NTJOIN_VERSION} https://github.com/bcgsc/ntJoin.git /tmp/ntJoin && \
    cd /tmp/ntJoin && \
    pip install --no-cache-dir python-igraph pybedtools pymannkendall packaging && \
    pip install . && \
    cp /tmp/ntJoin/ntJoin /usr/local/bin/ntJoin && \
    cp -r /tmp/ntJoin/bin /usr/local/bin/ && \
    apt-get purge -y git git gcc g++ ca-certificates \
        zlib1g-dev libbz2-dev liblzma-dev libssl-dev && \
    apt-get autoremove -y && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["ntJoin"]