FROM ubuntu:20.04
MAINTAINER Daniel Romero-Guzman
LABEL software=Circos
ENV version=0.69.9
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y build-essential wget pkg-config
WORKDIR /usr/local/bin/
RUN apt-get install -y libjpeg-dev libpng-dev libfreetype-dev libgd-perl
RUN cpan install YAML && cpan install ExtUtils::PkgConfig Config::General Readonly Font::TTF::Font Text::Format Clone List::MoreUtils Math::Bezier Math::Round Math::VecStat Params::Validate Regexp::Common SVF Set::IntSpan Statistics::Basic SVG
RUN wget http://circos.ca/distribution/circos-0.69-9.tgz && tar xvfz circos-0.69-9.tgz && ln -s /usr/local/bin/circos-0.69-9/bin/circos /usr/local/bin/
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /home/
