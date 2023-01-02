
#Finding a Motif in DNA solved by 24085
# 파일 읽고 긴 seq, 짧은 seq 구분
f = open('C:/Users/user/Downloads/rosalind_subs (2).txt', 'r')
lines = f.readlines()
seq1 = lines[0].split('\n')[0]
seq2 = lines[1].split('\n')[0]

# 일치하는 부분이 어디인가???
perfect = ''

# seq1을 전부 읽는데, seq2의 길이만큼 이동하면서 읽고 seq2와 완벽히 일치하는 부분의 intex 저장
for i in range(0,len(seq1)):
    if seq1[i:len(seq2)+i] == seq2:
        perfect = perfect + str(i+1) + ' '
        
perfect
