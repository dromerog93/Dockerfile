FROM ubuntu:20.04
MAINTAINER Daniel Romero-Guzman
LABEL software=ncbi-genome-download
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y && apt-get install -y build-essential
WORKDIR /usr/local/bin/
RUN apt-get install -y python3-virtualenv
RUN virtualenv ncbi-venv && ncbi-venv/bin/pip install --upgrade pip && ncbi-venv/bin/pip install ncbi-genome-download
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
WORKDIR /home/
ENTRYPOINT ["/usr/local/bin/ncbi-venv/bin/ncbi-genome-download"]
