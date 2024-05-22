import sys
import os

def process_gff(sample, gff_content):
    updated_content = gff_content.replace("MN908947.3", sample)
    return updated_content

def main():
    if len(sys.argv) != 3:
        print("Usage: python gff_parser.py <sample_names_file> <gff_file>")
        sys.exit(1)
    
    sample_file = sys.argv[1]  
    gff_file = sys.argv[2]  

    with open(gff_file, 'r') as file:
        gff_content = file.read()
    
    with open(sample_file, 'r') as file:
        samples = [line.strip() for line in file]
    
    for sample in samples:
        updated_content = process_gff(sample, gff_content)
        output_file = f"{sample}_GCA_009858895.3_ASM985889v3_genomic.200409.gff"
        with open(output_file, 'w') as file:
            file.write(updated_content)
        print(f"Created {output_file}")

if __name__ == "__main__":
    main()
