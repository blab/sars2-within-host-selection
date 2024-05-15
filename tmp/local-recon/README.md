# Pipeline Execution Overview

Local pipeline using info from nextflow command.sh from nf-core/viralrecon.

Overall this results in the exact same variant files as the output from viral recon. 

In order to run viralrecon a second time and get the same variant files use command below which resutls in a much shorter run time of 3min compared to ~30min for the initial run which includes all QC. The second run also can use the GFF annotation to get a variant-long-table with mutation annotations:


```bash
# Viralrecon second run for consensus variant calling
nextflow run nf-core/viralrecon -r 2.6.0 \
--input data_fetchNGS/samplesheet/samplesheet.csv \
--outdir results/3_data_viralrecon \
--platform illumina \
--protocol amplicon \
--fasta SRX17852076_consensus.fa \
--primer_bed modified_nCoV-2019.primer.bed \
--gff GCA_009858895.3_ASM985889v3_genomic.200409.gff \
--variant_caller ivar \
--skip_fastqc \
--skip_kraken2 \
--skip_cutadapt \
--skip_assembly \
--skip_nextclade \
--skip_multiqc \
--skip_consensus \
--skip_asciigenome \
-c custom.config \
-profile gizmo
```


### Steps:

>First run `conda env create -f recon-local.yml` to create conda env. 

1. **Variant Calling Against the Wuhan Reference Genome:**
   - **Input Files:** `nCoV-2019.reference.fasta` and `SARS-CoV-2.scheme.bed`
   - This step utilizes the viralrecon project's defaults for processing.
   - To view the first two entries of the Wuhan reference primer file, use:
     ```
     head -2 nCoV-2019.primer.bed
     ```
   - Example output:
     ```
     MN908947.3	25	50	SARS-CoV-2_1_LEFT	1	+
     MN908947.3	324	344	SARS-CoV-2_2_LEFT	2	+ 
     ```

2. **Variant Calling Against the Consensus Sequence:**
   - **Input File:** `consensus.reference.fasta`
   - The consensus sequence is generated using iVar. To view the header of the consensus sequence file, use the command:
     ```
     head -1 consensus.reference.fasta
     ```
   - Example output:
     ```
     >SRX17852108
     ```
   - **BED File:** A custom BED file is used for name matching: `modified_SARS-CoV-2.scheme.bed`
   - To inspect the first two entries of the BED file, use:
     ```
     head -2 custom_nCoV-2019.primer.bed
     ```
   - Example output:
     ```
     SRX17852108	25	50	SARS-CoV-2_1_LEFT	1	+
     SRX17852108	324	344	SARS-CoV-2_2_LEFT	2	+
     ```

To replace name col in the BED Primer file ```awk `BEGIN{FS=OFS="\t"} {$1="<string>"} 1` <file>.bed > <file2>.bed```

