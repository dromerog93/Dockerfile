FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.21"
LABEL description="BCFtools - Variant analysis tool in VCF/BCF format"
LABEL source="https://github.com/samtools/bcftools"
LABEL bioinfo.category="variant-calling"
LABEL bioinfo.subcategory="variant-calling"

ENV BCFTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make gcc ca-certificates \
        libbz2-dev liblzma-dev libz-dev libncurses-dev libcurl4-openssl-dev libssl-dev && \
    cd /tmp/ && \
    git clone --branch ${BCFTOOLS_VERSION} https://github.com/samtools/bcftools.git && \
    git clone --branch ${HTSLIB_VERSION} https://github.com/samtools/htslib.git && \
    cd htslib && \
    git submodule update --init --recursive && \ 
    make && \
    make install && \
    cd ../bcftools && \
    make && \
    make install && \
    apt-get purge -y git make gcc ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["bcftools"]