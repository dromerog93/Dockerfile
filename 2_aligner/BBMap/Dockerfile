FROM openjdk:11-jre-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="39.23"
LABEL description="BBMap - Ultra-fast, tolerant read aligner for short and long reads"
LABEL source="https://sourceforge.net/projects/bbmap/"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="short-read"

ENV BBMAP_VERSION=39.23
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      wget && \
    wget -O /tmp/bbmap.tar.gz https://sourceforge.net/projects/bbmap/files/BBMap_${BBMAP_VERSION}.tar.gz/download && \
    mkdir -p /opt/bbmap && \
    tar -xzf /tmp/bbmap.tar.gz -C /opt/bbmap --strip-components=1 && \
    ln -s /opt/bbmap/bbmap.sh /usr/local/bin/bbmap && \
    apt-get purge -y wget && \
    apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

ENV PATH="/opt/bbmap:$PATH"
WORKDIR /data

ENTRYPOINT ["bbmap"]
