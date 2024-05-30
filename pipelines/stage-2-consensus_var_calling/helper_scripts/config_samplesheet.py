import os
import sys
import pandas as pd

def split_samplesheet(samplesheet_path):
    """
    Split the samplesheet.csv file into individual sample files and save them in a nextflow_runs/ folder.

    Args:
        samplesheet_path (str): Path to the samplesheet.csv file.
    """
    if not os.path.isfile(samplesheet_path):
        print(f"Error: {samplesheet_path} does not exist.")
        sys.exit(1)

    output_folder = os.path.join(os.path.dirname(samplesheet_path), 'nextflow_runs')

    try:
        samplesheet = pd.read_csv(samplesheet_path)
    except Exception as e:
        print(f"Error reading {samplesheet_path}: {e}")
        sys.exit(1)

    if 'sample' not in samplesheet.columns:
        print(f"Error: 'sample' column not found in {samplesheet_path}.")
        sys.exit(1)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for sample in samplesheet['sample'].unique():
        sample_data = samplesheet[samplesheet['sample'] == sample]
        sample_file = os.path.join(output_folder, f"{sample}_samplesheet.csv")
        
        try:
            sample_data.to_csv(sample_file, index=False)
            print(f"Created {sample_file}")
        except Exception as e:
            print(f"Error writing {sample_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split_samplesheet.py <samplesheet_path>")
        sys.exit(1)
    
    samplesheet_path = sys.argv[1]

    if not os.path.isfile(samplesheet_path):
        print(f"Error: {samplesheet_path} is not a valid file.")
        sys.exit(1)

    split_samplesheet(samplesheet_path)
