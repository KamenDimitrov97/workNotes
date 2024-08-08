import sys

sample = sys.argv[1]
fastq1 = sys.argv[2]
fastq2 = sys.argv[3]
trimmed1 = sys.argv[4]
trimmed2 = sys.argv[5]

# Simulating read trimming (replace with actual trimming command)
with open(trimmed1, 'w') as f1, open(trimmed2, 'w') as f2:
    f1.write(f"Trimmed reads for {sample} R1\n")
    f2.write(f"Trimmed reads for {sample} R2\n")
