FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.5"
LABEL description="Redbean (wtdbg2) - Fast de novo assembler for long noisy reads"
LABEL source="https://github.com/ruanjue/wtdbg2"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="long-read"

ENV REDBEAN_VERSION=2.5
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make gcc zlib1g-dev ca-certificates && \
    git clone --branch v${REDBEAN_VERSION} https://github.com/ruanjue/wtdbg2.git /tmp/wtdbg2 && \
    cd /tmp/wtdbg2 && \
    make -j$(nproc) && \
    cp wtdbg2 wtpoa-cns kbm2 pgzf wtdbg2.pl wtdbg-cns /usr/local/bin/ && \
    cp -r /tmp/wtdbg2/scripts /usr/local/bin && \
    apt-get purge -y git make gcc zlib1g-dev ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /var/lib/apt/lists/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["wtdbg2"]

