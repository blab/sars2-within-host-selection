#!/bin/bash

# Script to fetch SRA run numbers associated with a given BioProject ID from the NCBI database.
# It conditionally loads the QIIME2 module based on the presence of the SLURM scheduler to load esearch binary.
#
# Usage:
#   ./fetch_sra_runs.sh <BioProject ID> [output file name]
#
# Example:
#   ./fetch_sra_runs.sh PRJNA123456 sra_ids.csv
#
# Output:
#   The script outputs the SRA run numbers to the specified file name or 'sra_ids.csv' by default.

set -euo pipefail

# Check if the script is running on a system with SLURM and load the QIIME2 module
# This is because esearch is loaded from the QIIME2 module. 
## TODO: Fix so do not have to load QIIME2 to use esearch.
load_qiime2_module_if_on_slurm() {
    if command -v sbatch &> /dev/null; then
        echo "Detected SLURM environment, loading QIIME2 module..."
        module load QIIME2/2020.11
    else
        echo "Non-SLURM environment detected, skipping module load..."
    fi
}

# Function to fetch SRA run numbers for a given BioProject ID
fetch_sra_runs() {
    local bioproject_id=$1
    local output_file=${2:-"sra_ids.csv"}
    echo "Fetching SRA runs for BioProject ID: $bioproject_id"
    esearch -db sra -query "$bioproject_id" | efetch -format runinfo | tail -n +2 | cut -d "," -f 1 > "$output_file"
    echo "SRA run numbers have been successfully written to $output_file"
}

# Check if the correct number of arguments is provided
if [ "$#" -lt 1 ]; then
    echo "Usage Error: Incorrect number of arguments supplied."
    echo "Please provide a single BioProject ID as an argument."
    echo "If no output file name is provided, the default file name 'sra_ids.csv' will be used."
    echo "Usage: $0 <BioProject ID> [output csv file name]"
    exit 1
fi

# Load QIIME2 module if script is running in a SLURM HPC environment
load_qiime2_module_if_on_slurm

# Fetch SRA runs using the provided BioProject ID and optional output file name
fetch_sra_runs "$1" "${2:-}"

