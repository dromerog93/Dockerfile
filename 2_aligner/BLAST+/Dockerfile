FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.16.0"
LABEL description="NCBI BLAST+ - Toolkit for nucleotide and protein sequence alignments"
LABEL source="https://blast.ncbi.nlm.nih.gov/Blast.cgi"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="general"

ENV BLAST_VERSION=2.16.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      wget ca-certificates \
      libgomp1 perl curl && \
    wget -O /tmp/ncbi-blast.tar.gz https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VERSION}/ncbi-blast-${BLAST_VERSION}+-x64-linux.tar.gz && \
    mkdir -p /opt/blast && \
    tar -xzf /tmp/ncbi-blast.tar.gz -C /opt/blast --strip-components=1 && \
    ln -s /opt/blast/bin/* /usr/local/bin/ && \
    apt-get purge -y wget ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["blastn"]
