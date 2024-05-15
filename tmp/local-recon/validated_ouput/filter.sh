#!/bin/bash

# filter TSV files in PWD that PASS pval 

for file in "$PWD"/*.tsv; 
do
  base_name=$(basename "$file")
  output_file="$PWD/filtered_$base_name"
  awk -F '\t' 'NR == 1 || $14 == "TRUE"' "$file" > "$output_file"
  echo "Filtered file created: $output_file"
done
