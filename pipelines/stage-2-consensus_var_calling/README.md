## Stage 2 - Consensus Variant Calling 

>NOTE: This is the first pass - there is lots of room for improvement from including args to snakemake/nextflow, etc.


Here we use the SARS-COV_2 consensus genomes for each sample from the previous analysis to create a modified variant calling analysis using each sample's own consensus genomes instead of the Wuhan reference genome.


In order to use each samples consensus fasta sequnces, we need to modify input files for nextflow/viralrecon where each input file needs to maatch the sample name. For example:

1. Sample fasta seuqneces header >
2. Primer BED file 
3. GFF annotation file - 


Run config_runs.sh passng in sample_names.txt , 