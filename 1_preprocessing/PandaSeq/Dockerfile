FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.11"
LABEL description="PandaSeq - Tool for merging paired-end Illumina reads"
LABEL source="https://github.com/neufeld/pandaseq"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="read-merging"

ENV PANDASEQ_VERSION=2.11
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make gcc ca-certificates \
        autoconf automake libtool libltdl-dev pkg-config \
        zlib1g-dev libbz2-dev libltdl7 && \
    git clone --branch v${PANDASEQ_VERSION} https://github.com/neufeld/pandaseq.git /tmp/pandaseq && \
    cd /tmp/pandaseq && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    apt-get purge -y git make gcc ca-certificates \
        autoconf automake pkg-config libtool libltdl-dev \
        zlib1g-dev libbz2-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["pandaseq"]
