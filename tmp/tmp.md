## TMP Project: Analysis of SARS-CoV-2 SRA Reads (BIOPROJECT PRJNA889424)

This project analyzes SARS-CoV-2 sequencing reads from the BIOPROJECT PRJNA889424 dataset. The analysis pipeline utilizes nf-core/viralrecon and nf-core/fetchngs tools, resulting in two primary output TSV files:

**1. iSNV TSV Table (nf-core/viralrecon output):**

| Column     | Description                                                                |
|------------|----------------------------------------------------------------------------|
| SAMPLE     | Unique identifier for the sample                                           |
| CHROM      | Reference chromosome or sequence ID                                       |
| POS        | Position of the variant in the reference sequence                         |
| REF        | Reference base(s)                                                         |
| ALT        | Alternate base(s) observed                                                 |
| FILTER     | Quality filter status                                                     |
| DP         | Total read depth at the position                                            |
| REF_DP     | Read depth of the reference allele                                         |
| ALT_DP     | Read depth of the alternate allele                                         |
| AF         | Allele frequency of the variant                                           |
| GENE       | The gene affected by the variant, if applicable                             |
| EFFECT     | The predicted effect of the variant on the gene                            |
| HGVS_C     | HGVS nomenclature for nucleotide changes                                  |
| HGVS_P     | HGVS nomenclature for protein changes (if nonsynonymous)                    |
| HGVS_P_1LETTER | Single-letter amino acid changes                                         |
| CALLER     | The variant calling software used                                         |
| LINEAGE    | The lineage of the viral strain, if known                                  |

**Example Data:**

| SAMPLE       | CHROM      | POS     | REF | ALT | FILTER | DP   | REF_DP | ALT_DP | AF   | GENE     | EFFECT                | HGVS_C       | HGVS_P           | HGVS_P_1LETTER | CALLER | LINEAGE |
|--------------|-------------|---------|-----|-----|--------|------|--------|--------|------|-----------|-----------------------|--------------|-------------------|-----------------|--------|---------|
| SRX17852125 | MN908947.3 | 28271  | A   | C   | PASS   | 14   | 10     | 4      | 0.29 | N        | upstream_gene_variant | c.-3A>C     | .                 | .               | ivar   | B.1.1.7 |
| SRX17852126 | MN908947.3 | 11083  | G   | T   | PASS   | 1109 | 143    | 966    | 0.87 | orf1ab   | missense_variant     | c.10818G>T  | p.Leu3606Phe     | p.L3606F       | ivar   | B.1.1   |

**2. SRA Metadata TSV Table (nf-core/fetchngs output):**

| Column                      | Description                                                                                                                                   |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| sample                      | Sample identifier                                                                                                                             |
| fastq_1                     | Path to the first FASTQ file                                                                                                                  |
| fastq_2                     | Path to the second FASTQ file (if paired-end sequencing)                                                                                     |
| run_accession               | Run accession number                                                                                                                          |
| experiment_accession        | Experiment accession number                                                                                                                     |
| sample_accession            | Sample accession number                                                                                                                         |
| secondary_sample_accession | Secondary sample accession number                                                                                                                |
| study_accession             | Study accession number                                                                                                                          |
| secondary_study_accession  | Secondary study accession number                                                                                                                |
| submission_accession       | Submission accession number                                                                                                                    |
| run_alias                  | Run alias                                                                                                                                     |
| experiment_alias            | Experiment alias                                                                                                                                |
| sample_alias                | Sample alias                                                                                                                                  |
| study_alias                 | Study alias                                                                                                                                   |
| library_layout              | Library layout (e.g., PAIRED, SINGLE)                                                                                                          |
| library_selection           | Library selection method (e.g., RT-PCR)                                                                                                       |
| library_source              | Library source material (e.g., VIRAL RNA)                                                                                                    |
| library_strategy            | Library strategy (e.g., WGS)                                                                                                                   |
| library_name                | Library name                                                                                                                                   |
| instrument_model            | Instrument model used for sequencing                                                                                                           |
| instrument_platform         | Sequencing platform                                                                                                                            |
| base_count                  | Total number of bases sequenced                                                                                                                |
| read_count                  | Total number of reads sequenced                                                                                                                 |
| tax_id                      | NCBI Taxonomy ID                                                                                                                                |
| scientific_name            | Scientific name of the organism                                                                                                               |
| sample_title                | Sample title                                                                                                                                   |
| experiment_title            | Experiment title                                                                                                                                |
| study_title                 | Study title                                                                                                                                   |
| sample_description          | Sample description                                                                                                                               |
| fastq_md5                  | MD5 checksums of the FASTQ files                                                                                                              |
| fastq_bytes                 | Size of the FASTQ files in bytes                                                                                                              |
| fastq_ftp                   | FTP download links for the FASTQ files                                                                                                          |
| fastq_galaxy                | Galaxy download links for the FASTQ files                                                                                                         |
| fastq_aspera                | Aspera download links for the FASTQ files                                                                                                         |

