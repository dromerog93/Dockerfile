FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="5.0.1"
LABEL description="RSeQC - RNA-seq quality control toolkit for alignment-based QC metrics"
LABEL source="https://rseqc.sourceforge.net/"
LABEL bioinfo.category="quality-assessment"
LABEL bioinfo.subcategory="expression"

ENV RSEQC_VERSION=5.0.1
ENV PIP_NO_CACHE_DIR=1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        zlib1g-dev libpng-dev r-base && \
    pip install --no-cache-dir RSeQC==${RSEQC_VERSION} && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["bash"]