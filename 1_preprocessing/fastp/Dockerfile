FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.24.0"
LABEL description="Fastp - All-in-one FASTQ preprocessor for quality control and trimming."
LABEL source="https://github.com/OpenGene/fastp"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="trimming"

ENV FASTP_VERSION=0.24.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget unzip make g++ ca-certificates \
        zlib1g-dev libisal-dev libdeflate-dev && \
    wget https://github.com/OpenGene/fastp/archive/refs/tags/v${FASTP_VERSION}.zip -O /tmp/fastp.zip && \
    unzip /tmp/fastp.zip -d /tmp/ && \
    cd /tmp/fastp-${FASTP_VERSION} && \
    make && \
    cp fastp /usr/local/bin && \
    apt-get purge -y make g++ wget unzip ca-certificates zlib1g-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["fastp"]
