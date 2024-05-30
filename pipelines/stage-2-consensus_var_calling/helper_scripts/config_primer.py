import sys
import os

def read_sample_names(sample_file):
    """
    Read sample names from a file.

    Args:
        sample_file (str): Path to the file containing sample names.

    Returns:
        list: A list of sample names.
    """
    try:
        with open(sample_file, 'r') as file:
            samples = [line.strip() for line in file]
        return samples
    except IOError as e:
        print(f"Error reading sample file: {e}")
        sys.exit(1)

def process_bed_file(bed_file, samples, output_folder):
    """
    Process the BED file by replacing the chromosome name with each sample name
    and creating a new BED file for each sample.

    Args:
        bed_file (str): Path to the input BED file.
        samples (list): List of sample names.
        output_folder (str): Path to the folder where the output BED files will be saved.
    """
    try:
        with open(bed_file, 'r') as file:
            bed_lines = file.readlines()
    except IOError as e:
        print(f"Error reading BED file: {e}")
        sys.exit(1)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for sample in samples:
        output_file = os.path.join(output_folder, f"{sample}_Artic_4.1.bed")
        try:
            with open(output_file, 'w') as outfile:
                for line in bed_lines:
                    columns = line.strip().split('\t')
                    columns[0] = sample
                    outfile.write('\t'.join(columns) + '\n')
            print(f"Created {output_file}")
        except IOError as e:
            print(f"Error writing to {output_file}: {e}")
            continue

def main():
    """
    Main function to process the input sample names file and BED file.
    """
    if len(sys.argv) != 3:
        print("Usage: python process_bed.py <sample_names_file> <primer_bed_file>")
        sys.exit(1)

    sample_file = sys.argv[1]
    bed_file = sys.argv[2]

    output_folder = "nextflow_runs"
    samples = read_sample_names(sample_file)
    process_bed_file(bed_file, samples, output_folder)

if __name__ == "__main__":
    main()
