FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y build-essential git wget
RUN apt-get install -y python3
RUN apt-get install -y zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev
RUN apt-get install -y python3-pip && pip install biopython
WORKDIR /usr/local/bin/git
RUN git clone https://github.com/DerrickWood/kraken2
RUN git clone https://github.com/jenniferlu717/Bracken
RUN wget https://github.com/ablab/spades/releases/download/v4.0.0/SPAdes-4.0.0-Linux.tar.gz
RUN tar -xzf SPAdes-4.0.0-Linux.tar.gz
WORKDIR /usr/local/bin/git/kraken2
RUN ./install_kraken2.sh /usr/local/bin/git/kraken2
WORKDIR /usr/local/bin/git/Bracken
RUN ./install_bracken.sh /usr/local/bin/git/bracken
WORKDIR /usr/local/bin/
RUN mv /usr/local/bin/git/SPAdes-4.0.0-Linux/bin/* /usr/local/bin/
RUN mv /usr/local/bin/git/SPAdes-4.0.0-Linux/share/* /usr/local/share/
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/local/bin/git/kraken2/kraken2 /usr/local/bin/kraken2
RUN ln -s /usr/local/bin/git/kraken2/kraken2-build /usr/local/bin/kraken2-build
RUN ln -s /usr/local/bin/git/kraken2/kraken2-inspect /usr/local/bin/kraken2-inspect
RUN ln -s /usr/local/bin/git/Bracken/bracken /usr/local/bin/bracken
RUN ln -s /usr/local/bin/git/Bracken/bracken-build /usr/local/bin/bracken-build
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /home/
