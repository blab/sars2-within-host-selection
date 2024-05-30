import os
import re
import sys
from Bio import SeqIO

def rename_sequences(input_file, output_file):
    """
    Process the input FASTA file, renaming each sequence header based on the given pattern,
    and save the modified sequences to an output FASTA file.

    Args:
        input_file (str): Path to the input FASTA file.
        output_file (str): Path to the output FASTA file.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('>'):
                match = re.search(r'>Consensus_([^\.]+)\.', line) # grabs the SAMPLE ID from >Consensus_SRX17852075.consensus_threshold_0.75_quality_20
                if match:
                    new_header = f">{match.group(1)}\n"
                    outfile.write(new_header)
                else:
                    outfile.write(line)
            else:
                outfile.write(line)

def split_fasta(input_file, output_folder):
    """
    Split the input FASTA file into individual FASTA files, each containing one sequence.

    Args:
        input_file (str): Path to the input FASTA file.
        output_folder (str): Path to the folder where the output FASTA files will be saved.
    """
    file_count = 0
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for record in SeqIO.parse(input_file, "fasta"):
        output_file = os.path.join(output_folder, f"{record.id}.consensus.fa")
        SeqIO.write(record, output_file, "fasta")
        file_count += 1
    
    print(f"Created {file_count} separate FASTA files in {output_folder}.")

def main(input_file):
    """
    Main function to process the input FASTA file by renaming sequences and splitting them
    into individual FASTA files.

    Args:
        input_file (str): Path to the input FASTA file.
    """
    output_folder = "nextflow_runs"
    intermediate_file = os.path.join(output_folder, f"renamed_{input_file}")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    rename_sequences(input_file, intermediate_file)
    split_fasta(intermediate_file, output_folder)
    print(f"Processed and split sequences from {input_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python combined_script.py <nextclade_alinged_fasta_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
