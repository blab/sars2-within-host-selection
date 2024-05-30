import sys
import os

def process_gff(sample, gff_content):
    """
    Replace the placeholder in the GFF content with the sample name.

    Args:
        sample (str): The sample name to replace the placeholder.
        gff_content (str): The content of the GFF file.

    Returns:
        str: The updated GFF content.
    """
    return gff_content.replace("MN908947.3", sample)

def read_samples(sample_file):
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

def read_gff(gff_file):
    """
    Read the content of a GFF file.

    Args:
        gff_file (str): Path to the GFF file.

    Returns:
        str: The content of the GFF file.
    """
    try:
        with open(gff_file, 'r') as file:
            return file.read()
    except IOError as e:
        print(f"Error reading GFF file: {e}")
        sys.exit(1)

def write_gff(output_file, content):
    """
    Write the content to a GFF file.

    Args:
        output_file (str): Path to the output GFF file.
        content (str): The content to write to the file.
    """
    try:
        with open(output_file, 'w') as file:
            file.write(content)
        print(f"Created {output_file}")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}")

def main():
    """
    Main function to process the input sample names file and GFF file.
    """
    if len(sys.argv) != 3:
        print("Usage: python gff_parser.py <sample_names_file> <gff_file>")
        sys.exit(1)

    sample_file = sys.argv[1]
    gff_file = sys.argv[2]

    output_folder = "nextflow_runs"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    samples = read_samples(sample_file)
    gff_content = read_gff(gff_file)

    for sample in samples:
        updated_content = process_gff(sample, gff_content)
        output_file = os.path.join(output_folder, f"{sample}_GCA_009858895.3_ASM985889v3_genomic.200409.gff")
        write_gff(output_file, updated_content)

if __name__ == "__main__":
    main()
