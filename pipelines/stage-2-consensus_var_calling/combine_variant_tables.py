import os
import sys
import pandas as pd
from datetime import datetime

def combine_variants_table(input_folder, output_file):
    combined_df = pd.DataFrame()
    
    csv_files = []
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file == 'variants_long_table.csv':
                csv_files.append(os.path.join(root, file))

    for i, csv_file in enumerate(csv_files):
        df = pd.read_csv(csv_file)
        if i == 0:
            combined_df = df
        else:
            combined_df = pd.concat([combined_df, df], ignore_index=True)
    
    combined_df.to_csv(output_file, index=False)
    print(f"Combined CSV saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python combine_variants_table.py <input_folder>")
        sys.exit(1)
    
    input_folder = sys.argv[1]

    if not os.path.isdir(input_folder):
        print(f"Error: {input_folder} is not a valid directory.")
        sys.exit(1)

    input_folder_name = os.path.basename(os.path.normpath(input_folder))
    current_date = datetime.now().strftime('%Y%m%d')
    output_file = f"combined_{input_folder_name}_{current_date}.csv"

    combine_variants_table(input_folder, output_file)
