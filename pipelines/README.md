## Overview

This code provides a set of pipelines optimized for High-Performance Computing (HPC) environments running the SLURM job scheduler, designed to identify intrahost Single Nucleotide Variats (iSNVs) from SRA reads. 

**Pipeline Execution**

The pipelines are executed using Nextflow and submitted to the HPC cluster using the `sbatch` command.

**Monitoring Pipelines**

Several options are available for monitoring pipeline execution and completion:

1.  **Direct Monitoring:**
    *   SSH into the head compute node and run `grabnode` to request an entire node.
    *   Use `tmux` to manage the session and directly run the bash script on the compute node.

2.  **SBATCH Monitoring:**
    *   After submitting the job with `sbatch`, run `tail -f nextflow.out` to review the Nextflow output in real-time.
    *   Include the `#SBATCH --mail-user=<email>` line in the job script to receive email notifications regarding job success or failure. 

## Pipeline specific overview

1. **Pipeline nf-core/fetchngs**
    * Submit job running `sbatch run_fetchNGS.sh`
    * Sample output
    ```
    data_fetchNGS/
    ├── custom
    │   └── user-settings.mkfg
    ├── fastq
    │   ├── SRX17852072_SRR21864254_1.fastq.gz
    │   ├── SRX17852072_SRR21864254_2.fastq.gz
    │   ├── SRX17852073_SRR21864253_1.fastq.gz
    │   └── SRX17852073_SRR21864253_2.fastq.gz
    ├── metadata
    │   ├── SRR21864253.runinfo_ftp.tsv
    │   └── SRR21864254.runinfo_ftp.tsv
    ├── pipeline_info
    │   ├── execution_report_2024-04-17_14-25-55.html
    │   ├── execution_timeline_2024-04-17_14-25-55.html
    │   ├── execution_trace_2024-04-17_14-25-55.txt
    │   ├── nf_core_fetchngs_software_mqc_versions.yml
    │   ├── params_2024-04-17_14-25-58.json
    │   └── pipeline_dag_2024-04-17_14-25-55.html
    └── samplesheet
        ├── id_mappings.csv
        ├── multiqc_config.yml
        └── samplesheet.csv
    ```

2. **Pipeline nf-core/viralrecon** 
    * Submit job running `sbatch run_viralRecon.sh`