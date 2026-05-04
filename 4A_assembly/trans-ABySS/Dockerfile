FROM dromero93/abyss:latest

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.0.1"
LABEL description="Trans-ABySS - De novo transcriptome assembler pipeline based on ABySS"
LABEL source="https://github.com/bcgsc/transabyss"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="transcriptome"

ENV TRANSABYSS_VERSION=2.0.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 python-is-python3 \
        git python3-pip ca-certificates wget && \
    pip install --no-cache-dir igraph && \
    wget https://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/blat/blat -O /usr/local/bin/blat && \
    chmod +x /usr/local/bin/blat && \
    git clone --branch ${TRANSABYSS_VERSION} https://github.com/bcgsc/transabyss.git /opt/transabyss && \
    sed -i -E "s/\bis not\s+(['\"]{1})\1/!= \1\1/g" /opt/transabyss/utilities/psl_cid_extractor.py && \
    ln -s /opt/transabyss/transabyss /usr/local/bin/transabyss && \
    apt-get purge -y git python3-pip ca-certificates wget && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["transabyss"]

