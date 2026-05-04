FROM condaforge/miniforge3:latest
MAINTAINER Daniel Romero-Guzman
LABEL software=PICRUSt2
ENV version=2.5.2
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /usr/local/bin/
RUN mamba create -n picrust2 -c bioconda -c conda-forge picrust2=2.5.2
RUN echo -e "\nconda activate picrust2" >> ~/.bashrc
WORKDIR /home/
