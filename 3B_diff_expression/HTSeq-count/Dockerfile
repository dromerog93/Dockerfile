FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.0.9"
LABEL description="HTSeq-count - Python framework to count reads per gene from BAM/SAM files"
LABEL source="https://htseq.readthedocs.io/en/master/"
LABEL bioinfo.category="differential-expression"
LABEL bioinfo.subcategory="quantification"

ENV HTSEQ_VERSION=2.0.9
ENV PIP_NO_CACHE_DIR=1
ENV DEBIAN_FRONTEND=noninteractive

RUN pip install --no-cache-dir HTSeq==${HTSEQ_VERSION} && \
    rm -rf /root/.cache /tmp/*

WORKDIR /data

ENTRYPOINT ["htseq-count"]

