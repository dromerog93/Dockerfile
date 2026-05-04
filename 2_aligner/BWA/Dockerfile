FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.7.19"
LABEL description="BWA - Burrows-Wheeler Aligner for short read alignment"
LABEL source="https://github.com/lh3/bwa"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="short-read"

ENV BWA_VERSION=0.7.19
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      git make gcc ca-certificates \
      zlib1g-dev && \
    git clone --branch v${BWA_VERSION} https://github.com/lh3/bwa.git /tmp/bwa && \
    cd /tmp/bwa && \
    make && \
    cp bwa /usr/local/bin/ && \
    apt-get purge -y git make gcc ca-certificates zlib1g-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["bwa"]
