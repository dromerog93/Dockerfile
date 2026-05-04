FROM python:3.8-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.3.1"
LABEL description="RiboDetector (CPU-Mode) - Tool to detect and remove rRNA reads from metatranscriptomic data."
LABEL source="https://github.com/hzi-bifo/RiboDetector"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="rRNA-filtering"

ENV RIBODETECTOR_VERSION=0.3.1
ENV TORCH_VERSION=1.10.2
ENV PIP_NO_CACHE_DIR=1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    pip install --no-cache-dir torch==${TORCH_VERSION}+cpu -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install --no-cache-dir git+https://github.com/hzi-bifo/RiboDetector.git@v${RIBODETECTOR_VERSION} && \
    apt-get purge -y git && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

WORKDIR /data

ENTRYPOINT ["ribodetector_cpu"]
