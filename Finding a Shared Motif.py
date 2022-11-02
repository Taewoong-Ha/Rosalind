# 힌트 1
# 2차원 배열을 통한 전수 조사
# print([0] * (len(Rosalind_1) + 1))
# print([[0]  for _ in range(len(Rosalind_2) + 1)]))

# 힌트 2
# 2차원 배열의 최대값 위치
# print(lcs)
# print(max(map(max, lcs)))
# print(np.argmax(lcs))
# print(np.argmax(lcs) // (len(Rosalind_1)+ 1))
# print(np.argmax(lcs) % (len(Rosalind_1) + 1))

# print(lcs[np.argmax(lcs) // (len(Rosalind_1)+ 1)][np.argmax(lcs) % (len(Rosalind_1) + 1)])



# seq 
Rosalind_1 = "ABCDEF"
Rosalind_2 = "GBCDFE"
Rosalind_3 = "ATACA"

# Result AC
# seq길이 + 1의 길이의 배열 생성
lcs = [[0] * (len(Rosalind_1) + 1) for _ in range(len(Rosalind_2) + 1)]
# 배열에 일치하면 값 넣고 아님 말고
for i in range(len(Rosalind_1) + 1):
    for j in range(len(Rosalind_2) +1 ):
        if i == 0 or j == 0:
            lcs[i][j] = 0
        elif Rosalind_1[i-1] == Rosalind_2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = 0
           
        
# 배열위해 numpy        
import numpy as np

# seq1과 seq2사이의 가장 긴 공통 부분을 찾기 위해서 함수 선언
def long_common_substring(seq1, seq2):
    # 이 부분에서 실수함 # 배열을 DF라 가정했을 때 앞이 행 뒤가 열
    lcs = lcs = np.zeros((len(seq2) + 1, len(seq1)+ 1) ) # 행 열
    # 이중 포문
    for i in range(len(seq2) + 1 ):
        for j in range(len(seq1) + 1):
            # index가 0 일때 모두 0으로 처리
            if i == 0 or j == 0:
                lcs[i][j] = 0
            # 공통부분이면 lcs의 해당 위치에 표시
            elif seq2[i-1] == seq1[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            # 아니라면 0 이건 그냥 안해도 되는데 가시화를 위해서 함
            else:
                lcs[i][j] = 0
    
    # 이것도 안해도 되지만 함
    # 좀 더 쉬운건 
    # common_seq = seq1[ (np.argmax(lcs) % (len(seq1) + 1 )) - ans: np.argmax(lcs) % (len(seq1) + 1 )]
    ans = 0
    while  True:
        x = lcs[np.argmax(lcs) // (len(seq1) + 1) - ans][np.argmax(lcs) % (len(seq1) + 1 ) - ans]
        if x != 0:
            ans += 1
        elif x == 0:
            # print(ans-1)
            break

    common_seq = seq1[ (np.argmax(lcs) % (len(seq1) + 1 )) - ans: np.argmax(lcs) % (len(seq1) + 1 )]
    return common_seq


# seq을 딕 -> 리스트
seq = {}
f = open('C:/Users/user/Downloads/rosalind_lcsm.txt','r')
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
