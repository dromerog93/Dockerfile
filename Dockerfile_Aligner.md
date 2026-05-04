# Bioinformatics Tools

## Aligners

### general

#### BLAST+

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.16.0"
LABEL description="NCBI BLAST+ - Toolkit for nucleotide and protein sequence alignments"
LABEL source="https://blast.ncbi.nlm.nih.gov/Blast.cgi"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="general"

ENV BLAST_VERSION=2.16.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      wget ca-certificates \
      libgomp1 perl curl && \
    wget -O /tmp/ncbi-blast.tar.gz https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VERSION}/ncbi-blast-${BLAST_VERSION}+-x64-linux.tar.gz && \
    mkdir -p /opt/blast && \
    tar -xzf /tmp/ncbi-blast.tar.gz -C /opt/blast --strip-components=1 && \
    ln -s /opt/blast/bin/* /usr/local/bin/ && \
    apt-get purge -y wget ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["blastn"]
```

#### DIAMOND

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.1.11"
LABEL description="DIAMOND - Fast protein aligner for high-throughput sequencing data"
LABEL source="https://github.com/bbuchfink/diamond"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="general"

ENV DIAMOND_VERSION=2.1.11
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git ca-certificates make cmake g++ \ 
        zlib1g-dev perl && \
    git clone --branch=v${DIAMOND_VERSION} https://github.com/bbuchfink/diamond.git /tmp/diamond && \
    cd /tmp/diamond && \
    cmake -B build && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git ca-certificates make cmake g++ && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["diamond"]
```

#### MMseqs2

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="17-b804f"
LABEL description="MMseqs2 - Fast and sensitive protein sequence search and clustering suite"
LABEL source="https://github.com/soedinglab/MMseqs2"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="general"

ENV MMSEQS2_VERSION=17-b804f
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git ca-certificates make cmake g++ \ 
        zlib1g-dev libatomic1 libgomp1 && \
    git clone --branch ${MMSEQS2_VERSION} https://github.com/soedinglab/MMseqs2.git /tmp/mmseqs2 && \
    cd /tmp/mmseqs2 && \
    cmake -B build && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git ca-certificates make cmake g++ zlib1g-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["mmseqs"]
```

### long-read

#### GMAP_GSNAP

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2025-04-18"
LABEL description="GMAP - Genomic Mapping and Alignment Program for RNA-Seq long reads"
LABEL source="http://research-pub.gene.com/gmap/"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="long-read"

ENV GMAP_VERSION=2025-04-18
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      wget make g++ ca-certificates \
      zlib1g-dev perl && \
    wget -O /tmp/gmap.tar.gz http://research-pub.gene.com/gmap/src/gmap-gsnap-${GMAP_VERSION}.tar.gz && \
    tar -xzf /tmp/gmap.tar.gz -C /tmp/ && \
    cd /tmp/gmap-${GMAP_VERSION} && \
    ./configure --prefix=/usr/local && \
    make && \
    make install && \
    apt-get purge -y wget make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["gmap"]
```

#### minimap2

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.29"
LABEL description="Minimap2 - Versatile fast aligner for long DNA or RNA reads"
LABEL source="https://github.com/lh3/minimap2"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="long-read"

ENV MINIMAP2_VERSION=2.29
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      git make g++ ca-certificates \
      zlib1g-dev && \
    git clone --branch v${MINIMAP2_VERSION} https://github.com/lh3/minimap2.git /tmp/minimap2 && \
    cd /tmp/minimap2 && \
    make && \
    cp minimap2 /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["minimap2"]
```

### msa

#### MAFFT

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="7.525"
LABEL description="MAFFT - Multiple sequence alignment program based on fast Fourier transform"
LABEL source="https://mafft.cbrc.jp/alignment/software/"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="msa"

ENV MAFFT_VERSION=7.525
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl make g++ ca-certificates && \
    cd /tmp && \
    curl -L https://mafft.cbrc.jp/alignment/software/mafft-${MAFFT_VERSION}-without-extensions-src.tgz | tar zx && \
    cd mafft-${MAFFT_VERSION}-without-extensions/core && \
    make && \
    make install && \
    apt-get purge -y curl make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["mafft"]
```

#### MAFFT

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="7.525"
LABEL description="MAFFT - Multiple sequence alignment program based on fast Fourier transform"
LABEL source="https://mafft.cbrc.jp/alignment/software/"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="msa"

ENV MAFFT_VERSION=7.525
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl make g++ ca-certificates \
        perl ruby && \
    cd /tmp && \
    curl -L https://mafft.cbrc.jp/alignment/software/mafft-${MAFFT_VERSION}-with-extensions-src.tgz | tar zx && \
    cd mafft-${MAFFT_VERSION}-with-extensions/core && \
    make && \
    make install && \
    cd ../extensions && \
    make && \
    make install && \
    apt-get purge -y curl make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["mafft"]
```

#### MUSCLE

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="3.8.1551"
LABEL description="MUSCLE - High-accuracy multiple sequence aligner for protein and nucleotide sequences"
LABEL source="https://github.com/rcedgar/muscle"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="msa"

ENV MUSCLE_VERSION=3.8.1551
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        g++ make curl ca-certificates && \
    cd /tmp/ && \
    curl -L -o muscle_src.tar.gz https://www.drive5.com/muscle/muscle_src_${MUSCLE_VERSION}.tar.gz && \
    tar -xzf muscle_src.tar.gz && \
    make && \
    mv muscle /usr/local/bin/muscle && \
    apt-get purge -y g++ make curl ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["muscle"]
```

#### MUSCLE

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="5.3"
LABEL description="MUSCLE - High-accuracy multiple sequence aligner for protein and nucleotide sequences"
LABEL source="https://drive5.com/muscle5/manual/"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="msa"

ENV MUSCLE_VERSION=5.3
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    curl -L https://github.com/rcedgar/muscle/releases/download/v${MUSCLE_VERSION}/muscle-linux-x86.v${MUSCLE_VERSION} -o /usr/local/bin/muscle && \
    chmod +x /usr/local/bin/muscle && \
    apt-get purge -y curl ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["muscle"]
```

#### clustalo

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="1.2.4"
LABEL description="Clustal Omega - Fast and scalable multiple sequence alignment tool"
LABEL source="https://www.ebi.ac.uk/Tools/msa/clustalo/"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="msa"

ENV CLUSTALO_VERSION=1.2.4
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl ca-certificates make g++ autoconf automake libtool \
        libgomp1 libargtable2-dev && \
    cd /tmp/ && \
    curl -L http://www.clustal.org/omega/clustal-omega-${CLUSTALO_VERSION}.tar.gz | tar zx && \
    cd clustal-omega-${CLUSTALO_VERSION} && \
    ./configure && \
    make && \
    make install && \
    apt-get purge -y curl ca-certificates make g++ autoconf automake libtool && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["clustalo"]
```

### rna-aligner

#### HISAT2

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.2.1"
LABEL description="HISAT2 - Fast and sensitive spliced aligner for RNA-Seq data"
LABEL source="https://github.com/DaehwanKimLab/hisat2"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="rna-aligner"

ENV HISAT2_VERSION=2.2.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
   apt-get install -y --no-install-recommends \
       git make g++ ca-certificates \
       python-is-python3 zlib1g-dev python3-minimal && \
    git clone --branch v${HISAT2_VERSION} https://github.com/DaehwanKimLab/hisat2.git /tmp/hisat2 && \
    cd /tmp/hisat2 && \
    make && \
    cp hisat2 /usr/local/bin/ && \
    cp hisat2-* /usr/local/bin/ && \
    cp hisat2*.py /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["hisat2"]
```

#### HISAT2

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="HISAT2_2.2.1_samtools_1.21_bcftools_1.21"
LABEL description="HISAT2 + samtools + bcftools - RNA-Seq aligner with variant calling utilities"
LABEL source="https://github.com/DaehwanKimLab/hisat2, https://github.com/samtools/samtools, https://github.com/samtools/bcftools"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="rna-aligner"

ENV HISAT2_VERSION=2.2.1
ENV SAMTOOLS_VERSION=1.21
ENV BCFTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/local/bin:$PATH"

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        git build-essential ca-certificates \
        python-is-python3 zlib1g-dev python3-minimal \
        libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev && \
    # Install HISAT2
    git clone --branch v${HISAT2_VERSION} https://github.com/DaehwanKimLab/hisat2.git /tmp/hisat2 && \
    cd /tmp/hisat2 && \
    make && \
    cp hisat2 /usr/local/bin/ && \
    cp hisat2-* /usr/local/bin/ && \
    cp hisat2*.py /usr/local/bin/ && \
    # Install htslib (required for samtools/bcftools)
    git clone --branch ${HTSLIB_VERSION} https://github.com/samtools/htslib.git /tmp/htslib && \
    cd /tmp/htslib && \
    git submodule update --init --recursive && \ 
    make && \
    make install && \
    # Install samtools
    git clone --branch ${SAMTOOLS_VERSION} https://github.com/samtools/samtools.git /tmp/samtools && \
    cd /tmp/samtools && \
    make && \
    make install && \
    # Install bcftools
    git clone --branch ${BCFTOOLS_VERSION} https://github.com/samtools/bcftools.git /tmp/bcftools && \
    cd /tmp/bcftools && \
    make && \
    make install && \
    # Clean
    apt-get purge -y git build-essential ca-certificates vim-common && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["bash"]
```

#### STAR

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.7.11b"
LABEL description="STAR - Ultrafast spliced aligner for RNA-Seq data"
LABEL source="https://github.com/alexdobin/STAR"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="rna-aligner"

ENV STAR_VERSION=2.7.11b
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make g++ ca-certificates vim-common \
        zlib1g-dev libgomp1 && \
    git clone --branch ${STAR_VERSION} https://github.com/alexdobin/STAR.git /tmp/STAR && \
    cd /tmp/STAR/source && \
    make && \
    cp STAR /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates vim-common && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["STAR"]
```

#### STAR

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="STAR_2.7.11b_samtools_1.21_bcftools_1.21"
LABEL description="STAR + samtools + bcftools - RNA-Seq aligner with variant calling utilities"
LABEL source="https://github.com/alexdobin/STAR, https://github.com/samtools/samtools, https://github.com/samtools/bcftools"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="rna-aligner"

ENV STAR_VERSION=2.7.11b
ENV SAMTOOLS_VERSION=1.21
ENV BCFTOOLS_VERSION=1.21
ENV HTSLIB_VERSION=1.21
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/local/bin:$PATH"

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        git build-essential ca-certificates vim-common \
        zlib1g-dev libgomp1 \
        libbz2-dev liblzma-dev libncurses-dev libcurl4-openssl-dev libssl-dev && \
    # Install STAR
    git clone --branch ${STAR_VERSION} https://github.com/alexdobin/STAR.git /tmp/STAR && \
    cd /tmp/STAR/source && \
    make && \
    cp STAR /usr/local/bin/ && \
    # Install htslib (required for samtools/bcftools)
    git clone --branch ${HTSLIB_VERSION} https://github.com/samtools/htslib.git /tmp/htslib && \
    cd /tmp/htslib && \
    git submodule update --init --recursive && \ 
    make && \
    make install && \
    # Install samtools
    git clone --branch ${SAMTOOLS_VERSION} https://github.com/samtools/samtools.git /tmp/samtools && \
    cd /tmp/samtools && \
    make && \
    make install && \
    # Install bcftools
    git clone --branch ${BCFTOOLS_VERSION} https://github.com/samtools/bcftools.git /tmp/bcftools && \
    cd /tmp/bcftools && \
    make && \
    make install && \
    # Clean
    apt-get purge -y git build-essential ca-certificates vim-common && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["bash"]
```

### short-read

#### BBMap

```dockerfile
FROM openjdk:11-jre-slim

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="39.23"
LABEL description="BBMap - Ultra-fast, tolerant read aligner for short and long reads"
LABEL source="https://sourceforge.net/projects/bbmap/"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="short-read"

ENV BBMAP_VERSION=39.23
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      wget && \
    wget -O /tmp/bbmap.tar.gz https://sourceforge.net/projects/bbmap/files/BBMap_${BBMAP_VERSION}.tar.gz/download && \
    mkdir -p /opt/bbmap && \
    tar -xzf /tmp/bbmap.tar.gz -C /opt/bbmap --strip-components=1 && \
    ln -s /opt/bbmap/bbmap.sh /usr/local/bin/bbmap && \
    apt-get purge -y wget && \
    apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

ENV PATH="/opt/bbmap:$PATH"
WORKDIR /data

ENTRYPOINT ["bbmap"]
```

#### BWA

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="0.7.19"
LABEL description="BWA - Burrows-Wheeler Aligner for short read alignment"
LABEL source="https://github.com/lh3/bwa"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="short-read"

ENV BWA_VERSION=0.7.19
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      make gcc ca-certificates wget \
      zlib1g-dev && \
    wget -O /tmp/bwa-${BWA_VERSION}.tar.gz https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VERSION}.tar.gz && \
    tar -xzf /tmp/bwa-${BWA_VERSION}.tar.gz -C /tmp/ && \
    cd /tmp/bwa-${BWA_VERSION} && \
    make && \
    cp bwa /usr/local/bin/ && \
    apt-get purge -y wget make gcc ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["bwa"]
```

#### BWA-MEM2

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.2.1"
LABEL description="BWA-MEM2 - Fast reimplementation of BWA-MEM for short read alignment"
LABEL source="https://github.com/bwa-mem2/bwa-mem2"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="short-read"

ENV BWAMEM2_VERSION=2.2.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      wget bzip2 ca-certificates \
      zlib1g-dev && \
    wget -O /tmp/bwa-mem2.tar.bz2 https://github.com/bwa-mem2/bwa-mem2/releases/download/v${BWAMEM2_VERSION}/bwa-mem2-${BWAMEM2_VERSION}_x64-linux.tar.bz2 && \
    mkdir /tmp/bwa-mem2 && tar -xjf /tmp/bwa-mem2.tar.bz2 -C /tmp && \
    cp /tmp/bwa-mem2-${BWAMEM2_VERSION}_x64-linux/bwa-mem2* /usr/local/bin/ && \
    apt-get purge -y wget bzip2 ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT ["bwa-mem2"]
```

#### Bowtie2

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.5.4"
LABEL description="Bowtie2 - Fast and sensitive gapped read aligner for short reads (Burrows-Wheeler Aligner)"
LABEL source="https://github.com/BenLangmead/bowtie2"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="short-read"

ENV BOWTIE2_VERSION=2.5.4
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      git make g++ ca-certificates \
      perl python3 zlib1g-dev && \
    git clone --branch v${BOWTIE2_VERSION} https://github.com/BenLangmead/bowtie2.git /tmp/bowtie2 && \
    cd /tmp/bowtie2 && \
    make && \
    cp bowtie2* /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["bowtie2"]
```

#### Mosaik

```dockerfile
FROM ubuntu:22.04

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="2.2.30"
LABEL description="Mosaik - Sensitive and accurate aligner for both short and long reads"
LABEL source="https://github.com/wanpinglee/MOSAIK"
LABEL bioinfo.category="aligners"
LABEL bioinfo.subcategory="short-read"

ENV MOSAIK_VERSION=master
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git make g++ make ca-certificates \
        zlib1g-dev && \
    git clone https://github.com/wanpinglee/MOSAIK.git /tmp/MOSAIK && \
    cd /tmp/MOSAIK/src/ && \
    make && \
    cp /tmp/MOSAIK/bin/Mosaik* /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

ENTRYPOINT []
CMD ["MosaikAligner"]
```

