FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.3.6"
LABEL description="FreeBayes - Bayesian genetic variant detector for polymorphisms and complex events"
LABEL source="https://github.com/freebayes/freebayes"
LABEL bioinfo.category="variant-calling"
LABEL bioinfo.subcategory="variant-calling"

ENV FREEBAYES_VERSION=1.3.6
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget ca-certificates \
        parallel python3-minimal && \
    wget https://github.com/freebayes/freebayes/releases/download/v${FREEBAYES_VERSION}/freebayes-${FREEBAYES_VERSION}-linux-amd64-static.gz -P /tmp && \
    gunzip /tmp/freebayes-${FREEBAYES_VERSION}-linux-amd64-static.gz && \
    mv /tmp/freebayes-${FREEBAYES_VERSION}-linux-amd64-static /usr/local/bin/freebayes && \
    chmod +x /usr/local/bin/freebayes && \
    wget https://github.com/freebayes/freebayes/releases/download/v${FREEBAYES_VERSION}/freebayes-${FREEBAYES_VERSION}-src.tar.gz -P /tmp && \
    mkdir /tmp/freebayes/ && \
    tar -xzf /tmp/freebayes-${FREEBAYES_VERSION}-src.tar.gz -C /tmp/ && \
    cp -r /tmp/freebayes/scripts /opt/freebayes/ && \
    ln -s /opt/freebayes/freebayes-parallel /usr/local/bin/freebayes-parallel && \
    ln -s /opt/freebayes/coverage_to_regions.py /usr/local/bin/coverage_to_regions && \
    ln -s /opt/freebayes/fasta_generate_regions.py /usr/local/bin/fasta_generate_regions && \
    apt-get purge -y wget ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["freebayes"]