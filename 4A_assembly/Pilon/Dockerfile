FROM openjdk:11-jre-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.24"
LABEL description="Pilon - Assembly polishing tool using short reads (Illumina)"
LABEL source="https://github.com/broadinstitute/pilon"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="polishing"

ENV PILON_VERSION=1.24
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget ca-certificates && \
    wget https://github.com/broadinstitute/pilon/releases/download/v${PILON_VERSION}/pilon-${PILON_VERSION}.jar -O /opt/pilon.jar && \
    chmod +x /opt/pilon.jar && \
    apt-get purge -y wget ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["java", "-jar", "/opt/pilon.jar"]

