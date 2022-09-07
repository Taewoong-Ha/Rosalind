## Problem
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)


## Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

## Sample Output
MVYIADKQHVASREAYGHMFKVCA


### solved

dna_codon_table = {
"TTT" : "F"      , "CTT" : "L",      "ATT": "I",      "GTT":"V",
"TTC" : "F"      , "CTC" : "L",      "ATC": "I",      "GTC":"V",
"TTA" : "L"      , "CTA" : "L",      "ATA": "I",      "GTA":"V",
"TTG" : "L"      , "CTG" : "L",      "ATG": "M",      "GTG":"V",
"TCT" : "S"      , "CCT" : "P",      "ACT": "T",      "GCT":"A",
"TCC" : "S"      , "CCC" : "P",      "ACC": "T",      "GCC":"A",
"TCA" : "S"      , "CCA" : "P",      "ACA": "T",      "GCA":"A",
"TCG" : "S"      , "CCG" : "P",      "ACG": "T",      "GCG":"A",
"TAT" : "Y"      , "CAT" : "H",      "AAT": "N",      "GAT":"D",
"TAC" : "Y"      , "CAC" : "H",      "AAC": "N",      "GAC":"D",
"TAA" : "Stop"   , "CAA" : "Q",      "AAA": "K",      "GAA":"E",
"TAG" : "Stop"   , "CAG" : "Q",      "AAG": "K",      "GAG":"E",
"TGT" : "C"      , "CGT" : "R",      "AGT": "S",      "GGT":"G",
"TGC" : "C"      , "CGC" : "R",      "AGC": "S",      "GGC":"G",
"TGA" : "Stop"   , "CGA" : "R",      "AGA": "R",      "GGA":"G",
"TGG" : "W"      , "CGG" : "R",      "AGG": "R",      "GGG":"G", 
}

f = open('C:/Users/user/Downloads/rosalind_splc.txt', 'r')
lines = f.readlines()
dna_string = {}

for line in lines:
    if line.find(">") == 0:
        key = line.split(">")[1]
        key = key.split("\n")[0]
        dna_string[key] = ""
    else:
        line = line.split("\n")[0]
        dna_string[key] += line

print(len(dna_string.values()))

for i in range(len(dna_string.values())):
    if i == 0:
        seq = list(dna_string.values())[i]
    else:
        seq = seq.replace(list(dna_string.values())[i],"")
        
print(seq)


protein = ""
for i in range(0, len(seq),3):
    if dna_codon_table[DNA[i:i+3]] == "Stop":
        break
    else:
        protein +=  dna_codon_table[DNA[i:i+3]]

        
print(protein)
