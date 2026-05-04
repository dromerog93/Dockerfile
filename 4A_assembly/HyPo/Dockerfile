FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.0.3"
LABEL description="HyPo - Fast and accurate genome polishing tool using long and/or short reads"
LABEL source="https://github.com/kensung-lab/hypo"
LABEL bioinfo.category="assembly"
LABEL bioinfo.subcategory="polishing"

ENV HYPO_VERSION=1.0.3
ENV KMC_VERSION=3.2.4
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git cmake make g++ ca-certificates python3-dev \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev \
        libcurl4-openssl-dev libgomp1 && \
    git clone --branch v${KMC_VERSION} --recurse-submodules https://github.com/refresh-bio/kmc.git /tmp/kmc && \
    cd /tmp/kmc && \
    make && \
    cp /tmp/kmc/bin/* /usr/local/bin/ && \
    git clone --branch v${HYPO_VERSION} --recursive https://github.com/kensung-lab/hypo.git /opt/hypo && \
    cd /opt/hypo && \
    chmod +x /opt/hypo/install_deps.sh && \
    ./install_deps.sh && \
    sed -i '/#include <chrono>/a #include <string>' /opt/hypo/external/suk/external/slog/include/slog/Monitor.hpp && \
    cp external/install/htslib/libhts.so external/install/htslib/lib/libhts.so && \
    cp external/install/htslib/libhts.a external/install/htslib/lib/libhts.a && \
    cp external/install/htslib/libhts.so.2to3part11 external/install/htslib/lib/libhts.so.2to3part11 && \
    export LD_LIBRARY_PATH=/opt/hypo/external/install/htslib:$LD_LIBRARY_PATH && \
    cmake -B build -DCMAKE_BUILD_TYPE=Release -Doptimise_for_native=ON && \
    cmake --build build && \
    cmake --install build && \
    apt-get purge -y git cmake make g++ ca-certificates python3-dev \
        zlib1g-dev libbz2-dev liblzma-dev libncurses-dev libssl-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /opt/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["hypo"]

