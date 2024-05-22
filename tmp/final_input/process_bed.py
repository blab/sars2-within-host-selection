import sys

def read_sample_names(sample_file):
    with open(sample_file, 'r') as file:
        samples = [line.strip() for line in file]
    return samples

def process_bed_file(bed_file, samples):
    with open(bed_file, 'r') as file:
        bed_lines = file.readlines()
    
    for sample in samples:
        output_file = f"{sample}_Artic_4.1.bed"
        with open(output_file, 'w') as outfile:
            for line in bed_lines:
                columns = line.strip().split('\t')
                columns[0] = sample
                outfile.write('\t'.join(columns) + '\n')
        print(f"Created {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_bed.py <sample_names_file> <primer_bed_file>")
        sys.exit(1)

    sample_file = sys.argv[1]
    bed_file = sys.argv[2]

    samples = read_sample_names(sample_file)
    process_bed_file(bed_file, samples)
