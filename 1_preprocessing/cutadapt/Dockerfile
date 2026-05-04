FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="5.0"
LABEL description="cutadapt - Adapter trimming tool for FASTQ files"
LABEL source="https://cutadapt.readthedocs.io"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="trimming"

ENV CUTADAPT_VERSION=5.0
ENV PIP_NO_CACHE_DIR=1

RUN pip install --no-cache-dir cutadapt==${CUTADAPT_VERSION} && \
    rm -rf /root/.cache /tmp/*

WORKDIR /data

ENTRYPOINT ["cutadapt"]
