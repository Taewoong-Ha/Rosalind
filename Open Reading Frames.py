# 파일 읽기
f = open('/Users/hataewoong/Downloads/rosalind_orf.txt', 'r')
lines = f.readlines()
dna_seq = ""
for line in lines:
    line = line.split("\n")[0]
    if line[0] == ">":
        pass
    else:
        dna_seq += line

# reverse complement
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
      
# stop
stop = ['TAA','TAG','TGA']

# dna to protein dictionary
dna_codon = {}
f = open('dan_codon_table.txt', 'r')
lines = f.readlines()
for line in lines:
    line = line.split("\t")
    line[1] = line[1].split('\n')
    dna_codon [line[0]] = line[1][0]
    
# atg index
def ATG_index(seq):
    a = seq.find("ATG")
    atg_index = []
    atg_index.append(a)

    while seq[a+1:].find("ATG") != -1:
        a = seq[a+1:].find("ATG") + a +1
        atg_index.append(a)
        
    return atg_index

# atg index 기반 protein translation
def protin(index, seq):
    protein = ""
    # 이중 포문 break 할 때 사용
    breaker = False
    break_point = "Stop"
    # atg index 기반으로 seq을 codon으로 구분
    split_dna = list(map(''.join, zip(*[iter(seq[index:])] * 3)))
    # codon에 stop codon이 존재하면 orf니까 진행하고 아니면 split_dna 자체를 제거
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
            
    # 여기는 protein seq 뒤에 Stop가 붙어서 그걸 떼놓기 위한 작업
    if protein[-4:] != "Stop":
        protein = ""
    else:
        protein = protein[0:-4]
            
            
    return protein

# atg index에 따라서 forward, reverse에 따라 protein 
res = []
for i in ATG_index(dna_seq):
    res.append(protein(i, dna_seq))
for j in ATG_index(dna_seq_rev):
    res.append(protein(j, dna_seq_rev))

res = set(res)    
for k in res:
    print(k)
