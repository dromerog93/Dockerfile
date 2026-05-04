FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.0.1"
LABEL description="LINKS - Long-read scaffolder using k-mers for ultra-fast contig connection"
LABEL source="https://github.com/bcgsc/LINKS"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="scaffolding"

ENV LINKS_VERSION=2.0.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git perl g++ make autoconf automake ca-certificates && \
    git clone --branch v${LINKS_VERSION} --recursive https://github.com/bcgsc/LINKS.git /tmp/LINKS && \
    cd /tmp/LINKS && \
    ./autogen.sh && \
    ./configure && \
    make install && \
    apt-get purge -y git g++ make autoconf automake ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["LINKS"]

