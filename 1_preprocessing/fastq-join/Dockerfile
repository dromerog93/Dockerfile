FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version=1.3.1
LABEL description="fastq-join - Joining paired-end reads with overlaps."
LABEL source="https://github.com/brwnj/fastq-join"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="read-merging"

ENV FASTQJOIN_VERSION=1.3.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git g++ make ca-certificates && \
    git clone --branch v${FASTQJOIN_VERSION} https://github.com/brwnj/fastq-join.git /tmp/fastq-join && \
    cd /tmp/fastq-join && \
    make && \
    cp /tmp/fastq-join/fastq-join /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["fastq-join"]
