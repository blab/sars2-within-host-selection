from Bio import SeqIO
import sys

def split_fasta(input_file):
    file_count = 0
    for record in SeqIO.parse(input_file, "fasta"):
        output_file = f"{record.id}.fasta"
        SeqIO.write(record, output_file, "fasta")
        file_count += 1
    
    print(f"Created {file_count} separate FASTA files.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split_fasta.py <input_fasta_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    split_fasta(input_file)
