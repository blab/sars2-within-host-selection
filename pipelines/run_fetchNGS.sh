#!/bin/bash

# --- Job Info and Notifications ---
#// #SBATCH --job-name=<job_name>
#// #SBATCH --mail-type=END,FAIL
#// #SBATCH --mail-user=<email>

# --- Resource Requests (customize as needed) ---
#SBATCH --nodes=1
#SBATCH --ntasks=15
#SBATCH --cpus-per-task=1
#SBATCH --mem=20G
#SBATCH --time=1:00:00
#SBATCH --partition=campus-new  

# --- Input/Output and Logging ---
#SBATCH --output=nextflow.out
#SBATCH --error=nextflow.err

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

# --- Nextflow Execution  ---
nextflow run nf-core/fetchngs \
    -r 1.12.0 \
    -profile apptainer \
    --download_method sratools \
    --nf_core_pipeline viralrecon \
    --input ids.csv \
    --outdir data_fetchNGS/ \
    -resume 

echo "Job finished at $(date)"




