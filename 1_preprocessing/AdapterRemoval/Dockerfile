FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.3.4"
LABEL description="AdapterRemoval - Adapter trimming and read merging tool for FASTQ files"
LABEL source="https://github.com/MikkelSchubert/adapterremoval"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="trimming"

ENV ADAPTERREMOVAL_VERSION=2.3.4
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make g++ ca-certificates \
        zlib1g-dev libbz2-dev && \
    git clone --branch v${ADAPTERREMOVAL_VERSION} https://github.com/MikkelSchubert/adapterremoval.git /tmp/adapterremoval && \
    cd /tmp/adapterremoval && \
    make && \
    make install && \
    apt-get purge -y git make g++ zlib1g-dev libbz2-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["AdapterRemoval"]

