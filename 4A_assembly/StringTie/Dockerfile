FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="3.0.0"
LABEL description="StringTie - Fast and highly efficient assembler of RNA-Seq alignments into potential transcripts"
LABEL source="https://github.com/gpertea/stringtie"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="transcriptome"

ENV STRINGTIE_VERSION=3.0.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make g++ ca-certificates curl \
        zlib1g-dev libbz2-dev liblzma-dev libdeflate-dev \
        samtools && \
    git clone --branch v${STRINGTIE_VERSION} https://github.com/gpertea/stringtie.git /tmp/stringtie && \
    cd /tmp/stringtie && \
    make release && \
    cp stringtie /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates curl \
        zlib1g-dev libbz2-dev liblzma-dev libdeflate-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /var/lib/apt/lists/* /root/.cache

WORKDIR /data

ENTRYPOINT ["stringtie"]

