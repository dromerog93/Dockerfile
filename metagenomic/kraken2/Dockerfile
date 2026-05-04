FROM ubuntu:20.04
MAINTAINER Daniel Romero-Guzman
LABEL software=kraken2
ENV version=2.1.3
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y build-essential git
WORKDIR /usr/local/bin/git
RUN git clone https://github.com/DerrickWood/kraken2
RUN apt-get install -y zlib1g-dev
WORKDIR /usr/local/bin/git/kraken2
RUN ./install_kraken2.sh /usr/local/bin/git/kraken2
WORKDIR /usr/local/bin/
RUN ln -s /usr/local/bin/git/kraken2/kraken2 /usr/local/bin/kraken2
RUN ln -s /usr/local/bin/git/kraken2/kraken2-build /usr/local/bin/kraken2-build
RUN ln -s /usr/local/bin/git/kraken2/kraken2-inspect /usr/local/bin/kraken2-inspect
RUN echo "export PATH=$PATH:/usr/local/bin/kraken2-git" >> /root/.bashrc
RUN touch /root/.bashrc
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /home/
