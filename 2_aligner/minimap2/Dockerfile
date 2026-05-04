FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.29"
LABEL description="Minimap2 - Versatile fast aligner for long DNA or RNA reads"
LABEL source="https://github.com/lh3/minimap2"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="long-read"

ENV MINIMAP2_VERSION=2.29
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      git make g++ ca-certificates \
      zlib1g-dev && \
    git clone --branch v${MINIMAP2_VERSION} https://github.com/lh3/minimap2.git /tmp/minimap2 && \
    cd /tmp/minimap2 && \
    make && \
    cp minimap2 /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["minimap2"]
