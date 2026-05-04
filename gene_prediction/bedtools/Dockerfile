FROM ubuntu:20.04
MAINTAINER Daniel Romero-Guzman
LABEL software=bedtools
LABEL GIT=https://github.com/arq5x/bedtools2
ENV version=2.31.0
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y build-essential wget
WORKDIR /usr/local/bin/
RUN apt-get install -y python zlib1g-dev libncurses5-dev libncursesw5-dev libbz2-dev liblzma-dev && wget https://github.com/arq5x/bedtools2/releases/download/v${version}/bedtools-${version}.tar.gz && tar -zxvf bedtools-${version}.tar.gz && cd bedtools2 && make && make install
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 
RUN apt-get remove -y build-essential wget
WORKDIR /home/
ENTRYPOINT ["bedtools"]
