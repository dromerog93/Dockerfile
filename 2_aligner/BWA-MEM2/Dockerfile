FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.2.1"
LABEL description="BWA-MEM2 - Fast reimplementation of BWA-MEM for short read alignment"
LABEL source="https://github.com/bwa-mem2/bwa-mem2"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="short-read"

ENV BWAMEM2_VERSION=2.2.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      wget bzip2 ca-certificates \
      zlib1g-dev && \
    wget -O /tmp/bwa-mem2.tar.bz2 https://github.com/bwa-mem2/bwa-mem2/releases/download/v${BWAMEM2_VERSION}/bwa-mem2-${BWAMEM2_VERSION}_x64-linux.tar.bz2 && \
    mkdir /tmp/bwa-mem2 && tar -xjf /tmp/bwa-mem2.tar.bz2 -C /tmp && \
    cp /tmp/bwa-mem2-${BWAMEM2_VERSION}_x64-linux/bwa-mem2* /usr/local/bin/ && \
    apt-get purge -y wget bzip2 ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["bwa-mem2"]
