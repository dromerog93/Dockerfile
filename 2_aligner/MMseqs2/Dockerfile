FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="17-b804f"
LABEL description="MMseqs2 - Fast and sensitive protein sequence search and clustering suite"
LABEL source="https://github.com/soedinglab/MMseqs2"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="general"

ENV MMSEQS2_VERSION=17-b804f
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git ca-certificates make cmake g++ \ 
        zlib1g-dev libatomic1 libgomp1 && \
    git clone --branch ${MMSEQS2_VERSION} https://github.com/soedinglab/MMseqs2.git /tmp/mmseqs2 && \
    cd /tmp/mmseqs2 && \
    cmake -B build && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git ca-certificates make cmake g++ zlib1g-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["mmseqs"]
