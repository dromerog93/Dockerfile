# Bioinformatics Tools

## Preprocessing

### rRNA-filtering

#### RiboDetector

```dockerfile
FROM python:3.8-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.3.1"
LABEL description="RiboDetector (CPU-Mode) - Tool to detect and remove rRNA reads from metatranscriptomic data."
LABEL source="https://github.com/hzi-bifo/RiboDetector"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="rRNA-filtering"

ENV RIBODETECTOR_VERSION=0.3.1
ENV TORCH_VERSION=1.10.2
ENV PIP_NO_CACHE_DIR=1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    pip install --no-cache-dir torch==${TORCH_VERSION}+cpu -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install --no-cache-dir git+https://github.com/hzi-bifo/RiboDetector.git@v${RIBODETECTOR_VERSION} && \
    apt-get purge -y git && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

WORKDIR /data

ENTRYPOINT ["ribodetector_cpu"]
```

#### SortMeRNA

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="4.3.7"
LABEL description="SortMeRNA - rRNA filtering tool for metatranscriptomics and RNA-seq"
LABEL source="https://github.com/biocore/sortmerna"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="rRNA-filtering"

ENV SORTMERNA_VERSION=4.3.7
ENV ROCKSDB_VERSION=9.1.1
ENV DEBIAN_FRONTEND=noninteractive
ENV LD_LIBRARY_PATH=/usr/local/lib

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git cmake make g++ ca-certificates \ 
        zlib1g-dev && \
    git clone --branch v${ROCKSDB_VERSION} https://github.com/facebook/rocksdb.git /tmp/rocksdb && \
    cd /tmp/rocksdb && \
    cmake -B build -DCMAKE_BUILD_TYPE=Release \
        -DWITH_TESTS=OFF -DWITH_TOOLS=OFF -DWITH_GFLAGS=OFF \
        -DWITH_ZLIB=ON && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    echo "/usr/local/lib" > /etc/ld.so.conf.d/rocksdb.conf && \
    ldconfig && \
    git clone --branch v${SORTMERNA_VERSION} https://github.com/biocore/sortmerna.git /tmp/sortmerna && \
    git clone https://github.com/cameron314/concurrentqueue.git /tmp/concurrentqueue && \
    cp /tmp/concurrentqueue/concurrentqueue.h /tmp/sortmerna/include/ && \
    cd /tmp/sortmerna && \ 
    cmake -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-include stdint.h" && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git cmake g++ zlib1g-dev ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["sortmerna"]
```

### read-merging

#### PandaSeq

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.11"
LABEL description="PandaSeq - Tool for merging paired-end Illumina reads"
LABEL source="https://github.com/neufeld/pandaseq"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="read-merging"

ENV PANDASEQ_VERSION=2.11
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make gcc ca-certificates \
        autoconf automake libtool libltdl-dev pkg-config \
        zlib1g-dev libbz2-dev libltdl7 && \
    git clone --branch v${PANDASEQ_VERSION} https://github.com/neufeld/pandaseq.git /tmp/pandaseq && \
    cd /tmp/pandaseq && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    apt-get purge -y git make gcc ca-certificates \
        autoconf automake pkg-config libtool libltdl-dev \
        zlib1g-dev libbz2-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["pandaseq"]
```

#### fastq-join

```dockerfile
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
```

### trimming

#### cutadapt

```dockerfile
FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="5.0"
LABEL description="cutadapt - Adapter trimming tool for FASTQ files"
LABEL source="https://cutadapt.readthedocs.io"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="trimming"

ENV CUTADAPT_VERSION=5.0
ENV PIP_NO_CACHE_DIR=1

RUN pip install --no-cache-dir cutadapt==${CUTADAPT_VERSION} && \
    rm -rf /root/.cache /tmp/*

WORKDIR /data

ENTRYPOINT ["cutadapt"]
```

#### fastp

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.24.0"
LABEL description="Fastp - All-in-one FASTQ preprocessor for quality control and trimming."
LABEL source="https://github.com/OpenGene/fastp"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="trimming"

ENV FASTP_VERSION=0.24.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget unzip make g++ ca-certificates \
        zlib1g-dev libisal-dev libdeflate-dev && \
    wget https://github.com/OpenGene/fastp/archive/refs/tags/v${FASTP_VERSION}.zip -O /tmp/fastp.zip && \
    unzip /tmp/fastp.zip -d /tmp/ && \
    cd /tmp/fastp-${FASTP_VERSION} && \
    make && \
    cp fastp /usr/local/bin && \
    apt-get purge -y make g++ wget unzip ca-certificates zlib1g-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["fastp"]
```

#### trimmomatic

```dockerfile
FROM openjdk:11-jre-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.39"
LABEL description="Trimmomatic - Flexible read trimming tool for Illumina NGS data."
LABEL source="http://www.usadellab.org/cms/?page=trimmomatic"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="trimming"

ENV TRIMMOMATIC_VERSION=0.39
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget ca-certificates unzip && \
    wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-${TRIMMOMATIC_VERSION}.zip -O /tmp/Trimmomatic.zip && \
    unzip /tmp/Trimmomatic.zip -d /opt/ && \
    ln -s /opt/Trimmomatic-${TRIMMOMATIC_VERSION}/trimmomatic-${TRIMMOMATIC_VERSION}.jar /opt/trimmomatic.jar && \
    apt-get purge -y wget ca-certificates unzip && \
    apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["java", "-jar", "/opt/trimmomatic.jar"]
```

