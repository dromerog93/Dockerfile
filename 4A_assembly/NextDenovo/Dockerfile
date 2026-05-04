FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.5.2"
LABEL description="NextDenovo - De novo assembler optimized for long noisy reads"
LABEL source="https://github.com/Nextomics/NextDenovo"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="long-read"

ENV NEXTDENOVO_VERSION=2.5.2
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make gcc ca-certificates \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev libdeflate-dev && \
    pip install paralleltask && \
    git clone --branch ${NEXTDENOVO_VERSION} https://github.com/Nextomics/NextDenovo.git /opt/NextDenovo && \
    cd /opt/NextDenovo && \
    sed -i '/^bam_sort:/,/^$/s/-lpthread -lm -lz/& -ldeflate -lssl -lcrypto -lcurl/' /opt/NextDenovo/util/Makefile && \
    sed -i '/^ctg_cns.so:/,/^$/s/$(CTG_CNS_CFLAGS)/$(CTG_CNS_CFLAGS) -lcurl -ldeflate -lssl -lcrypto -lz -lpthread/' /opt/NextDenovo/lib/Makefile && \
    make && \
    ln -s /opt/NextDenovo/nextDenovo /usr/local/bin/nextDenovo && \
    apt-get purge -y git make gcc ca-certificates \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["nextDenovo"]
