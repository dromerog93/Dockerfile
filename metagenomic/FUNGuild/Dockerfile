FROM ubuntu:20.04
MAINTAINER Daniel Romero-Guzman
LABEL software=FUNGuild
ENV version=1.1
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y && apt-get install -y build-essential git
WORKDIR /usr/local/bin/
RUN apt-get install -y python-dev pip && pip install requests
RUN git clone https://github.com/UMNFuN/FUNGuild/ && cp FUNGuild/Guilds_v${version}.py /usr/local/bin/
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
WORKDIR /home/
ENTRYPOINT ["python3", "/usr/local/bin/Guilds_v1.1.py"]
