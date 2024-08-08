import sys

sample = sys.argv[1]
fastq1 = sys.argv[2]
fastq2 = sys.argv[3]
output = sys.argv[4]

# Simulating QC (replace with actual QC command)
with open(output, 'w') as f:
    f.write(f"Quality control report for {sample}\n")
    f.write(f"Processed {fastq1} and {fastq2}\n")
