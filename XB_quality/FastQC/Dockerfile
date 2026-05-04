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