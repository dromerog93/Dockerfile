FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2025-04-18"
LABEL description="GMAP - Genomic Mapping and Alignment Program for RNA-Seq long reads"
LABEL source="http://research-pub.gene.com/gmap/"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="long-read"

ENV GMAP_VERSION=2025-04-18
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      wget make g++ ca-certificates \
      zlib1g-dev perl && \
    wget -O /tmp/gmap.tar.gz http://research-pub.gene.com/gmap/src/gmap-gsnap-${GMAP_VERSION}.tar.gz && \
    tar -xzf /tmp/gmap.tar.gz -C /tmp/ && \
    cd /tmp/gmap-${GMAP_VERSION} && \
    ./configure --prefix=/usr/local && \
    make && \
    make install && \
    apt-get purge -y wget make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["gmap"]
