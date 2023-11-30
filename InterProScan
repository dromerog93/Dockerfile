FROM ubuntu:20.04
MAINTAINER Daniel Romero-Guzman
LABEL software=InterProScan
ENV version=5.63-95.0
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y && apt-get install -y build-essential wget
RUN apt-get install -y python3-dev python3-pip python3
RUN apt-get install -y default-jre
WORKDIR /usr/local/bin/
RUN wget https://ftp.ebi.ac.uk/pub/software/unix/iprscan/5/5.63-95.0/interproscan-5.63-95.0-64-bit.tar.gz && tar -pxvzf interproscan-5.63-95.0-64-bit.tar.gz
RUN cd interproscan-5.63-95.0/ && python3 setup.py -f interproscan.properties
RUN ln -s /usr/local/bin/interproscan-5.63-95.0/interproscan.sh /usr/local/bin/interproscan
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
WORKDIR /home/
