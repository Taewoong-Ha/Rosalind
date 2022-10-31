# seq 2개를 dic -> 리스트
seq = {}
f = open('C:/Users/user/Downloads/rosalind_sseq.txt','r')
lines = f.readlines()
for line in lines:
    if line.find('>') == 0:
        key = line.split('>')[1]
        key = key.split('\n')[0]
        seq[key] = '' 
    else:
        line = line.split('\n')[0]
        seq[key] += line
seq = list(seq.values())
seq1 = seq[0]
seq2 = seq[1]

# 1. seq2의 전부를 돈다.
# 2. seq2의 첫번째 서열이 있는 seq1의 위치를 리스트로 저장
# 3. seq2의 첫번째 서열이 있는 seq1의 위치 이후 부터 seq2의 두번째 서열을 찾고 리스트에 append함 -> 이걸 끝까지 반복
lst = []
for i in range(len(seq2)):
    indices = ""
    if i == 0:
        print(i)
        indices = seq1.find(seq2[0])+1 
        lst.append(indices)
    else:
        indices = seq1 [ int(lst[i-1] ) : ].find(seq2[i])  +1+  int(lst[i-1])
        lst.append(indices)
print(lst)

# a b c 형태로 읽는다.
aa = ""
for i in lst:
    aa = aa + str(i) + " "
print(aa)
