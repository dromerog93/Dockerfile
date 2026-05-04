# Bioinformatics Tools

## Variant-calling

### variant-calling

#### FreeBayes

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.3.6"
LABEL description="FreeBayes - Bayesian genetic variant detector for polymorphisms and complex events"
LABEL source="https://github.com/freebayes/freebayes"
LABEL bioinfo.category="variant-calling"
LABEL bioinfo.subcategory="variant-calling"

ENV FREEBAYES_VERSION=1.3.6
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget ca-certificates \
        parallel python3-minimal && \
    wget https://github.com/freebayes/freebayes/releases/download/v${FREEBAYES_VERSION}/freebayes-${FREEBAYES_VERSION}-linux-amd64-static.gz -P /tmp && \
    gunzip /tmp/freebayes-${FREEBAYES_VERSION}-linux-amd64-static.gz && \
    mv /tmp/freebayes-${FREEBAYES_VERSION}-linux-amd64-static /usr/local/bin/freebayes && \
    chmod +x /usr/local/bin/freebayes && \
    wget https://github.com/freebayes/freebayes/releases/download/v${FREEBAYES_VERSION}/freebayes-${FREEBAYES_VERSION}-src.tar.gz -P /tmp && \
    mkdir /tmp/freebayes/ && \
    tar -xzf /tmp/freebayes-${FREEBAYES_VERSION}-src.tar.gz -C /tmp/ && \
    cp -r /tmp/freebayes/scripts /opt/freebayes/ && \
    ln -s /opt/freebayes/freebayes-parallel /usr/local/bin/freebayes-parallel && \
    ln -s /opt/freebayes/coverage_to_regions.py /usr/local/bin/coverage_to_regions && \
    ln -s /opt/freebayes/fasta_generate_regions.py /usr/local/bin/fasta_generate_regions && \
    apt-get purge -y wget ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["freebayes"]
```

#### GATK

```dockerfile
FROM openjdk:17-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="4.6.2.0"
LABEL description="GATK - Toolkit for variant analysis developed by the Broad Institute"
LABEL source="https://github.com/broadinstitute/gatk"
LABEL bioinfo.category="variant-calling"
LABEL bioinfo.subcategory="variant-calling"

ENV GATK_VERSION=4.6.2.0
ENV SPARK_VERSION=3.5.1
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git git-lfs wget \
        python-is-python3 && \
    wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz -P /tmp && \
    tar -xzf /tmp/spark-${SPARK_VERSION}-bin-hadoop3.tgz -C /opt && \
    ln -s /opt/spark-${SPARK_VERSION}-bin-hadoop3 /opt/spark && \
    cd /tmp/ && \
    git clone --branch ${GATK_VERSION} https://github.com/broadinstitute/gatk.git && \
    cd gatk && \
    ./gradlew installAll && \
    mv build/* /usr/local/bin/ && \
    ln -s /usr/local/bin/install/gatk/bin/gatk /usr/local/bin/gatk && \
    apt-get purge -y git-lfs git wget && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["gatk"]
```

#### bcftools

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.21"
LABEL description="BCFtools - Variant analysis tool in VCF/BCF format"
LABEL source="https://github.com/samtools/bcftools"
LABEL bioinfo.category="variant-calling"
LABEL bioinfo.subcategory="variant-calling"

ENV BCFTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make gcc ca-certificates \
        libbz2-dev liblzma-dev libz-dev libncurses-dev libcurl4-openssl-dev libssl-dev && \
    cd /tmp/ && \
    git clone --branch ${BCFTOOLS_VERSION} https://github.com/samtools/bcftools.git && \
    git clone --branch ${HTSLIB_VERSION} https://github.com/samtools/htslib.git && \
    cd htslib && \
    git submodule update --init --recursive && \ 
    make && \
    make install && \
    cd ../bcftools && \
    make && \
    make install && \
    apt-get purge -y git make gcc ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["bcftools"]
```

