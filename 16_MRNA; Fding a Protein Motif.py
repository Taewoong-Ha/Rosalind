## Problem
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.
You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into
http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following
http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.
Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

## Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

## Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614

## 고도화 필요

## def
def finding_protein_motif(seq):
    motif = []
    where_motif = []
    for i in range(0,len(seq)):
        if i+4 > len(seq):
            pass
        elif i+3 > len(seq):
            pass
        elif i+2 > len(seq):
            pass
        elif i+1 > len(seq):
            pass
        elif seq[i] == "N":
            a = seq[i:i+4]
            if a[1] != "P" and a[3] != "P":
                if a[2] == "S" or a[2] == "T":
                    where_motif.append(i+1)
    print(where_motif)

import urllib.request
from urllib import request



## print
f = open('C:/Users/user/Downloads/rosalind_mprt.txt', 'r')
ff = f.readlines()
ID =[]
full_ID = []
for i in ff:
    if i.find("_") == -1:
        i = i.split("\n")[0]
        full_ID.append(i)
        ID.append(i)
    else:
        i = i.split("\n")[0]
        full_ID.append(i)
        i = i.split("_")[0]
        ID.append(i)

        
        
# print(ID)

for i in range(len(ID)):
    fastq_url = "http://www.uniprot.org/uniprot/" + ID[i] + ".fasta"
    write_path = "C:/Users/user/Downloads/seq.txt"
    urllib.request.urlretrieve(fastq_url, write_path)
    
    f = open('C:/Users/user/Downloads/seq.txt', 'r')
    lines = f.readlines()
    seq_string = {}
    
    for line in lines:
        if line.find('>') == 0:
            seq_string[ID[i]] = ""
        else:
            line = line.split('\n')[0]
            seq_string[ID[i]] += line
        

    print(full_ID[i])
    finding_protein_motif(seq_string[ID[i]]) 
