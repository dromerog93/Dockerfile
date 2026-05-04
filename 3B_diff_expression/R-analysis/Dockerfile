FROM rocker/r-ver:4.5.0

LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
LABEL version="4.5.0"
LABEL description="DESeq2, edgeR and limma - Differential expression analysis tools in R (Bioconductor)"
LABEL source="https://bioconductor.org/packages/3.21/, https://bioconductor.org/packages/release/bioc/html/DESeq2.html, https://bioconductor.org/packages/release/bioc/html/edgeR.html, https://www.bioconductor.org/packages/release/bioc/html/limma.html"
LABEL bioinfo.category="diff-expression"
LABEL bioinfo.subcategory="differential-analysis"

ENV DEBIAN_FRONTEND=noninteractive
ENV DESEQ2_VERSION=1.48.0
ENV EDGER_VERSION=4.6.2
ENV LIMMA_VERSION=3.64.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends zlib1g-dev && \
    Rscript -e "install.packages('BiocManager')" && \
    Rscript -e "BiocManager::install(version = '3.21')" && \
    Rscript -e "BiocManager::install(c('DESeq2', 'edgeR', 'limma'))" && \
    Rscript -e "stopifnot( \
        packageVersion('DESeq2') == Sys.getenv('DESEQ2_VERSION'), \
        packageVersion('edgeR') == Sys.getenv('EDGER_VERSION'), \
        packageVersion('limma') == Sys.getenv('LIMMA_VERSION'))" && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data

CMD ["Rscript"]

