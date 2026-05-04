FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="4.3.7"
LABEL description="SortMeRNA - rRNA filtering tool for metatranscriptomics and RNA-seq"
LABEL source="https://github.com/biocore/sortmerna"
LABEL bioinfo.category="preprocessing"
LABEL bioinfo.subcategory="rRNA-filtering"

ENV SORTMERNA_VERSION=4.3.7
ENV ROCKSDB_VERSION=9.1.1
ENV DEBIAN_FRONTEND=noninteractive
ENV LD_LIBRARY_PATH=/usr/local/lib

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git cmake make g++ ca-certificates \ 
        zlib1g-dev && \
    git clone --branch v${ROCKSDB_VERSION} https://github.com/facebook/rocksdb.git /tmp/rocksdb && \
    cd /tmp/rocksdb && \
    cmake -B build -DCMAKE_BUILD_TYPE=Release \
        -DWITH_TESTS=OFF -DWITH_TOOLS=OFF -DWITH_GFLAGS=OFF \
        -DWITH_ZLIB=ON && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    echo "/usr/local/lib" > /etc/ld.so.conf.d/rocksdb.conf && \
    ldconfig && \
    git clone --branch v${SORTMERNA_VERSION} https://github.com/biocore/sortmerna.git /tmp/sortmerna && \
    git clone https://github.com/cameron314/concurrentqueue.git /tmp/concurrentqueue && \
    cp /tmp/concurrentqueue/concurrentqueue.h /tmp/sortmerna/include/ && \
    cd /tmp/sortmerna && \ 
    cmake -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-include stdint.h" && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git cmake g++ zlib1g-dev ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["sortmerna"]

