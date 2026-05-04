FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.2.1"
LABEL description="HISAT2 - Fast and sensitive spliced aligner for RNA-Seq data"
LABEL source="https://github.com/DaehwanKimLab/hisat2"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="rna-aligner"

ENV HISAT2_VERSION=2.2.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
   apt-get install -y --no-install-recommends \
       git make g++ ca-certificates \
       python-is-python3 zlib1g-dev python3-minimal && \
    git clone --branch v${HISAT2_VERSION} https://github.com/DaehwanKimLab/hisat2.git /tmp/hisat2 && \
    cd /tmp/hisat2 && \
    make && \
    cp hisat2 /usr/local/bin/ && \
    cp hisat2-* /usr/local/bin/ && \
    cp hisat2*.py /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["hisat2"]