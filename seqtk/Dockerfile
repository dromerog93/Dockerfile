FROM ubuntu:20.04
MAINTAINER Daniel Romero-Guzman
LABEL software=seqtk
ENV version=1.3
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y build-essential automake git
WORKDIR /usr/local/bin/
RUN apt-get install -y zlib1g-dev libbz2-dev liblzma-dev pkg-config libtool libltdl-dev && git clone https://github.com/lh3/seqtk.git && mv seqtk seqtk_git && cd seqtk_git && make && make install
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /home/
