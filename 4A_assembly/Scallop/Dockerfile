FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.10.5"
LABEL description="Scallop - Reference-based transcript assembler using RNA-seq alignments"
LABEL source="https://github.com/Kingsford-Group/scallop"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="transcriptome"

ENV SCALLOP_VERSION=0.10.5
ENV BOOST_VERSION=1.88.0
ENV SAMTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make cmake g++ ca-certificates autoconf automake libtool \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev \
        coinor-clp coinor-libclp-dev && \
    git clone --branch boost-${BOOST_VERSION} --recurse-submodules https://github.com/boostorg/boost.git /tmp/boost && \
    cd /tmp/boost && \
    ./bootstrap.sh && \
    ./b2 install --prefix=/usr/local && \
    git clone --branch ${HTSLIB_VERSION} https://github.com/samtools/htslib.git /tmp/htslib && \
    cd /tmp/htslib && \
    git submodule update --init --recursive && \ 
    make && \
    make install && \
    git clone --branch ${SAMTOOLS_VERSION} https://github.com/samtools/samtools.git /tmp/samtools && \
    cd /tmp/samtools && \
    make && \
    make install && \
    git clone --branch v${SCALLOP_VERSION} https://github.com/Kingsford-Group/scallop.git /tmp/scallop && \
    cd /tmp/scallop/ && \
    cp configure.linux.ac configure.ac && \
    aclocal && \
    autoheader && \
    automake --add-missing && \
    autoconf && \
    ./configure && \
    make && \
    make install && \
    apt-get purge -y git make cmake g++ ca-certificates autoconf automake libtool \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["scallop"]

