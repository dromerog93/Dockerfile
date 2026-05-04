FROM ubuntu:20.04
MAINTAINER Daniel Romero-Guzman
LABEL software=FAPROTAX
ENV version=1.2.7
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y && apt-get install -y build-essential wget unzip
WORKDIR /usr/local/bin/
RUN apt-get install -y python-dev pip && pip install numpy cython && pip install h5py biom-format==2.1.8.post1
RUN wget https://pages.uoregon.edu/slouca/LoucaLab/archive/FAPROTAX/SECTION_Download/MODULE_Downloads/CLASS_Latest%20release/UNIT_FAPROTAX_${version}/FAPROTAX_${version}.zip && unzip FAPROTAX_${version}.zip && rm FAPROTAX_${version}.zip && rm -r __MACOSX && mv FAPROTAX_${version}/* . && rm -r FAPROTAX_${version}
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
WORKDIR /home/
ENTRYPOINT ["/usr/local/bin/collapse_table.py"]
