FROM python:2.7-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.2.8"
LABEL description="BESST - Bayesian scaffolder using paired-end or mate-pair information"
LABEL source="https://github.com/ksahlin/BESST"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="scaffolding"

ENV BESST_VERSION=2.2.8
ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_NO_CACHE_DIR=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        zlib1g-dev libbz2-dev liblzma-dev && \
    pip install --no-cache-dir BESST==${BESST_VERSION} && \
    apt-get purge -y build-essential zlib1g-dev libbz2-dev liblzma-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /root/.cache /tmp/* /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["runBESST"]