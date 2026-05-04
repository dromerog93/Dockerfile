FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.7.11b"
LABEL description="STAR - Ultrafast spliced aligner for RNA-Seq data"
LABEL source="https://github.com/alexdobin/STAR"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="rna-aligner"

ENV STAR_VERSION=2.7.11b
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make g++ ca-certificates vim-common \
        zlib1g-dev libgomp1 && \
    git clone --branch ${STAR_VERSION} https://github.com/alexdobin/STAR.git /tmp/STAR && \
    cd /tmp/STAR/source && \
    make && \
    cp STAR /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates vim-common && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["STAR"]