import os
import pandas as pd

def combine_variants_table(output_file):
    combined_df = pd.DataFrame()
    
    csv_files = []
    for root, dirs, files in os.walk('.'):
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
    output_file = 'combined_variants_long_table.csv'
    combine_variants_table(output_file)
