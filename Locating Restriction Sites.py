# 파일 불러오기
f = open('/Users/hataewoong/Downloads/rosalind_revp.txt', 'r')
lines = f.readlines()
seq = ""
for line in lines:
    line = line.split("\n")[0]
    if line[0] == ">":
        pass
    else:
        seq += line

# 거꾸로 읽기
seq_rev =""
for i in seq[::-1]:
    if i == "A":
        seq_rev += "T"
    elif i == "T":
        seq_rev += "A"
    elif i == "G":
        seq_rev += "C"
    elif i == "C":
        seq_rev += "G"
        
        
# seq 길이만큼 읽는다
# palindromic range 4~12
# seq의 첫번째 문자는 따로 지정해줘야함
# forward: TCAATGCATGCGGGTCTATATGCAT
# reverse: ATGCATATAGACCCGCATGCATTGA
print(seq[5:11]) # GCATGC
print(seq_rev[-11:-5]) # GCATGC
print(seq[20:24]) # TGCA
print(seq_rev[-24:-20]) # TGCA



for j in range(len(seq)):
    for i in range(4,13):
        if j == 0:
            if seq[j:j+i]  == seq_rev[-i:]:
                print(j+1, i)
        else:
            if seq[j:j+i] == seq_rev[-j-i:-j]:
                if len(seq[j:j+i]) > 2:
                    if j+i > len(seq):
                        pass
                    else: 
                        print(j+1, i)
    #                     print(seq[j:j+i])
    #                     print(seq_rev[-j-i:-j])
                else:
                    pass
            else:
                pass
