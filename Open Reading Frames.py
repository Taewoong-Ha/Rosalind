dna_seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
rna_seq = ""
for i in dna_seq:
    if i == "T":
        rna_seq += "U"
    else:
        rna_seq += i

rna_codon = {}
f = open('C:/Users/user/Desktop/Rosalind/RNA_codon_.txt', 'r')
lines = f.readlines()
for line in lines:
    line = line.split("\t")
    line[1] = line[1].split('\n')
    rna_codon [line[0]] = line[1][0]
# print(rna_codon)

# print(rna_seq)

a = rna_seq.find("AUG")
start_index = []
start_index.append(a)

while rna_seq[a+1:].find("AUG") != -1:
    a = rna_seq[a+1:].find("AUG") + a +1
    start_index.append(a)
    
# print(start_index)

for i in start_index:
    print(i)
    Protein = ""
    split_mRNA = list(map(''.join, zip(*[iter(rna_seq[i:])] * length)))
    print(split_mRNA)
    for rna in split_mRNA:
        for key in rna_codon.keys():
            if key == rna:
                if rna_codon[key] == "Stop":
                    pass
                
                Protein += rna_codon[key]
    print(Protein)
    
    
    
    
rna_seq_reverse = ""
for i in rna_seq[::-1]:
    if i == "G":
        rna_seq_reverse += "C"
    elif i == "C":
        rna_seq_reverse += "G"
    elif i == "A":
        rna_seq_reverse += "U"
    elif i == "U":
        rna_seq_reverse += "A"
        
