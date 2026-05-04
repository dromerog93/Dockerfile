FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.5.1"
LABEL description="Unicycler - Hybrid assembler with SPAdes, Racon and BLAST+"
LABEL source="https://github.com/rrwick/Unicycler"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="hybrid"

ENV DEBIAN_FRONTEND=noninteractive
ENV UNICYCLER_VERSION=0.5.1
ENV SPADES_VERSION=3.15.5
ENV RACON_VERSION=1.5.0
ENV BLAST_VERSION=2.16.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       python3 perl curl python3-distutils python-is-python3 \
       python3-pip python3-setuptools \
       git wget make cmake gcc g++ ca-certificates \
       zlib1g-dev libbz2-dev libopenmpi-dev \
       libgomp1 \
       samtools && \
    git clone --branch v${SPADES_VERSION} https://github.com/ablab/spades.git /tmp/spades && \
    cd /tmp/spades/assembler && \
    ./spades_compile.sh -j$(nproc) && \
    cp -r bin share /usr/local/ && \
    git clone --branch ${RACON_VERSION} --recursive https://github.com/lbcb-sci/racon.git /tmp/racon && \
    cd /tmp/racon && \
    cmake -B build -DCMAKE_BUILD_TYPE=Release && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    wget -O /tmp/ncbi-blast.tar.gz https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VERSION}/ncbi-blast-${BLAST_VERSION}+-x64-linux.tar.gz && \
    mkdir -p /opt/blast && \
    tar -xzf /tmp/ncbi-blast.tar.gz -C /opt/blast --strip-components=1 && \
    ln -s /opt/blast/bin/* /usr/local/bin/ && \
    git clone --branch v${UNICYCLER_VERSION} https://github.com/rrwick/Unicycler.git /tmp/unicycler && \
    cd /tmp/unicycler && \
    python3 setup.py install && \
    apt-get purge -y python3-pip python3-setuptools git make cmake gcc g++ wget zlib1g-dev libbz2-dev libopenmpi-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache /tmp/* && \
    rm -rf /usr/lib/python3/dist-packages/setuptools* /usr/share/doc/python3-pip*

WORKDIR /data

ENTRYPOINT ["unicycler"]

