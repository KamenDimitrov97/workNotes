import sys

sample = sys.argv[1]
bam = sys.argv[2]
summary = sys.argv[3]

# Simulating summary generation (replace with actual summary generation command)
with open(summary, 'w') as f:
    f.write(f"Summary for {sample}\n")
    f.write(f"Processed BAM file: {bam}\n")
