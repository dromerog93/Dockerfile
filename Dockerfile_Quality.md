# Bioinformatics Tools

## Quality-assessment

### alignment

#### Qualimap

```dockerfile
FROM openjdk:11-jre-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.3"
LABEL description="Qualimap - Quality control tool for alignment files (BAM/SAM)"
LABEL source="http://qualimap.conesalab.org/"
LABEL bioinfo.category="quality-assessment"
LABEL bioinfo.subcategory="alignment"

ENV QUALIMAP_VERSION=2.3
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       wget unzip \
       libfreetype6 libfontconfig1 && \
    wget -O /tmp/qualimap.zip https://bitbucket.org/kokonech/qualimap/downloads/qualimap_v${QUALIMAP_VERSION}.zip && \
    unzip /tmp/qualimap.zip -d /opt && \
    chmod +x /opt/qualimap*/qualimap && \
    ln -s /opt/qualimap*/qualimap /usr/local/bin/qualimap && \
    apt-get purge -y wget unzip && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["qualimap"]
```

### expression

#### RSeQC

```dockerfile
FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="5.0.1"
LABEL description="RSeQC - RNA-seq quality control toolkit for alignment-based QC metrics"
LABEL source="https://rseqc.sourceforge.net/"
LABEL bioinfo.category="quality-assessment"
LABEL bioinfo.subcategory="expression"

ENV RSEQC_VERSION=5.0.1
ENV PIP_NO_CACHE_DIR=1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        zlib1g-dev libpng-dev r-base && \
    pip install --no-cache-dir RSeQC==${RSEQC_VERSION} && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["bash"]
```

### fastq

#### FastQC

```dockerfile
FROM openjdk:11-jre-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.12.1"
LABEL description="FASTQC - Quality control tool for FASTQ files"
LABEL source="https://www.bioinformatics.babraham.ac.uk/projects/fastqc/"
LABEL bioinfo.category="quality-assessment"
LABEL bioinfo.subcategory="fastq"

ENV FASTQC_VERSION=0.12.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       wget unzip fontconfig fonts-dejavu-core \ 
       perl && \
    wget -O /tmp/fastqc.zip https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v${FASTQC_VERSION}.zip && \
    unzip /tmp/fastqc.zip -d /opt && \
    chmod +x /opt/FastQC/fastqc && \
    ln -s /opt/FastQC/fastqc /usr/local/bin/fastqc && \
    apt-get purge -y wget unzip && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["fastqc"]
```

#### MultiQC

```dockerfile
FROM python:3.11-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.28"
LABEL description="MultiQC - Aggregate quality control reports across bioinformatics tools"
LABEL source="https://multiqc.info"
LABEL bioinfo.category="quality-assessment"
LABEL bioinfo.subcategory="fastq"

ENV MULTIQC_VERSION=1.28
ENV DEBIAN_FRONTEND=noninteractive

RUN pip install multiqc==${MULTIQC_VERSION} && \
    apt-get clean && apt-get purge && \
    rm -rf /root/.cache /tmp/*

ENTRYPOINT ["multiqc"]
```

