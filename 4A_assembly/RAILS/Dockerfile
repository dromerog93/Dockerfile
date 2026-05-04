FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.5.1"
LABEL description="RAILS + Cobbler - Long-read scaffolding and gap filling module"
LABEL source="https://github.com/bcgsc/RAILS"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="scaffolding"

ENV RAILS_VERSION=1.5.1
ENV SAMTOOLS_VERSION=1.8
ENV HTSLIB_VERSION=1.8
ENV BWA_VERSION=0.7.15
ENV MINIMAP2_VERSION=2.15
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git perl make gcc ca-certificates \
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
    git clone --branch v${BWA_VERSION} https://github.com/lh3/bwa.git /tmp/bwa && \
    cd /tmp/bwa && \
    sed -i '/rle_auxtab/d' rle.h && \
    make && \
    cp bwa /usr/local/bin/ && \
    git clone --branch v${MINIMAP2_VERSION} https://github.com/lh3/minimap2.git /tmp/minimap2 && \
    cd /tmp/minimap2 && \
    make && \
    cp minimap2 /usr/local/bin/ && \
    git clone --branch v${RAILS_VERSION} https://github.com/bcgsc/RAILS.git /tmp/RAILS && \
    cp /tmp/RAILS/bin/* /usr/local/bin/ && \
    apt-get purge -y git make gcc ca-certificates \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["runRAILS.sh"]