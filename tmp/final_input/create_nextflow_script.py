import sys

def create_nextflow_script(sample):
    script_content = f"""#!/bin/bash

# --- Job Info and Notifications ---
#SBATCH --job-name={sample}
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
#SBATCH --output=logs/nextflow_{sample}.out
#SBATCH --error=logs/nextflow_{sample}.err

# --- Load SLURM Modules  ---
load_modules() {{
  module purge
  local modules=(Apptainer/1.1.6 Nextflow/23.04.2 Java/17.0.6)
  for module in "${{modules[@]}}"; do
    module load "$module" || {{
      echo "Error: Failed to load module '$module'!"
      exit 1
    }}
  done
}}

# --- Script Start ---
echo "Job started on $(hostname) at $(date)"
echo "Job ID: $SLURM_JOB_ID"
echo "Using $SLURM_CPUS_ON_NODE cores."
load_modules

# Viralrecon second run for consensus variant calling
nextflow run nf-core/viralrecon -r 2.6.0 \\
--input {sample}_samplesheet.csv \\
--outdir results/{sample}_runViralRecon \\
--platform illumina \\
--protocol amplicon \\
--fasta {sample}.fasta \\
--primer_bed {sample}_Artic_4.1.bed \\
--gff {sample}_GCA_009858895.3_ASM985889v3_genomic.200409.gff \\
--variant_caller ivar \\
--skip_fastqc \\
--skip_kraken2 \\
--skip_cutadapt \\
--skip_assembly \\
--skip_nextclade \\
--skip_multiqc \\
--skip_consensus \\
--skip_asciigenome \\
-c custom.config \\
-profile gizmo
"""

    script_filename = f"{sample}_runViralRecon.sh"
    with open(script_filename, 'w') as script_file:
        script_file.write(script_content)
    print(f"Created {script_filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python create_nextflow_scripts.py <sample_names_file>")
        sys.exit(1)
    
    sample_file = sys.argv[1]


    with open(sample_file, 'r') as file:
        samples = [line.strip() for line in file]
    
   
    for sample in samples:
        create_nextflow_script(sample)

if __name__ == "__main__":
    main()
