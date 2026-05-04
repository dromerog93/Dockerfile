FROM rust:1.87.0-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.6.0"
LABEL description="Polypolish - Illumina-based assembly polisher written in Rust"
LABEL source="https://github.com/rrwick/Polypolish"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="polishing"

ENV DEBIAN_FRONTEND=noninteractive
ENV POLYPOLISH_VERSION=0.6.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git ca-certificates samtools && \
    git clone --branch v${POLYPOLISH_VERSION} https://github.com/rrwick/Polypolish.git /tmp/Polypolish && \
    cd /tmp/Polypolish && \
    cargo build --release && \
    cp /tmp/Polypolish/target/release/polypolish /usr/local/bin/ && \
    apt-get purge -y git ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cargo/registry /root/.cargo/git

WORKDIR /data

ENTRYPOINT ["polypolish"]

