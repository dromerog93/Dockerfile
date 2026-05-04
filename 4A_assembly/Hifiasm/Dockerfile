FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.25.0"
LABEL description="Hifiasm - Fast haplotype-resolved de novo assembler for PacBio HiFi reads"
LABEL source="https://github.com/chhylp123/hifiasm"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="long-read"

ENV HIFIASM_VERSION=0.25.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make g++ zlib1g-dev ca-certificates && \
    git clone --branch ${HIFIASM_VERSION} https://github.com/chhylp123/hifiasm.git /tmp/hifiasm && \
    cd /tmp/hifiasm && \
    make -j$(nproc) && \
    cp hifiasm /usr/local/bin/ && \
    apt-get purge -y git make g++ zlib1g-dev ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /root/.cache /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["hifiasm"]

