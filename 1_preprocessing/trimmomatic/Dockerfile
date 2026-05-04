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
