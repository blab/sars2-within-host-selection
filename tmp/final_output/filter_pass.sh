input_file="$1"
base_name=$(basename "$input_file")
output_file="${PWD}/${base_name%.csv}_filtered.csv"


awk -F ',' 'NR == 1 || $6 == "PASS"' "$input_file" > "$output_file"

echo "Filtered file created: $output_file"