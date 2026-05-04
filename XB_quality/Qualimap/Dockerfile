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

