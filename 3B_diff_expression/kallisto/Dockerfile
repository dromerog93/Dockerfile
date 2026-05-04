FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.51.1"
LABEL description="kallisto - Pseudoalignment for RNA-seq quantification"
LABEL source="https://pachterlab.github.io/kallisto"
LABEL bioinfo.category="differential-expression"
LABEL bioinfo.subcategory="pseudoaligner"

ENV KALLISTO_VERSION=0.51.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       git cmake g++ make ca-certificates \
       zlib1g-dev libhdf5-dev && \
    git clone --branch v${KALLISTO_VERSION} https://github.com/pachterlab/kallisto.git /tmp/kallisto && \
    cd /tmp/kallisto && \
    cmake -B build -DUSE_HDF5=ON && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git cmake g++ make ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["kallisto"]