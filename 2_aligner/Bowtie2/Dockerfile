FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.5.4"
LABEL description="Bowtie2 - Fast and sensitive gapped read aligner for short reads (Burrows-Wheeler Aligner)"
LABEL source="https://github.com/BenLangmead/bowtie2"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="short-read"

ENV BOWTIE2_VERSION=2.5.4
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      git make g++ ca-certificates \
      perl python3 zlib1g-dev && \
    git clone --branch v${BOWTIE2_VERSION} https://github.com/BenLangmead/bowtie2.git /tmp/bowtie2 && \
    cd /tmp/bowtie2 && \
    make && \
    cp bowtie2* /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["bowtie2"]
