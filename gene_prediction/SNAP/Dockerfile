FROM ubuntu:20.04
MAINTAINER Daniel Romero-Guzman
LABEL software=SNAP
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y build-essential automake git
WORKDIR /usr/local/bin/
RUN apt-get install -y zlib1g-dev libbz2-dev liblzma-dev pkg-config libtool libltdl-dev && git clone https://github.com/KorfLab/SNAP.git && mv SNAP SNAP_git && cd SNAP_git && make
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /home/
