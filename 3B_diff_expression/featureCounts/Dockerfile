FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.1.1"
LABEL description="featureCounts - Read quantification tool from the Subread package"
LABEL source="https://subread.sourceforge.net"
LABEL bioinfo.category="differential-expression"
LABEL bioinfo.subcategory="quantification"

ENV SUBREAD_VERSION=2.1.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget make g++ ca-certificates \
        zlib1g-dev && \
    wget https://sourceforge.net/projects/subread/files/subread-${SUBREAD_VERSION}/subread-${SUBREAD_VERSION}-source.tar.gz -P /tmp && \
    tar -xzf /tmp/subread-${SUBREAD_VERSION}-source.tar.gz -C /tmp && \
    cd /tmp/subread-${SUBREAD_VERSION}-source/src && \
    make -f Makefile.Linux && \
    cp /tmp/subread-${SUBREAD_VERSION}-source/bin/utilities/* /usr/local/bin/ && \
    rm -r /tmp/subread-${SUBREAD_VERSION}-source/bin/utilities && \
    cp /tmp/subread-${SUBREAD_VERSION}-source/bin/* /usr/local/bin/ && \
    apt-get purge -y wget make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["featureCounts"]