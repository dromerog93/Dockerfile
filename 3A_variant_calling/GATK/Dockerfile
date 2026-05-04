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

