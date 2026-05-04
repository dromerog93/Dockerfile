FROM ubuntu:20.04
MAINTAINER Daniel Romero-Guzman
LABEL software=TransDecoder
ENV version=5.7.0
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y build-essential automake git
WORKDIR /usr/local/bin/
RUN apt-get install -y zlib1g-dev libbz2-dev liblzma-dev pkg-config libtool libltdl-dev && git clone https://github.com/TransDecoder/TransDecoder.git && cd TransDecoder && make && make install
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /home/
