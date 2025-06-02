

def readFile(filepath):
    """Reading a file and returning a list of lines"""
    with open(filepath, 'r') as f:
        return[l.strip() for l in f.readlines()]
    
def gc_content(sequence):
    gc_content = ((sequence.count('G') + sequence.count('C'))/len(sequence)*100)
    return gc_content

filepath = "C:\\Users\\Mahesh\\OneDrive\\Desktop\\bio-info in python\\roselind problems\\stronghold\\gc_content.txt"
# === Read data fromthe file(FASTA formatted file)
# Storing File contents in a list
FASTAFile = readFile(filepath)
# Dictionary for Labels + Data
FASTADict = {}
# String for holding the current label
FASTALabel = ""

print(FASTAFile)

# === Clean/Prepare the data(Format for ease of you with our gc_content function)
# converting FASTA/List file data into a dictionary
for line in FASTAFile:
    line = line.strip()

    if line.startswith('>'):
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    elif FASTALabel:
       FASTADict[FASTALabel] += line

print(f"\nFASTA Dictionary: \n{FASTADict}")

# === Format the data (Store the datain a convenient way)
# === Run needed operation on the data (pass the data to our gc_content function)    
#Using Dictionary Comprehension to genetrate a new dictionoary with GC content
RESULDict ={key: gc_content(value) for (key, value) in FASTADict.items()}

print(f"\nresult dictionary: \n{RESULDict}")

# Looking  for max value in the values() of our new dictionoary
MaxGCKey = max(RESULDict, key=RESULDict.get)

# === Collect result(Roselind submission in our case)
# Printing Rosalind formatted result
print(f"\nFinal result: \n{MaxGCKey[1:]}\n{RESULDict[MaxGCKey]}")

