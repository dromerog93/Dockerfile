FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.2.4"
LABEL description="Clustal Omega - Fast and scalable multiple sequence alignment tool"
LABEL source="https://www.ebi.ac.uk/Tools/msa/clustalo/"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="msa"

ENV CLUSTALO_VERSION=1.2.4
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl ca-certificates make g++ autoconf automake libtool \
        libgomp1 libargtable2-dev && \
    cd /tmp/ && \
    curl -L http://www.clustal.org/omega/clustal-omega-${CLUSTALO_VERSION}.tar.gz | tar zx && \
    cd clustal-omega-${CLUSTALO_VERSION} && \
    ./configure && \
    make && \
    make install && \
    apt-get purge -y curl ca-certificates make g++ autoconf automake libtool && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["clustalo"]

