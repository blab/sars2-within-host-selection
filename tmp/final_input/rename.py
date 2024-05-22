import re
import sys

def process_fasta(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('>'):
                # regex to match and extract the SRX number
                match = re.search(r'>Consensus_(SRX[0-9]+)\.consensus_threshold_0\.75_quality_20', line)
                if match:
                    new_header = f">{match.group(1)}\n"
                    outfile.write(new_header)
                else:
                    outfile.write(line)
            else:
                outfile.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_fasta.py <input_fasta_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = f"output_{input_file}"
    process_fasta(input_file, output_file)
    print(f"Processed file saved as {output_file}")
