FROM ubuntu:20.04
MAINTAINER Daniel Romero-Guzman
LABEL software=get_homologues
ENV version=20230515
ENV DEBIAN_FRONTEND noninteractive
# Install wget, python, biopython and R
RUN apt-get update -y && apt-get install -y build-essential git wget
RUN apt-get install -y python3-dev python3-pip python3
RUN apt-get install -y r-base r-base-dev libgd-gd2-perl
RUN pip3 install numpy==1.24.4 biopython==1.70

WORKDIR /usr/local/bin/

# Install BLAST
RUN wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.14.1/ncbi-blast-2.14.1+-x64-linux.tar.gz && tar -xvzf ncbi-blast-2.14.1+-x64-linux.tar.gz
RUN mv ncbi-blast-2.14.1+/bin/* /usr/local/bin && rm -r ncbi-blast-2.14.1+ && rm ncbi-blast-2.14.1+-x64-linux.tar.gz

# Install DIAMOND
RUN wget https://github.com/bbuchfink/diamond/releases/download/v2.0.6/diamond-linux64.tar.gz && tar -xzvf diamond-linux64.tar.gz && rm diamond-linux64.tar.gz

# Install get_homologues
WORKDIR /usr/local/bin/
RUN git clone https://github.com/eead-csic-compbio/get_homologues.git
RUN yes | perl get_homologues/install.pl
RUN echo 'export GETHOMS=/usr/local/bin/get_homologues' >> ~/.bashrc && echo 'export PATH=${GETHOMS}/:${PATH}' >> ~/.bashrc

RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
WORKDIR /home/
