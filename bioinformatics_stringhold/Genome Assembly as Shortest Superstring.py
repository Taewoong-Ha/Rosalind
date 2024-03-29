import numpy as np

def long_common_substring(seq1, seq2):
    # 이 부분에서 실수함 # 배열을 DF라 가정했을 때 앞이 행 뒤가 열
    lcs = np.zeros((len(seq2) + 1, len(seq1)+ 1) ) # 행 열
    for i in range(len(seq2) + 1 ):
        for j in range(len(seq1) + 1):
            if i == 0 or j == 0:  # index가 0 일때 모두 0으로 처리
                lcs[i][j] = 0            
            elif seq2[i-1] == seq1[j-1]: # 공통부분이면 lcs의 해당 위치에 표시
                lcs[i][j] = lcs[i-1][j-1] + 1            
            else: # 아니라면 0 이건 그냥 안해도 되는데 가시화를 위해서 함
                lcs[i][j] = 0
                
    ans = 0
    while  True:
        x = lcs[np.argmax(lcs) // (len(seq1) + 1) - ans][np.argmax(lcs) % (len(seq1) + 1 ) - ans]
        if x != 0:
            ans += 1
        elif x == 0:
            # print(ans-1)
            break

    seq1_only = seq1[ : (np.argmax(lcs) % (len(seq1) + 1 )) - ans]
    common_seq = seq1[ (np.argmax(lcs) % (len(seq1) + 1 )) - ans: np.argmax(lcs) % (len(seq1) + 1 )]
    seq2_only = seq2[np.argmax(lcs) % (len(seq1)):]
    se1_union_seq2 = seq1_only + common_seq + seq2_only
    return se1_union_seq2


# seq을 딕 -> 리스트
seq = {}
f = open('/Users/hataewoong/Downloads/rosalind_long-2.txt','r')
lines = f.readlines()
for line in lines:
    if line.find('>') == 0:
        key = line.split('>')[1]
        key = key.split('\n')[0]
        seq[key] = '' 
    else:
        line = line.split('\n')[0]
        seq[key] += line
seq_list = list(seq.values())


# seq길이만큼 반복하는데, 첫번째꺼는 지들끼리 비교하고 그 이후는 앞의 결과물과 비교함
for i in range(len(seq_list)):
    if i == 0 :
        lnn = long_common_substring(seq_list[i], seq_list[i])
    else :
        lnn = long_common_substring(lnn, seq_list[i])

print(lnn)
