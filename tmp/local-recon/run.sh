#!/bin/bash

# --- Define ref genome and primer BED ( Note: example here uses Artic V4.1 primer bed) --- 

# --- Wuhan variant calling ---
# REFERENCE_GENOME="nCoV-2019.reference.fasta"
# PRIMER_BED="SARS-CoV-2.scheme.bed"

# --- Consensus variant calling ---
REFERENCE_GENOME="consensus.reference.fasta"
PRIMER_BED="modified_SARS-CoV-2.scheme.bed"


# --- Script start ---

mkdir bowtie2

# make Bowtie2 index
bowtie2-build --seed 1 --threads 12 "$REFERENCE_GENOME" bowtie2/nCoV-2019.reference

# cerate FASTA index and size file
samtools faidx "$REFERENCE_GENOME"
cut -f 1,2 "$REFERENCE_GENOME".fai > "$REFERENCE_GENOME".sizes


[ ! -f SRX17852076_1.fastq.gz ] && ln -sf SRX17852076_SRR21864250_1.fastq.gz SRX17852076_1.fastq.gz
[ ! -f SRX17852076_2.fastq.gz ] && ln -sf SRX17852076_SRR21864250_2.fastq.gz SRX17852076_2.fastq.gz


fastp \
    --in1 SRX17852076_1.fastq.gz \
    --in2 SRX17852076_2.fastq.gz \
    --out1 SRX17852076_1.fastp.fastq.gz \
    --out2 SRX17852076_2.fastp.fastq.gz \
    --json SRX17852076.fastp.json \
    --html SRX17852076.fastp.html \
    --thread 6 \
    --detect_adapter_for_pe \
    --cut_front \
    --cut_tail \
    --trim_poly_x \
    --cut_mean_quality 30 \
    --qualified_quality_phred 30 \
    --unqualified_percent_limit 10 \
    --length_required 50 \
    2> SRX17852076.fastp.log


INDEX=`find -L ./ -name "*.rev.1.bt2" | sed "s/\.rev.1.bt2$//"`
[ -z "$INDEX" ] && INDEX=`find -L ./ -name "*.rev.1.bt2l" | sed "s/\.rev.1.bt2l$//"`

# check index files 
[ -z "$INDEX" ] && echo "Bowtie2 index files not found" 1>&2 && exit 1

# run Bowtie2 
bowtie2 \
    -x "$INDEX" \
    -1 SRX17852076_1.fastp.fastq.gz -2 SRX17852076_2.fastp.fastq.gz \
    --threads 12 \
    --local --very-sensitive-local --seed 1 \
    2> SRX17852076.bowtie2.log \
    | samtools view -F4 -bhS --threads 12 -o SRX17852076.bam -

# ?unmapped reads
if [ -f SRX17852076.unmapped.fastq.1.gz ]; then
    mv SRX17852076.unmapped.fastq.1.gz SRX17852076.unmapped_1.fastq.gz
fi
if [ -f SRX17852076.unmapped.fastq.2.gz ]; then
    mv SRX17852076.unmapped.fastq.2.gz SRX17852076.unmapped_2.fastq.gz
fi

# sort and index BAM file
samtools sort -@ 6 -o SRX17852076.sorted.bam -T SRX17852076.sorted SRX17852076.bam
samtools index -@ 1 SRX17852076.sorted.bam

# trim primers w/ ivar
ivar trim \
    -m 30 -q 20 -e \
    -i SRX17852076.sorted.bam \
    -b "$PRIMER_BED" \
    -p SRX17852076.ivar_trim \
    > SRX17852076.ivar_trim.ivar.log

# sort and index trimmed BAM file
samtools sort -@ 6 -o SRX17852076.ivar_trim.sorted.bam -T SRX17852076.ivar_trim.sorted SRX17852076.ivar_trim.bam 
samtools index -@ 1 SRX17852076.ivar_trim.sorted.bam 

# call variants w/ ivar
samtools mpileup \
    --ignore-overlaps --count-orphans --no-BAQ --max-depth 0 --min-BQ 0 \
    --reference "$REFERENCE_GENOME" \
    SRX17852076.ivar_trim.sorted.bam \
    | ivar variants \
    -t 0.01 -q 20 -m 10 \
    -g GCA_009858895.3_ASM985889v3_genomic.200409.gff \
    -r "$REFERENCE_GENOME" \
    -p SRX17852076 

# filter variants PASS == TRUE only 
awk -F '\t' 'NR == 1 || $14 == "TRUE"' SRX17852076.tsv > filtered_SRX17852076.tsv
