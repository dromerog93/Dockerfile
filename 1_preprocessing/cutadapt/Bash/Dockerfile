FROM ubuntu:20.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="5.0"
LABEL description="Cutadapt 5.0 - Adapter trimming tool for FASTQ files."
LABEL source="https://cutadapt.readthedocs.io"
LABEL bioinfo.category="preprocessing"

ENV CUTADAPT_VERSION=5.0
ENV PIP_NO_CACHE_DIR=1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && apt-get install -y build-essential
WORKDIR /usr/local/bin/
RUN apt-get install -y python3-virtualenv
RUN virtualenv cutadapt-venv && cutadapt-venv/bin/pip install --upgrade pip && cutadapt-venv/bin/pip install cutadapt
RUN ln -s /usr/local/bin/cutadapt-venv/bin/cutadapt /usr/local/bin/
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
WORKDIR /home/
