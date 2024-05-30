#!/bin/bash


if [ "$#" -ne 5 ]; then
    echo "Usage: $0 <sample_names_file> <input_fasta_file> <primer_bed_file> <gff_file> <samplesheet_file>"
    exit 1
fi

sample_names_file=$1
input_fasta_file=$2
primer_bed_file=$3
gff_file=$4
samplesheet_file=$5

# Step 1: Process the combined FASTA file
echo "Processing combined FASTA file..."
python helper_scripts/config_fasta.py "$input_fasta_file"
if [ $? -ne 0 ]; then
    echo "Error: Failed to process combined FASTA file."
    exit 1
fi

# Step 2: Process the BED file
echo "Processing BED file..."
python helper_scripts/config_primer.py "$sample_names_file" "$primer_bed_file"
if [ $? -ne 0 ]; then
    echo "Error: Failed to process BED file."
    exit 1
fi

# Step 3: Process the GFF file
echo "Processing GFF file..."
python helper_scripts/config_gff.py "$sample_names_file" "$gff_file"
if [ $? -ne 0 ]; then
    echo "Error: Failed to process GFF file."
    exit 1
fi

# Step 4: Process the samplesheet file
echo "Processing samplesheet file..."
python helper_scripts/config_samplesheet.py "$samplesheet_file"
if [ $? -ne 0 ]; then
    echo "Error: Failed to process samplesheet file."
    exit 1
fi


# Step 5: Create Nextflow scripts for each sample
echo "Creating Nextflow scripts..."
python helper_scripts/config_script.py "$sample_names_file"
if [ $? -ne 0 ]; then
    echo "Error: Failed to create Nextflow scripts."
    exit 1
fi

echo "Nextflow sample specific scirpts created successfully."
