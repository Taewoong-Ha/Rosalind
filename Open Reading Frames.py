f = open('/Users/hataewoong/Downloads/rosalind_orf-5.txt', 'r')
lines = f.readlines()
dna_seq = ""
for line in lines:
    line = line.split("\n")[0]
    if line[0] == ">":
        pass
    else:
        dna_seq += line

dna_seq_rev = ''
for i in dna_seq[::-1]:
    if i == "G":
        dna_seq_rev += "C"
    elif i == "C":
        dna_seq_rev += "G"
    elif i == "A":
        dna_seq_rev += "T"
    elif i == "T":
        dna_seq_rev += "A"
        
stop = ['TAA','TAG','TGA']


dna_codon = {}
f = open('dan_codon_table.txt', 'r')
lines = f.readlines()
for line in lines:
    line = line.split("\t")
    line[1] = line[1].split('\n')
    dna_codon [line[0]] = line[1][0]
    

def ATG_index(seq):
    a = seq.find("ATG")
    atg_index = []
    atg_index.append(a)

    while seq[a+1:].find("ATG") != -1:
        a = seq[a+1:].find("ATG") + a +1
        atg_index.append(a)
        
    return atg_index


def protin(index, seq):
    protein = ""
    breaker = False
    break_point = "Stop"

    split_dna = list(map(''.join, zip(*[iter(seq[index:])] * 3)))
    for i in stop:
        if i in split_dna:
            for j in split_dna:
                protein += dna_codon[j]
                if dna_codon[j] == "Stop":
                    breaker = True
                    break
            
                else:
                    protein += dna_codon[i]
            if breaker == True:
                break
                
        else: 
            split_dna = []

    if protein[-4:] != "Stop":
        protein = ""
    else:
        protein = protein[0:-4]
            
            
    return protein

res = []
for i in ATG_index(dna_seq):
    res.append(protein(i, dna_seq))
for j in ATG_index(dna_seq_rev):
    res.append(protein(j, dna_seq_rev))

res = set(res)    
for k in res:
    print(k)
