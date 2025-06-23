# Use Cases: 
# 1. Finding conserved regions in DNA
# 2. Designing primers for PCR
# 3. Building multiple sequence alignments
# 4. Estimating evolutionary relationships.


# PARSE FASTA FILE AND STORE IN DICTIONARY

def readFile(filepath):
    """Reading a file and returning a list of lines"""
    with open(filepath, 'r') as f:
        return[l.strip() for l in f.readlines()]

filepath = "test file\consensus and profile.txt"
# ===Read data fromthe file(FASTA formatted file)
# Storing File contents in a list
FASTAFile = readFile(filepath)
# Dictionary for Labels + Data
FASTADict = {}
# String for holding the current label
FASTALabel = ""

for line in FASTAFile:
    line = line.strip()

    if line.startswith('>'):
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    elif FASTALabel:
       FASTADict[FASTALabel] += line

print(FASTADict)

# Extracting sequences from the FASTA dictionary
sequences = list(FASTADict.values())
n = len(sequences[0])

# Initialize a list to hold the counts of A, C, G, T for each position
profile = {
    'A': [0] * n,
    'C': [0] * n,
    'G': [0] * n,
    'T': [0] * n
}

# Calculate the profile matrix
for seq in sequences:
    for i, nucleotide in enumerate(seq):
        profile[nucleotide][i] += 1

# Construct the consensus string
consensus = ''
for i in range(n):
    max_nucleotide = max(profile, key=lambda x: profile[x][i])
    consensus += max_nucleotide

# Print output in the required format
print("Result:")
print(f"\nConsensus String: {consensus}")
for nucleotide in "ACGT":
    print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")