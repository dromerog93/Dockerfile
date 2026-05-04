FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.2.30"
LABEL description="Mosaik - Sensitive and accurate aligner for both short and long reads"
LABEL source="https://github.com/wanpinglee/MOSAIK"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="short-read"

ENV MOSAIK_VERSION=master
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make g++ make ca-certificates \
        zlib1g-dev && \
    git clone https://github.com/wanpinglee/MOSAIK.git /tmp/MOSAIK && \
    cd /tmp/MOSAIK/src/ && \
    make && \
    cp /tmp/MOSAIK/bin/Mosaik* /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["MosaikAligner"]