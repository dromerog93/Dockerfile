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
