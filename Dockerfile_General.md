# Bioinformatics Tools

## Aligners

### rna-aligner

#### samtools

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.21"
LABEL description="Samtools - Toolkit for manipulation of SAM/BAM/CRAM files"
LABEL source="https://github.com/samtools/samtools"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="rna-aligner"

ENV SAMTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        git make gcc ca-certificates \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev && \
    git clone --branch ${HTSLIB_VERSION} https://github.com/samtools/htslib.git /tmp/htslib && \
    cd /tmp/htslib && \
    git submodule update --init --recursive && \ 
    make && \
    make install && \
    git clone --branch ${SAMTOOLS_VERSION} https://github.com/samtools/samtools.git /tmp/samtools && \
    cd /tmp/samtools && \
    make && \
    make install && \
    apt-get purge -y git make gcc ca-certificates && \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["samtools"]
```

