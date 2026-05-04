# Bioinformatics Tools

## Assembly

### hybrid

#### MaSuRCA

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="4.1.3"
LABEL description="MaSuRCA - Hybrid genome assembler combining Illumina and long reads"
LABEL source="https://github.com/alekseyzimin/masurca"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="hybrid"

ENV MASURCA_VERSION=4.1.3
ENV SAMTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV BWA_VERSION=0.7.19
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget make gcc g++ ca-certificates \
        zlib1g-dev libboost-dev libbz2-dev \
        perl libgomp1 && \
    wget -O /tmp/bwa-${BWA_VERSION}.tar.gz https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VERSION}.tar.gz && \
    tar -xzf /tmp/bwa-${BWA_VERSION}.tar.gz -C /tmp/ && \
    cd /tmp/bwa-${BWA_VERSION} && \
    make && \
    cp bwa /usr/local/bin/ && \
    wget -O /tmp/MaSuRCA-${MASURCA_VERSION}.tar.gz https://github.com/alekseyzimin/masurca/releases/download/v${MASURCA_VERSION}/MaSuRCA-${MASURCA_VERSION}.tar.gz && \
    tar -C /opt/ -xzvf /tmp/MaSuRCA-${MASURCA_VERSION}.tar.gz && \
    cd /opt/MaSuRCA-${MASURCA_VERSION} && \
    sed -i '/cp -a \.\.\/Flye/d' install.sh && \
    ./install.sh && \
    ln -s /opt/MaSuRCA-${MASURCA_VERSION}/bin/masurca /usr/local/bin/masurca && \
    ln -s /opt/MaSuRCA-${MASURCA_VERSION}/bin/polca.sh /usr/local/bin/polca && \
    ln -s /opt/MaSuRCA-${MASURCA_VERSION}/bin/chromosome_scaffolder.sh /usr/local/bin/chromosome_scaffolder && \
    ln -s /opt/MaSuRCA-${MASURCA_VERSION}/bin/samba.sh /usr/local/bin/samba && \
    apt-get purge -y wget make gcc g++ ca-certificates \
        zlib1g-dev libboost-dev libbz2-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["bash"]
```

#### Unicycler

```dockerfile
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
```

### long-read

#### Canu

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.3"
LABEL description="Canu 2.3 - Long-read assembler for PacBio and Oxford Nanopore reads"
LABEL source="https://github.com/marbl/canu"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="long-read"

ENV CANU_VERSION=2.3
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git g++ make ca-certificates perl \
        zlib1g-dev pkg-config liblzma-dev libssl-dev libcurl4-openssl-dev libbz2-dev \
        libgomp1 && \
    git clone --branch v${CANU_VERSION} https://github.com/marbl/canu.git /tmp/canu && \
    cd /tmp/canu/src && \
    make -j$(nproc) && \
    mkdir -p /opt/canu && \
    cp -r /tmp/canu/build/* /opt/canu/ && \
    ln -s /opt/canu/bin/canu /usr/local/bin/canu && \
    apt-get purge -y git g++ make ca-certificates \
        zlib1g-dev pkg-config liblzma-dev libssl-dev libcurl4-openssl-dev libbz2-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /root/.cache /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["canu"]
```

#### Flye

```dockerfile
FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.9.6"
LABEL description="Flye - Fast and accurate de novo assembler for long noisy reads"
LABEL source="https://github.com/mikolmogorov/Flye"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="long-read"

ENV FLYE_VERSION=2.9.6
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git g++ make ca-certificates \
        zlib1g-dev libcurl4-openssl-dev && \
    git clone --branch ${FLYE_VERSION} https://github.com/fenderglass/Flye.git /tmp/flye && \
    python /tmp/flye/setup.py install --prefix /usr/local && \
    apt-get purge -y git g++ make ca-certificates \
        zlib1g-dev libcurl4-openssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /root/.cache /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["flye"]
```

#### Hifiasm

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.25.0"
LABEL description="Hifiasm - Fast haplotype-resolved de novo assembler for PacBio HiFi reads"
LABEL source="https://github.com/chhylp123/hifiasm"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="long-read"

ENV HIFIASM_VERSION=0.25.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make g++ zlib1g-dev ca-certificates && \
    git clone --branch ${HIFIASM_VERSION} https://github.com/chhylp123/hifiasm.git /tmp/hifiasm && \
    cd /tmp/hifiasm && \
    make -j$(nproc) && \
    cp hifiasm /usr/local/bin/ && \
    apt-get purge -y git make g++ zlib1g-dev ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /root/.cache /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["hifiasm"]
```

#### NextDenovo

```dockerfile
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
```

#### Raven

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.8.3"
LABEL description="Raven - Fast and memory-efficient assembler for long error-prone reads"
LABEL source="https://github.com/lbcb-sci/raven"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="long-read"

ENV RAVEN_VERSION=1.8.3
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make cmake g++ ca-certificates \
        zlib1g-dev && \
    git clone --branch ${RAVEN_VERSION} https://github.com/lbcb-sci/raven.git /tmp/raven && \
    cd /tmp/raven && \
    cmake -B build -DRAVEN_BUILD_EXE=1 -DCMAKE_BUILD_TYPE=Release && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git make cmake g++ ca-certificates zlib1g-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /root/.cache /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["raven"]
```

#### Redbean

```dockerfile
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
```

### metagenome

#### MEGAHIT

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.2.9"
LABEL description="MEGAHIT - Ultra-fast and memory-efficient assembler for NGS short reads"
LABEL source="https://github.com/voutcn/megahit"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="metagenome"

ENV MEGAHIT_VERSION=1.2.9
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       git make cmake g++ ca-certificates \
       zlib1g-dev bzip2 gzip libgomp1 python-is-python3 && \
    git clone --branch v${MEGAHIT_VERSION} https://github.com/voutcn/megahit.git /tmp/megahit && \
    cd /tmp/megahit && \
    git submodule update --init --recursive && \
    cmake -B build && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git make cmake g++ ca-certificates zlib1g-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["megahit"]
```

### polishing

#### HyPo

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.0.3"
LABEL description="HyPo - Fast and accurate genome polishing tool using long and/or short reads"
LABEL source="https://github.com/kensung-lab/hypo"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="polishing"

ENV HYPO_VERSION=1.0.3
ENV KMC_VERSION=3.2.4
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git cmake make g++ ca-certificates python3-dev \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev \
        libcurl4-openssl-dev libgomp1 && \
    git clone --branch v${KMC_VERSION} --recurse-submodules https://github.com/refresh-bio/kmc.git /tmp/kmc && \
    cd /tmp/kmc && \
    make && \
    cp /tmp/kmc/bin/* /usr/local/bin/ && \
    git clone --branch v${HYPO_VERSION} --recursive https://github.com/kensung-lab/hypo.git /opt/hypo && \
    cd /opt/hypo && \
    chmod +x /opt/hypo/install_deps.sh && \
    ./install_deps.sh && \
    sed -i '/#include <chrono>/a #include <string>' /opt/hypo/external/suk/external/slog/include/slog/Monitor.hpp && \
    cp external/install/htslib/libhts.so external/install/htslib/lib/libhts.so && \
    cp external/install/htslib/libhts.a external/install/htslib/lib/libhts.a && \
    cp external/install/htslib/libhts.so.2to3part11 external/install/htslib/lib/libhts.so.2to3part11 && \
    export LD_LIBRARY_PATH=/opt/hypo/external/install/htslib:$LD_LIBRARY_PATH && \
    cmake -B build -DCMAKE_BUILD_TYPE=Release -Doptimise_for_native=ON && \
    cmake --build build && \
    cmake --install build && \
    apt-get purge -y git cmake make g++ ca-certificates python3-dev \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /opt/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["hypo"]
```

#### Medaka

```dockerfile
FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.1.0"
LABEL description="Medaka - Neural network polishing for Oxford Nanopore assemblies"
LABEL source="https://github.com/nanoporetech/medaka"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="polishing"

ENV MEDAKA_VERSION=2.1.0
ENV SAMTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV MINIMAP2_VERSION=2.29
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make gcc ca-certificates \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev && \
    git clone --branch ${HTSLIB_VERSION} https://github.com/samtools/htslib.git /tmp/htslib && \
    cd /tmp/htslib && \
    git submodule update --init --recursive && \ 
    make && \
    make install && \
    git clone --branch ${SAMTOOLS_VERSION} https://github.com/samtools/samtools.git /tmp/samtools && \
    cd /tmp/samtools && \
    make && \
    make install && \
    git clone --branch v${MINIMAP2_VERSION} https://github.com/lh3/minimap2.git /tmp/minimap2 && \
    cd /tmp/minimap2 && \
    make && \
    cp minimap2 /usr/local/bin/ && \
    pip install pyabpoa && \
    pip install --no-cache-dir medaka-cpu==${MEDAKA_VERSION} --extra-index-url https://download.pytorch.org/whl/cpu && \
    apt-get purge -y git make gcc ca-certificates \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["medaka_consensus"]
```

#### NextPolish

```dockerfile
FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.4.1"
LABEL description="NextPolish - Genome polishing tool for hybrid or long/short reads"
LABEL source="https://github.com/Nextomics/NextPolish"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="polishing"

ENV NEXTPOLISH_VERSION=1.4.1
ENV BWA_VERSION=0.7.19
ENV MINIMAP2_VERSION=2.29
ENV SAMTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV PIP_NO_CACHE_DIR=1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git wget ca-certificates build-essential \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev && \
    pip install paralleltask && \
    wget -O /tmp/bwa-${BWA_VERSION}.tar.gz https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VERSION}.tar.gz && \
    tar -xzf /tmp/bwa-${BWA_VERSION}.tar.gz -C /tmp/ && \
    cd /tmp/bwa-${BWA_VERSION} && \
    make && \
    cp bwa /usr/local/bin/ && \
    git clone --branch v${MINIMAP2_VERSION} https://github.com/lh3/minimap2.git /tmp/minimap2 && \
    cd /tmp/minimap2 && \
    make && \
    cp minimap2 /usr/local/bin/ && \
    git clone --branch ${HTSLIB_VERSION} https://github.com/samtools/htslib.git /tmp/htslib && \
    cd /tmp/htslib && \
    git submodule update --init --recursive && \ 
    make && \
    make install && \
    git clone --branch ${SAMTOOLS_VERSION} https://github.com/samtools/samtools.git /tmp/samtools && \
    cd /tmp/samtools && \
    make && \
    make install && \
    wget https://github.com/Nextomics/NextPolish/releases/download/v${NEXTPOLISH_VERSION}/NextPolish.tgz -O /tmp/NextPolish.tar.gz && \
    tar -xzf /tmp/NextPolish.tar.gz -C /tmp/ && \
    cd /tmp/NextPolish && \
    make -C util seq_split seq_count && \
    cp /tmp/NextPolish/util/seq_split /usr/local/bin/ && \
    cp /tmp/NextPolish/util/seq_count /usr/local/bin/ && \
    mkdir /opt/NextPolish && \
    cp -r lib /opt/NextPolish/ && \
    cp -r doc /opt/NextPolish/ && \
    cp LICENSE README.md /opt/NextPolish/ && \
    cp nextPolish /opt/NextPolish/ && \
    mkdir -p /opt/NextPolish/bin && \
    ln -s /usr/local/bin/seq_split /opt/NextPolish/bin/seq_split && \
    ln -s /usr/local/bin/seq_count /opt/NextPolish/bin/seq_count && \
    ln -s /usr/local/bin/samtools /opt/NextPolish/bin/samtools && \
    ln -s /usr/local/bin/bwa /opt/NextPolish/bin/bwa && \
    ln -s /usr/local/bin/minimap2 /opt/NextPolish/bin/minimap2 && \
    ln -s /opt/NextPolish/nextPolish /usr/local/bin/nextPolish && \
    apt-get purge -y git wget ca-certificates build-essential \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["nextPolish"]
```

#### Pilon

```dockerfile
FROM openjdk:11-jre-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.24"
LABEL description="Pilon - Assembly polishing tool using short reads (Illumina)"
LABEL source="https://github.com/broadinstitute/pilon"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="polishing"

ENV PILON_VERSION=1.24
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget ca-certificates && \
    wget https://github.com/broadinstitute/pilon/releases/download/v${PILON_VERSION}/pilon-${PILON_VERSION}.jar -O /opt/pilon.jar && \
    chmod +x /opt/pilon.jar && \
    apt-get purge -y wget ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["java", "-jar", "/opt/pilon.jar"]
```

#### PolyPolish

```dockerfile
FROM rust:1.87.0-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.6.0"
LABEL description="Polypolish - Illumina-based assembly polisher written in Rust"
LABEL source="https://github.com/rrwick/Polypolish"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="polishing"

ENV DEBIAN_FRONTEND=noninteractive
ENV POLYPOLISH_VERSION=0.6.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git ca-certificates samtools && \
    git clone --branch v${POLYPOLISH_VERSION} https://github.com/rrwick/Polypolish.git /tmp/Polypolish && \
    cd /tmp/Polypolish && \
    cargo build --release && \
    cp /tmp/Polypolish/target/release/polypolish /usr/local/bin/ && \
    apt-get purge -y git ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cargo/registry /root/.cargo/git

WORKDIR /data

ENTRYPOINT ["polypolish"]
```

#### Racon

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.5.0"
LABEL description="Racon - Consensus module for raw de novo genome assembly of long uncorrected reads"
LABEL source="https://github.com/lbcb-sci/racon"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="polishing"

ENV RACON_VERSION=1.5.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git cmake make g++ ca-certificates \
        zlib1g-dev && \
    git clone --branch ${RACON_VERSION} https://github.com/lbcb-sci/racon.git /tmp/racon && \
    cd /tmp/racon && \
    cmake -B build -DCMAKE_BUILD_TYPE=Release && \
    cmake --build build && \
    cmake --install build && \
    apt-get purge -y git cmake make g++ ca-certificates zlib1g-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["racon"]
```

### short-read

#### ABySS

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.3.10"
LABEL description="ABySS - A de novo, parallel, paired-end sequence assembler for short reads"
LABEL source="https://github.com/bcgsc/abyss"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="short-read"

ENV ABYSS_VERSION=2.3.10
ENV BTLLIB_VERSION=1.7.5
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       git gcc g++ cmake autoconf automake \
       meson ninja-build python3-dev ca-certificates \
       zlib1g-dev libopenmpi-dev libsparsehash-dev libboost-all-dev \
       make samtools bzip2 xz-utils \
       openmpi-bin libgomp1 && \
    git clone --branch v${BTLLIB_VERSION} https://github.com/bcgsc/btllib.git /tmp/btllib && \
    git clone https://github.com/simongog/sdsl-lite.git /tmp/btllib/subprojects/sdsl-lite && \
    cd /tmp/btllib/subprojects/sdsl-lite/ && \
    cmake -B build && \
    cmake --build build && \
    cd /tmp/btllib/ && \
    ./compile --prefix=/usr/local && \
    git clone --branch ${ABYSS_VERSION} https://github.com/bcgsc/abyss.git /tmp/abyss && \
    cd /tmp/abyss && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    apt-get purge -y git gcc g++ cmake autoconf automake \
       meson ninja-build python3-dev ca-certificates \
       zlib1g-dev libboost-all-dev libsparsehash-dev libopenmpi-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["abyss-pe"]
```

#### Minia

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="3.2.6"
LABEL description="Minia - Memory-efficient short-read genome assembler based on Bloom filters"
LABEL source="https://github.com/GATB/minia"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="short-read"

ENV MINIA_VERSION=3.2.6
ENV GATB_CORE_VERSION=1.4.2
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       git cmake make g++ ca-certificates \
       zlib1g-dev && \
    git clone --branch v${MINIA_VERSION} --recurse-submodules https://github.com/GATB/minia.git /tmp/minia && \
    cd /tmp/minia && \
    cmake -B build && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git make cmake g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["minia"]
```

#### SPAdes

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="4.2.0"
LABEL description="SPAdes - Genome assembler for single-cell, standard and metagenomic NGS data"
LABEL source="https://github.com/ablab/spades"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="short-read"

ENV SPADES_VERSION=4.2.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make cmake gcc g++ ca-certificates \
        zlib1g-dev libbz2-dev python3 python3-distutils libopenmpi-dev && \
    git clone --branch v${SPADES_VERSION} https://github.com/ablab/spades.git /tmp/spades && \
    cd /tmp/spades/src && \
    cmake -B build -DSPADES_ENABLE_PROJECTS="spades;hpcspades;hammer;corrector;spades_tools;binspreader;spaligner" && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git make cmake gcc g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

WORKDIR /data

ENTRYPOINT ["spades.py"]
```

### transcriptome

#### Scallop

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.10.5"
LABEL description="Scallop - Reference-based transcript assembler using RNA-seq alignments"
LABEL source="https://github.com/Kingsford-Group/scallop"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="transcriptome"

ENV SCALLOP_VERSION=0.10.5
ENV BOOST_VERSION=1.88.0
ENV SAMTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make cmake g++ ca-certificates autoconf automake libtool \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev \
        coinor-clp coinor-libclp-dev && \
    git clone --branch boost-${BOOST_VERSION} --recurse-submodules https://github.com/boostorg/boost.git /tmp/boost && \
    cd /tmp/boost && \
    ./bootstrap.sh && \
    ./b2 install --prefix=/usr/local && \
    git clone --branch ${HTSLIB_VERSION} https://github.com/samtools/htslib.git /tmp/htslib && \
    cd /tmp/htslib && \
    git submodule update --init --recursive && \ 
    make && \
    make install && \
    git clone --branch ${SAMTOOLS_VERSION} https://github.com/samtools/samtools.git /tmp/samtools && \
    cd /tmp/samtools && \
    make && \
    make install && \
    git clone --branch v${SCALLOP_VERSION} https://github.com/Kingsford-Group/scallop.git /tmp/scallop && \
    cd /tmp/scallop/ && \
    cp configure.linux.ac configure.ac && \
    aclocal && \
    autoheader && \
    automake --add-missing && \
    autoconf && \
    ./configure && \
    make && \
    make install && \
    apt-get purge -y git make cmake g++ ca-certificates autoconf automake libtool \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["scallop"]
```

#### StringTie

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="3.0.0"
LABEL description="StringTie - Fast and highly efficient assembler of RNA-Seq alignments into potential transcripts"
LABEL source="https://github.com/gpertea/stringtie"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="transcriptome"

ENV STRINGTIE_VERSION=3.0.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make g++ ca-certificates curl \
        zlib1g-dev libbz2-dev liblzma-dev libdeflate-dev \
        samtools && \
    git clone --branch v${STRINGTIE_VERSION} https://github.com/gpertea/stringtie.git /tmp/stringtie && \
    cd /tmp/stringtie && \
    make release && \
    cp stringtie /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates curl \
        zlib1g-dev libbz2-dev liblzma-dev libdeflate-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /var/lib/apt/lists/* /root/.cache

WORKDIR /data

ENTRYPOINT ["stringtie"]
```

#### Trinity

```dockerfile
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
```

#### trans-ABySS

```dockerfile
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
```

### transcriptome-merge

#### TACO

```dockerfile
FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.7.3"
LABEL description="TACO - Transcriptome Aggregation and Construction (multi-sample transcriptome assembler)"
LABEL source="https://github.com/tacorna/taco"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="transcriptome-merge"

ENV TACO_VERSION=0.7.3
ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_NO_CACHE_DIR=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget ca-certificates && \
    wget https://github.com/tacorna/taco/releases/download/v${TACO_VERSION}/taco-v${TACO_VERSION}.Linux_x86_64.tar.gz -O /tmp/taco.tar.gz && \
    tar -xzf /tmp/taco.tar.gz -C /tmp/ && \
    cp /tmp/taco-v${TACO_VERSION}.Linux_x86_64/taco* /usr/local/bin/ && \
    apt-get purge -y wget ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /root/.cache /tmp/* /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["taco_run"]
```

