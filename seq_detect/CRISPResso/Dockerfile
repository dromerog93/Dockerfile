FROM ubuntu:20.04
MAINTAINER Daniel Romero-Guzman
LABEL software=CRISPResso
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y && apt-get install -y build-essential
WORKDIR /usr/local/bin/
RUN apt-get install -y python3-virtualenv
RUN virtualenv crispr-venv && crispr-venv/bin/pip install --upgrade pip && crispr-venv/bin/pip install CRISPResso --no-use-wheel
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
WORKDIR /home/
ENTRYPOINT ["/usr/local/bin/cutadapt-venv/bin/cutadapt"]
