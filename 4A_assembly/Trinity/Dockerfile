FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.15.2"
LABEL description="Trinity - De novo and genome-guided RNA-Seq transcriptome assembler"
LABEL source="https://github.com/trinityrnaseq/trinityrnaseq"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="transcriptome"

ENV TRINITY_VERSION=2.15.2
ENV BOWTIE2_VERSION=2.5.4
ENV SALMON_VERSION=1.10.3
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git ca-certificates make cmake gcc g++ curl unzip automake autoconf rsync \
        zlib1g-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libboost-all-dev libtbb-dev \
        perl python3 python-is-python3 openjdk-11-jre-headless samtools jellyfish python3-numpy \
        libtime-hires-perl libgomp1 && \
    git clone --branch v${BOWTIE2_VERSION} https://github.com/BenLangmead/bowtie2.git /tmp/bowtie2 && \
    cd /tmp/bowtie2 && \
    make && \
    cp bowtie2* /usr/local/bin/ && \
    git clone --branch v${SALMON_VERSION} https://github.com/COMBINE-lab/salmon.git /tmp/salmon && \
    cd /tmp/salmon && \
    cmake -B build -DCMAKE_INSTALL_PREFIX=/usr/local -DNO_VERSION_CHECK=ON && \
    cmake --build build && \
    cmake --install build && \
    git clone --branch Trinity-v${TRINITY_VERSION} --recursive https://github.com/trinityrnaseq/trinityrnaseq.git /tmp/trinity && \
    cd /tmp/trinity && \
    cp /usr/share/misc/config.* /tmp/trinity/trinity-plugins/bamsifter/htslib/ && \
    make plugins && \
    make && \
    make install && \
    apt-get purge -y git ca-certificates make cmake gcc g++ curl unzip automake autoconf \
        zlib1g-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libboost-all-dev libtbb-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["Trinity"]

