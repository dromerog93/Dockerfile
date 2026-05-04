FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="4.1.3"
LABEL description="MaSuRCA - Hybrid genome assembler combining Illumina and long reads"
LABEL source="https://github.com/alekseyzimin/masurca"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="hybrid"

ENV MASURCA_VERSION=4.1.3
ENV SAMTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV BWA_VERSION=0.7.19
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget make gcc g++ ca-certificates \
        zlib1g-dev libboost-dev libbz2-dev \
        perl libgomp1 && \
    wget -O /tmp/bwa-${BWA_VERSION}.tar.gz https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VERSION}.tar.gz && \
    tar -xzf /tmp/bwa-${BWA_VERSION}.tar.gz -C /tmp/ && \
    cd /tmp/bwa-${BWA_VERSION} && \
    make && \
    cp bwa /usr/local/bin/ && \
    wget -O /tmp/MaSuRCA-${MASURCA_VERSION}.tar.gz https://github.com/alekseyzimin/masurca/releases/download/v${MASURCA_VERSION}/MaSuRCA-${MASURCA_VERSION}.tar.gz && \
    tar -C /opt/ -xzvf /tmp/MaSuRCA-${MASURCA_VERSION}.tar.gz && \
    cd /opt/MaSuRCA-${MASURCA_VERSION} && \
    sed -i '/cp -a \.\.\/Flye/d' install.sh && \
    ./install.sh && \
    ln -s /opt/MaSuRCA-${MASURCA_VERSION}/bin/masurca /usr/local/bin/masurca && \
    ln -s /opt/MaSuRCA-${MASURCA_VERSION}/bin/polca.sh /usr/local/bin/polca && \
    ln -s /opt/MaSuRCA-${MASURCA_VERSION}/bin/chromosome_scaffolder.sh /usr/local/bin/chromosome_scaffolder && \
    ln -s /opt/MaSuRCA-${MASURCA_VERSION}/bin/samba.sh /usr/local/bin/samba && \
    apt-get purge -y wget make gcc g++ ca-certificates \
        zlib1g-dev libboost-dev libbz2-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["bash"]

