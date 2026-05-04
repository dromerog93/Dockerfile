FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.4.1"
LABEL description="NextPolish - Genome polishing tool for hybrid or long/short reads"
LABEL source="https://github.com/Nextomics/NextPolish"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="polishing"

ENV NEXTPOLISH_VERSION=1.4.1
ENV BWA_VERSION=0.7.19
ENV MINIMAP2_VERSION=2.29
ENV SAMTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV PIP_NO_CACHE_DIR=1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git wget ca-certificates build-essential \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev && \
    pip install paralleltask && \
    wget -O /tmp/bwa-${BWA_VERSION}.tar.gz https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VERSION}.tar.gz && \
    tar -xzf /tmp/bwa-${BWA_VERSION}.tar.gz -C /tmp/ && \
    cd /tmp/bwa-${BWA_VERSION} && \
    make && \
    cp bwa /usr/local/bin/ && \
    git clone --branch v${MINIMAP2_VERSION} https://github.com/lh3/minimap2.git /tmp/minimap2 && \
    cd /tmp/minimap2 && \
    make && \
    cp minimap2 /usr/local/bin/ && \
    git clone --branch ${HTSLIB_VERSION} https://github.com/samtools/htslib.git /tmp/htslib && \
    cd /tmp/htslib && \
    git submodule update --init --recursive && \ 
    make && \
    make install && \
    git clone --branch ${SAMTOOLS_VERSION} https://github.com/samtools/samtools.git /tmp/samtools && \
    cd /tmp/samtools && \
    make && \
    make install && \
    wget https://github.com/Nextomics/NextPolish/releases/download/v${NEXTPOLISH_VERSION}/NextPolish.tgz -O /tmp/NextPolish.tar.gz && \
    tar -xzf /tmp/NextPolish.tar.gz -C /tmp/ && \
    cd /tmp/NextPolish && \
    make -C util seq_split seq_count && \
    cp /tmp/NextPolish/util/seq_split /usr/local/bin/ && \
    cp /tmp/NextPolish/util/seq_count /usr/local/bin/ && \
    mkdir /opt/NextPolish && \
    cp -r lib /opt/NextPolish/ && \
    cp -r doc /opt/NextPolish/ && \
    cp LICENSE README.md /opt/NextPolish/ && \
    cp nextPolish /opt/NextPolish/ && \
    mkdir -p /opt/NextPolish/bin && \
    ln -s /usr/local/bin/seq_split /opt/NextPolish/bin/seq_split && \
    ln -s /usr/local/bin/seq_count /opt/NextPolish/bin/seq_count && \
    ln -s /usr/local/bin/samtools /opt/NextPolish/bin/samtools && \
    ln -s /usr/local/bin/bwa /opt/NextPolish/bin/bwa && \
    ln -s /usr/local/bin/minimap2 /opt/NextPolish/bin/minimap2 && \
    ln -s /opt/NextPolish/nextPolish /usr/local/bin/nextPolish && \
    apt-get purge -y git wget ca-certificates build-essential \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["nextPolish"]

