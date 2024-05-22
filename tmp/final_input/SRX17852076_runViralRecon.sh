#!/bin/bash

# --- Job Info and Notifications ---
#SBATCH --job-name=SRX17852076
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=covadiuc@uw.edu

# --- Resource Requests (customize as needed) ---
#SBATCH --nodes=1
#SBATCH --ntasks=15
#SBATCH --cpus-per-task=1
#SBATCH --mem=20G
#SBATCH --time=1:00:00
#SBATCH --partition=campus-new

# --- Input/Output and Logging ---
#SBATCH --output=logs/nextflow_SRX17852076.out
#SBATCH --error=logs/nextflow_SRX17852076.err

# --- Load SLURM Modules  ---
load_modules() {
  module purge
  local modules=(Apptainer/1.1.6 Nextflow/23.04.2 Java/17.0.6)
  for module in "${modules[@]}"; do
    module load "$module" || {
      echo "Error: Failed to load module '$module'!"
      exit 1
    }
  done
}

# --- Script Start ---
echo "Job started on $(hostname) at $(date)"
echo "Job ID: $SLURM_JOB_ID"
echo "Using $SLURM_CPUS_ON_NODE cores."
load_modules

# Viralrecon second run for consensus variant calling
nextflow run nf-core/viralrecon -r 2.6.0 \
--input SRX17852076_samplesheet.csv \
--outdir results/SRX17852076_runViralRecon \
--platform illumina \
--protocol amplicon \
--fasta SRX17852076.fasta \
--primer_bed SRX17852076_Artic_4.1.bed \
--gff SRX17852076_GCA_009858895.3_ASM985889v3_genomic.200409.gff \
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
