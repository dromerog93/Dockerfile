# Bioinformatics Tools

## Diff-expression

### differential-analysis

#### R-analysis

```dockerfile
FROM rocker/r-ver:4.5.0

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="4.5.0"
LABEL description="DESeq2, edgeR and limma - Differential expression analysis tools in R (Bioconductor)"
LABEL source="https://bioconductor.org/packages/3.21/, https://bioconductor.org/packages/release/bioc/html/DESeq2.html, https://bioconductor.org/packages/release/bioc/html/edgeR.html, https://www.bioconductor.org/packages/release/bioc/html/limma.html"
LABEL bioinfo.category="diff-expression"
LABEL bioinfo.subcategory="differential-analysis"

ENV DEBIAN_FRONTEND=noninteractive
ENV DESEQ2_VERSION=1.48.0
ENV EDGER_VERSION=4.6.2
ENV LIMMA_VERSION=3.64.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends zlib1g-dev && \
    Rscript -e "install.packages('BiocManager')" && \
    Rscript -e "BiocManager::install(version = '3.21')" && \
    Rscript -e "BiocManager::install(c('DESeq2', 'edgeR', 'limma'))" && \
    Rscript -e "stopifnot( \
        packageVersion('DESeq2') == Sys.getenv('DESEQ2_VERSION'), \
        packageVersion('edgeR') == Sys.getenv('EDGER_VERSION'), \
        packageVersion('limma') == Sys.getenv('LIMMA_VERSION'))" && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

CMD ["Rscript"]
```

## Differential-expression

### pseudoaligner

#### kallisto

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.51.1"
LABEL description="kallisto - Pseudoalignment for RNA-seq quantification"
LABEL source="https://pachterlab.github.io/kallisto"
LABEL bioinfo.category="differential-expression"
LABEL bioinfo.subcategory="pseudoaligner"

ENV KALLISTO_VERSION=0.51.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       git cmake g++ make ca-certificates \
       zlib1g-dev libhdf5-dev && \
    git clone --branch v${KALLISTO_VERSION} https://github.com/pachterlab/kallisto.git /tmp/kallisto && \
    cd /tmp/kallisto && \
    cmake -B build -DUSE_HDF5=ON && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git cmake g++ make ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["kallisto"]
```

#### salmon

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.10.3"
LABEL description="Salmon - Accurate transcript-level quantification from RNA-seq data"
LABEL source="https://github.com/COMBINE-lab/salmon"
LABEL bioinfo.category="differential-expression"
LABEL bioinfo.subcategory="pseudoaligner"

ENV SALMON_VERSION=1.10.3
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       git cmake g++ make ca-certificates curl unzip \
       zlib1g-dev libcurl4-openssl-dev libbz2-dev liblzma-dev libboost-all-dev libtbb-dev && \
    git clone --branch v${SALMON_VERSION} https://github.com/COMBINE-lab/salmon.git /tmp/salmon && \
    cd /tmp/salmon && \
    cmake -B build -DCMAKE_INSTALL_PREFIX=/usr/local -DNO_VERSION_CHECK=ON && \
    cmake --build build && \
    cmake --install build && \
    apt-get purge -y git cmake g++ make ca-certificates curl unzip \
       libcurl4-openssl-dev libboost-all-dev  && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["salmon"]
```

### quantification

#### HTSeq-count

```dockerfile
FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.0.9"
LABEL description="HTSeq-count - Python framework to count reads per gene from BAM/SAM files"
LABEL source="https://htseq.readthedocs.io/en/master/"
LABEL bioinfo.category="differential-expression"
LABEL bioinfo.subcategory="quantification"

ENV HTSEQ_VERSION=2.0.9
ENV PIP_NO_CACHE_DIR=1
ENV DEBIAN_FRONTEND=noninteractive

RUN pip install --no-cache-dir HTSeq==${HTSEQ_VERSION} && \
    rm -rf /root/.cache /tmp/*

WORKDIR /data

ENTRYPOINT ["htseq-count"]
```

#### featureCounts

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.1.1"
LABEL description="featureCounts - Read quantification tool from the Subread package"
LABEL source="https://subread.sourceforge.net"
LABEL bioinfo.category="differential-expression"
LABEL bioinfo.subcategory="quantification"

ENV SUBREAD_VERSION=2.1.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget make g++ ca-certificates \
        zlib1g-dev && \
    wget https://sourceforge.net/projects/subread/files/subread-${SUBREAD_VERSION}/subread-${SUBREAD_VERSION}-source.tar.gz -P /tmp && \
    tar -xzf /tmp/subread-${SUBREAD_VERSION}-source.tar.gz -C /tmp && \
    cd /tmp/subread-${SUBREAD_VERSION}-source/src && \
    make -f Makefile.Linux && \
    cp /tmp/subread-${SUBREAD_VERSION}-source/bin/utilities/* /usr/local/bin/ && \
    rm -r /tmp/subread-${SUBREAD_VERSION}-source/bin/utilities && \
    cp /tmp/subread-${SUBREAD_VERSION}-source/bin/* /usr/local/bin/ && \
    apt-get purge -y wget make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["featureCounts"]
```

