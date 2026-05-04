FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.1.0"
LABEL description="Medaka - Neural network polishing for Oxford Nanopore assemblies"
LABEL source="https://github.com/nanoporetech/medaka"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="polishing"

ENV MEDAKA_VERSION=2.1.0
ENV SAMTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV MINIMAP2_VERSION=2.29
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make gcc ca-certificates \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev && \
    git clone --branch ${HTSLIB_VERSION} https://github.com/samtools/htslib.git /tmp/htslib && \
    cd /tmp/htslib && \
    git submodule update --init --recursive && \ 
    make && \
    make install && \
    git clone --branch ${SAMTOOLS_VERSION} https://github.com/samtools/samtools.git /tmp/samtools && \
    cd /tmp/samtools && \
    make && \
    make install && \
    git clone --branch v${MINIMAP2_VERSION} https://github.com/lh3/minimap2.git /tmp/minimap2 && \
    cd /tmp/minimap2 && \
    make && \
    cp minimap2 /usr/local/bin/ && \
    pip install pyabpoa && \
    pip install --no-cache-dir medaka-cpu==${MEDAKA_VERSION} --extra-index-url https://download.pytorch.org/whl/cpu && \
    apt-get purge -y git make gcc ca-certificates \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["medaka_consensus"]